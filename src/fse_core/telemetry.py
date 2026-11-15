"""In-memory telemetry counters and latency percentile tracker."""

from __future__ import annotations

from collections import defaultdict
import math


class InMemoryMetricsSink:
    """Zero-dependency metrics sink for local assertions and latency monitoring."""

    def __init__(self) -> None:
        self.counters: dict[str, int] = defaultdict(int)
        self.timings: dict[str, list[float]] = defaultdict(list)

    def increment(self, metric: str, value: int = 1, **tags: str) -> None:
        key = self._format_key(metric, tags)
        self.counters[key] += value

    def observe_ms(self, metric: str, duration_ms: float, **tags: str) -> None:
        key = self._format_key(metric, tags)
        self.timings[key].append(duration_ms)

    def percentile_ms(self, metric: str, pct: float, **tags: str) -> float:
        key = self._format_key(metric, tags)
        samples = sorted(self.timings.get(key, []))
        if not samples:
            return 0.0
        idx = min(len(samples) - 1, max(0, math.ceil((pct / 100.0) * len(samples)) - 1))
        return samples[idx]

    @staticmethod
    def _format_key(metric: str, tags: dict[str, str]) -> str:
        if not tags:
            return metric
        tag_str = ",".join(f"{k}={v}" for k, v in sorted(tags.items()))
        return f"{metric}{{{tag_str}}}"
