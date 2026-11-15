"""Core domain services covering OOP banking, safe SQL planning, and algorithm benchmarks."""

from __future__ import annotations

from collections.abc import Sequence
from itertools import count
import math
import re
import time
from typing import Any

from .contracts import (
    AccountSnapshot,
    AccountTransaction,
    Clock,
    ComplexityReport,
    InsufficientFundsError,
    LedgerRepository,
    MetricsSink,
    QueryPlanResult,
    SystemClock,
    ValidationError,
)
from .telemetry import InMemoryMetricsSink

_IDENTIFIER_RE = re.compile(r"^[A-Za-z_][A-Za-z0-9_]*$")


def _validate_identifier(name: str, kind: str) -> str:
    if not isinstance(name, str):
        raise TypeError(f"{kind} must be a string")
    if not _IDENTIFIER_RE.fullmatch(name):
        raise ValidationError(f"Unsafe or invalid SQL {kind}: {name!r}")
    return name


class BankingLedgerService:
    """Clean-architecture ledger service using integer minor units and atomic transfers."""

    def __init__(
        self,
        repository: LedgerRepository,
        clock: Clock | None = None,
        metrics: MetricsSink | None = None,
    ) -> None:
        self._repo = repository
        self._clock = clock or SystemClock()
        self._metrics = metrics or InMemoryMetricsSink()
        self._seq = count(1)

    def open_account(
        self, account_id: str, owner: str, initial_cents: int = 0, currency: str = "MAD"
    ) -> AccountSnapshot:
        if not isinstance(account_id, str) or not account_id.strip():
            raise ValidationError("account_id must be a non-empty string")
        if not isinstance(owner, str) or not owner.strip():
            raise ValidationError("owner must be a non-empty string")
        if not isinstance(initial_cents, int) or isinstance(initial_cents, bool):
            raise TypeError("initial_cents must be an integer")
        if initial_cents < 0:
            raise ValidationError("initial_cents cannot be negative")
        if self._repo.get_account(account_id) is not None:
            raise ValidationError(f"Account already exists: {account_id}")

        snapshot = AccountSnapshot(
            account_id=account_id,
            owner=owner.strip(),
            balance_cents=initial_cents,
            currency=currency,
        )
        self._repo.save_account(snapshot)
        if initial_cents > 0:
            self._record_tx(account_id, "OPENING_DEPOSIT", initial_cents, initial_cents)
        self._metrics.increment("ledger.accounts_opened", currency=currency)
        return snapshot

    def deposit(self, account_id: str, amount_cents: int) -> AccountSnapshot:
        started = time.perf_counter()
        self._validate_positive_cents(amount_cents)
        account = self._require_account(account_id)
        updated = AccountSnapshot(
            account_id=account.account_id,
            owner=account.owner,
            balance_cents=account.balance_cents + amount_cents,
            currency=account.currency,
        )
        self._repo.save_account(updated)
        self._record_tx(account_id, "DEPOSIT", amount_cents, updated.balance_cents)
        self._metrics.increment("ledger.deposits")
        self._metrics.observe_ms(
            "ledger.deposit_ms", (time.perf_counter() - started) * 1000.0
        )
        return updated

    def withdraw(self, account_id: str, amount_cents: int) -> AccountSnapshot:
        started = time.perf_counter()
        self._validate_positive_cents(amount_cents)
        account = self._require_account(account_id)
        if account.balance_cents < amount_cents:
            self._metrics.increment("ledger.insufficient_funds")
            raise InsufficientFundsError(
                f"Account {account_id} has {account.balance_cents} cents, requested {amount_cents}"
            )
        updated = AccountSnapshot(
            account_id=account.account_id,
            owner=account.owner,
            balance_cents=account.balance_cents - amount_cents,
            currency=account.currency,
        )
        self._repo.save_account(updated)
        self._record_tx(account_id, "WITHDRAWAL", -amount_cents, updated.balance_cents)
        self._metrics.increment("ledger.withdrawals")
        self._metrics.observe_ms(
            "ledger.withdraw_ms", (time.perf_counter() - started) * 1000.0
        )
        return updated

    def transfer(
        self, source_id: str, target_id: str, amount_cents: int
    ) -> tuple[AccountSnapshot, AccountSnapshot]:
        if source_id == target_id:
            raise ValidationError("source_id and target_id must differ")
        self._validate_positive_cents(amount_cents)
        source = self._require_account(source_id)
        target = self._require_account(target_id)
        if source.currency != target.currency:
            raise ValidationError("Cross-currency transfers require explicit FX conversion")
        if source.balance_cents < amount_cents:
            self._metrics.increment("ledger.transfer_rejected")
            raise InsufficientFundsError("Insufficient funds for transfer")

        new_source = AccountSnapshot(
            account_id=source.account_id,
            owner=source.owner,
            balance_cents=source.balance_cents - amount_cents,
            currency=source.currency,
        )
        new_target = AccountSnapshot(
            account_id=target.account_id,
            owner=target.owner,
            balance_cents=target.balance_cents + amount_cents,
            currency=target.currency,
        )
        self._repo.save_account(new_source)
        self._repo.save_account(new_target)
        self._record_tx(source_id, "TRANSFER_OUT", -amount_cents, new_source.balance_cents)
        self._record_tx(target_id, "TRANSFER_IN", amount_cents, new_target.balance_cents)
        self._metrics.increment("ledger.transfers")
        return new_source, new_target

    def _require_account(self, account_id: str) -> AccountSnapshot:
        account = self._repo.get_account(account_id)
        if account is None:
            raise ValidationError(f"Unknown account: {account_id}")
        return account

    @staticmethod
    def _validate_positive_cents(amount_cents: int) -> None:
        if not isinstance(amount_cents, int) or isinstance(amount_cents, bool):
            raise TypeError("amount_cents must be an integer")
        if amount_cents <= 0:
            raise ValidationError("amount_cents must be positive")

    def _record_tx(
        self, account_id: str, kind: str, amount_cents: int, balance_after_cents: int
    ) -> None:
        entry = AccountTransaction(
            transaction_id=f"tx-{next(self._seq):06d}",
            account_id=account_id,
            kind=kind,
            amount_cents=amount_cents,
            balance_after_cents=balance_after_cents,
            timestamp=self._clock.now(),
        )
        self._repo.append_transaction(entry)


