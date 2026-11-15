"""Typed DTOs, protocols, errors, and dependency injection container."""

from __future__ import annotations

from collections.abc import Callable
from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any, Protocol


class DomainError(Exception):
    """Base domain exception."""


class ValidationError(DomainError):
    """Raised when domain invariants or input bounds are violated."""


class InsufficientFundsError(DomainError):
    """Raised when an account lacks funds for a debit operation."""


@dataclass(frozen=True, slots=True)
class AccountTransaction:
    """Immutable ledger entry representing a balance mutation."""

    transaction_id: str
    account_id: str
    kind: str
    amount_cents: int
    balance_after_cents: int
    timestamp: datetime


@dataclass(frozen=True, slots=True)
class AccountSnapshot:
    """Point-in-time state of a ledger account."""

    account_id: str
    owner: str
    balance_cents: int
    currency: str = "MAD"


@dataclass(frozen=True, slots=True)
class QueryPlanResult:
    """Parameterized SQL statement and bound positional arguments."""

    operation: str
    table: str
    sql: str
    params: tuple[Any, ...]


@dataclass(frozen=True, slots=True)
class ComplexityReport:
    """Empirical comparison metrics and inferred complexity tier."""

    algorithm: str
    input_size: int
    comparisons: int
    elapsed_ms: float
    complexity_class: str


class Clock(Protocol):
    """Time source abstraction for deterministic testing."""

    def now(self) -> datetime: ...


class SystemClock:
    """UTC wall-clock provider."""

    def now(self) -> datetime:
        return datetime.now(timezone.utc)


class LedgerRepository(Protocol):
    """Persistence contract for accounts and immutable transactions."""

    def save_account(self, snapshot: AccountSnapshot) -> None: ...

    def get_account(self, account_id: str) -> AccountSnapshot | None: ...

    def append_transaction(self, entry: AccountTransaction) -> None: ...

    def list_transactions(self, account_id: str) -> list[AccountTransaction]: ...


class MetricsSink(Protocol):
    """Observability contract for counters and timings."""

    def increment(self, metric: str, value: int = 1, **tags: str) -> None: ...

    def observe_ms(self, metric: str, duration_ms: float, **tags: str) -> None: ...


@dataclass
class InMemoryLedgerRepository:
    """Thread-safe-by-copy in-memory repository for unit and stress tests."""

    _accounts: dict[str, AccountSnapshot] = field(default_factory=dict)
    _ledger: dict[str, list[AccountTransaction]] = field(default_factory=dict)

    def save_account(self, snapshot: AccountSnapshot) -> None:
        self._accounts[snapshot.account_id] = snapshot

    def get_account(self, account_id: str) -> AccountSnapshot | None:
        return self._accounts.get(account_id)

    def append_transaction(self, entry: AccountTransaction) -> None:
        self._ledger.setdefault(entry.account_id, []).append(entry)

    def list_transactions(self, account_id: str) -> list[AccountTransaction]:
        return list(self._ledger.get(account_id, []))


class ServiceContainer:
    """Lightweight factory/singleton dependency injection container."""

    def __init__(self) -> None:
        self._factories: dict[type[Any], Callable[[ServiceContainer], Any]] = {}
        self._singletons: dict[type[Any], Any] = {}

    def register_singleton(
        self, interface: type[Any], factory: Callable[[ServiceContainer], Any]
    ) -> None:
        self._factories[interface] = factory
        self._singletons.pop(interface, None)

    def resolve(self, interface: type[Any]) -> Any:
        if interface in self._singletons:
            return self._singletons[interface]
        factory = self._factories.get(interface)
        if factory is None:
            raise KeyError(f"No provider registered for {interface.__name__}")
        instance = factory(self)
        self._singletons[interface] = instance
        return instance
