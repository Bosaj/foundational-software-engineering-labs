"""Modular domain architecture for foundational software engineering labs."""

from .contracts import (
    AccountSnapshot,
    AccountTransaction,
    ComplexityReport,
    DomainError,
    InsufficientFundsError,
    QueryPlanResult,
    ServiceContainer,
    ValidationError,
)
from .evaluator import (
    AlgorithmicBenchmarkEngine,
    BankingLedgerService,
    RelationalSchemaPlanner,
)
from .telemetry import InMemoryMetricsSink

__all__ = [
    "AccountSnapshot",
    "AccountTransaction",
    "AlgorithmicBenchmarkEngine",
    "BankingLedgerService",
    "ComplexityReport",
    "DomainError",
    "InMemoryMetricsSink",
    "InsufficientFundsError",
    "QueryPlanResult",
    "RelationalSchemaPlanner",
    "ServiceContainer",
    "ValidationError",
]