class RelationalSchemaPlanner:
    """Builds injection-safe parameterized SQL CRUD query plans."""

    def __init__(self, metrics: MetricsSink | None = None) -> None:
        self._metrics = metrics or InMemoryMetricsSink()

    def build_select(
        self,
        table: str,
        columns: Sequence[str] | None = None,
        where: dict[str, Any] | None = None,
        limit: int | None = None,
    ) -> QueryPlanResult:
        safe_table = _validate_identifier(table, "table")
        col_sql = "*"
        if columns:
            safe_cols = [_validate_identifier(col, "column") for col in columns]
            col_sql = ", ".join(safe_cols)

        params: list[Any] = []
        where_clauses: list[str] = []
        for col, value in (where or {}).items():
            safe_col = _validate_identifier(col, "column")
            where_clauses.append(f"{safe_col} = ?")
            params.append(value)

        sql = f"SELECT {col_sql} FROM {safe_table}"
        if where_clauses:
            sql += " WHERE " + " AND ".join(where_clauses)
        if limit is not None:
            if not isinstance(limit, int) or isinstance(limit, bool) or limit <= 0:
                raise ValidationError("limit must be a positive integer")
            sql += " LIMIT ?"
            params.append(limit)

        self._metrics.increment("sql.planned", operation="SELECT")
        return QueryPlanResult("SELECT", safe_table, sql, tuple(params))

    def build_insert(self, table: str, values: dict[str, Any]) -> QueryPlanResult:
        safe_table = _validate_identifier(table, "table")
        if not values:
            raise ValidationError("values cannot be empty for INSERT")
        safe_cols = [_validate_identifier(col, "column") for col in values]
        placeholders = ", ".join("?" for _ in safe_cols)
        sql = f"INSERT INTO {safe_table} ({', '.join(safe_cols)}) VALUES ({placeholders})"
        self._metrics.increment("sql.planned", operation="INSERT")
        return QueryPlanResult("INSERT", safe_table, sql, tuple(values.values()))


class AlgorithmicBenchmarkEngine:
    """Executes deterministic sorting/search labs and records exact comparison complexity."""

    def __init__(self, metrics: MetricsSink | None = None) -> None:
        self._metrics = metrics or InMemoryMetricsSink()

    def binary_search(self, sorted_items: Sequence[int], target: int) -> tuple[int, ComplexityReport]:
        started = time.perf_counter()
        low, high = 0, len(sorted_items) - 1
        comparisons = 0
        found_idx = -1
        while low <= high:
            mid = (low + high) // 2
            comparisons += 1
            val = sorted_items[mid]
            if val == target:
                found_idx = mid
                break
            comparisons += 1
            if val < target:
                low = mid + 1
            else:
                high = mid - 1
        elapsed_ms = (time.perf_counter() - started) * 1000.0
        report = ComplexityReport(
            algorithm="binary_search",
            input_size=len(sorted_items),
            comparisons=comparisons,
            elapsed_ms=elapsed_ms,
            complexity_class=self.classify_comparisons(len(sorted_items), comparisons),
        )
        self._metrics.observe_ms("algo.binary_search_ms", elapsed_ms)
        return found_idx, report

    def merge_sort(self, items: Sequence[int]) -> tuple[list[int], ComplexityReport]:
        started = time.perf_counter()
        comparisons = 0

        def _sort(chunk: list[int]) -> list[int]:
            nonlocal comparisons
            if len(chunk) <= 1:
                return chunk
            mid = len(chunk) // 2
            left = _sort(chunk[:mid])
            right = _sort(chunk[mid:])
            merged: list[int] = []
            i = j = 0
            while i < len(left) and j < len(right):
                comparisons += 1
                if left[i] <= right[j]:
                    merged.append(left[i])
                    i += 1
                else:
                    merged.append(right[j])
                    j += 1
            merged.extend(left[i:])
            merged.extend(right[j:])
            return merged

        result = _sort(list(items))
        elapsed_ms = (time.perf_counter() - started) * 1000.0
        report = ComplexityReport(
            algorithm="merge_sort",
            input_size=len(items),
            comparisons=comparisons,
            elapsed_ms=elapsed_ms,
            complexity_class=self.classify_comparisons(len(items), comparisons),
        )
        self._metrics.observe_ms("algo.merge_sort_ms", elapsed_ms)
        return result, report

    @staticmethod
    def classify_comparisons(n: int, comparisons: int) -> str:
        if n <= 1 or comparisons <= 2:
            return "O(1)"
        log_n = max(1.0, math.log2(n))
        if comparisons <= 2.5 * log_n:
            return "O(log n)"
        if comparisons <= 1.2 * n:
            return "O(n)"
        if comparisons <= 1.5 * n * log_n:
            return "O(n log n)"
        return "O(n^2)"
