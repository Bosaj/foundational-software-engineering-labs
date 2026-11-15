"""Architecture, security, observability, and load tests for fse_core."""

from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path
import sys
import unittest

SRC_DIR = str(Path(__file__).resolve().parents[1] / "src")
if SRC_DIR not in sys.path:
    sys.path.insert(0, SRC_DIR)

from fse_core import (  # noqa: E402
    AlgorithmicBenchmarkEngine,
    BankingLedgerService,
    InMemoryMetricsSink,
    InsufficientFundsError,
    RelationalSchemaPlanner,
    ServiceContainer,
    ValidationError,
)
from fse_core.contracts import InMemoryLedgerRepository  # noqa: E402


class _FixedClock:
    def now(self) -> datetime:
        return datetime(2026, 1, 15, 12, 0, tzinfo=timezone.utc)


def _build_container() -> ServiceContainer:
    container = ServiceContainer()
    container.register_singleton(InMemoryMetricsSink, lambda _: InMemoryMetricsSink())
    container.register_singleton(
        InMemoryLedgerRepository, lambda _: InMemoryLedgerRepository()
    )
    container.register_singleton(
        BankingLedgerService,
        lambda c: BankingLedgerService(
            repository=c.resolve(InMemoryLedgerRepository),
            clock=_FixedClock(),
            metrics=c.resolve(InMemoryMetricsSink),
        ),
    )
    container.register_singleton(
        RelationalSchemaPlanner,
        lambda c: RelationalSchemaPlanner(metrics=c.resolve(InMemoryMetricsSink)),
    )
    container.register_singleton(
        AlgorithmicBenchmarkEngine,
        lambda c: AlgorithmicBenchmarkEngine(metrics=c.resolve(InMemoryMetricsSink)),
    )
    return container


class TestFseArchitecture(unittest.TestCase):
    def test_atomic_transfers_and_insufficient_funds(self) -> None:
        container = _build_container()
        ledger: BankingLedgerService = container.resolve(BankingLedgerService)
        repo: InMemoryLedgerRepository = container.resolve(InMemoryLedgerRepository)

        ledger.open_account("ACC-1", "Oussama", initial_cents=10_000)
        ledger.open_account("ACC-2", "Lab", initial_cents=2_500)

        src, dst = ledger.transfer("ACC-1", "ACC-2", 4_000)
        self.assertEqual(src.balance_cents, 6_000)
        self.assertEqual(dst.balance_cents, 6_500)

        with self.assertRaises(InsufficientFundsError):
            ledger.transfer("ACC-1", "ACC-2", 99_999)

        # Ensure rejected transfer mutated neither balance nor audit trail
        self.assertEqual(repo.get_account("ACC-1").balance_cents, 6_000)
        self.assertEqual(len(repo.list_transactions("ACC-1")), 2)

    def test_ledger_type_and_boundary_validation(self) -> None:
        container = _build_container()
        ledger: BankingLedgerService = container.resolve(BankingLedgerService)
        ledger.open_account("ACC-X", "Tester")

        with self.assertRaises(TypeError):
            ledger.deposit("ACC-X", True)  # type: ignore[arg-type]
        with self.assertRaises(ValidationError):
            ledger.deposit("ACC-X", 0)
        with self.assertRaises(ValidationError):
            ledger.transfer("ACC-X", "ACC-X", 100)

    def test_sql_planner_blocks_injection_identifiers(self) -> None:
        container = _build_container()
        planner: RelationalSchemaPlanner = container.resolve(RelationalSchemaPlanner)

        plan = planner.build_select(
            "students",
            columns=("id", "full_name"),
            where={"cohort": "ENSIAS-2026"},
            limit=25,
        )
        self.assertEqual(
            plan.sql,
            "SELECT id, full_name FROM students WHERE cohort = ? LIMIT ?",
        )
        self.assertEqual(plan.params, ("ENSIAS-2026", 25))

        with self.assertRaises(ValidationError):
            planner.build_select("students; DROP TABLE users;--")
        with self.assertRaises(ValidationError):
            planner.build_insert("students", {"name OR 1=1": "bad"})

    def test_algorithms_complexity_and_stress_observability(self) -> None:
        container = _build_container()
        engine: AlgorithmicBenchmarkEngine = container.resolve(AlgorithmicBenchmarkEngine)
        metrics: InMemoryMetricsSink = container.resolve(InMemoryMetricsSink)
        ledger: BankingLedgerService = container.resolve(BankingLedgerService)

        unsorted = list(range(256, 0, -1))
        sorted_items, sort_report = engine.merge_sort(unsorted)
        self.assertEqual(sorted_items, list(range(1, 257)))
        self.assertEqual(sort_report.complexity_class, "O(n log n)")

        idx, search_report = engine.binary_search(sorted_items, 199)
        self.assertEqual(idx, 198)
        self.assertEqual(search_report.complexity_class, "O(log n)")

        ledger.open_account("STRESS", "LoadRunner", initial_cents=1_000_000)
        for _ in range(250):
            ledger.deposit("STRESS", 100)
            ledger.withdraw("STRESS", 50)

        self.assertEqual(metrics.counters["ledger.deposits"], 250)
        self.assertEqual(metrics.counters["ledger.withdrawals"], 250)
        self.assertLess(metrics.percentile_ms("ledger.deposit_ms", 95), 50.0)


if __name__ == "__main__":
    unittest.main()
