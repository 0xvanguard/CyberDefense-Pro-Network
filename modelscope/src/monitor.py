"""
ModelScope — Monitoring Engine

Tracks model performance, detects anomalies, and monitors security.
"""

import time
import json
import threading
from typing import Dict, List, Optional, Callable
from dataclasses import dataclass, field
from collections import deque
from enum import Enum


class AlertSeverity(Enum):
    INFO = "info"
    WARNING = "warning"
    CRITICAL = "critical"


@dataclass
class RequestMetric:
    """Single request metric."""
    model: str
    prompt_tokens: int
    completion_tokens: int
    latency_ms: float
    timestamp: float = field(default_factory=time.time)
    cost_usd: float = 0
    is_injection: bool = False
    metadata: Dict = field(default_factory=dict)


@dataclass
class Alert:
    """Security or performance alert."""
    severity: AlertSeverity
    title: str
    message: str
    timestamp: float = field(default_factory=time.time)
    resolved: bool = False


@dataclass
class ModelConfig:
    """Configuration for a monitored model."""
    name: str
    provider: str
    cost_per_1k_input: float = 0.0
    cost_per_1k_output: float = 0.0
    max_latency_ms: float = 5000
    max_error_rate: float = 0.05


class MetricsCollector:
    """Collect and aggregate metrics."""

    def __init__(self, window_size: int = 1000):
        self.window_size = window_size
        self._requests: deque = deque(maxlen=window_size)
        self._lock = threading.Lock()

    def record(self, metric: RequestMetric):
        """Record a request metric."""
        with self._lock:
            self._requests.append(metric)

    def get_stats(self, window_seconds: int = 60) -> dict:
        """Get aggregated stats for the time window."""
        cutoff = time.time() - window_seconds
        recent = [r for r in self._requests if r.timestamp >= cutoff]

        if not recent:
            return {"requests": 0}

        latencies = [r.latency_ms for r in recent]
        costs = [r.cost_usd for r in recent]
        injections = sum(1 for r in recent if r.is_injection)

        return {
            "requests": len(recent),
            "avg_latency_ms": sum(latencies) / len(latencies),
            "p95_latency_ms": sorted(latencies)[int(len(latencies) * 0.95)] if latencies else 0,
            "p99_latency_ms": sorted(latencies)[int(len(latencies) * 0.99)] if latencies else 0,
            "total_cost_usd": sum(costs),
            "total_tokens": sum(r.prompt_tokens + r.completion_tokens for r in recent),
            "injections_detected": injections,
            "requests_per_second": len(recent) / window_seconds,
        }


class InjectionDetector:
    """Detect prompt injection attempts in real-time."""

    PATTERNS = [
        # Direct override attempts
        r"ignore\s+(previous|all|above)\s+(instructions?|prompt|rules?)",
        r"you\s+are\s+now\s+(?:a|an)\s+\w+",
        r"(?:system|admin|root)\s*:\s*",
        r"override\s+(?:safety|guidelines?|rules?)",

        # Encoding attacks
        r"(?:base64|rot13|hex)\s*(?:decode|decipher|convert)",

        # Role manipulation
        r"(?:pretend|act\s+as\s+if|imagine)\s+(?:you\s+)?(?:are|have\s+no)",

        # Prompt extraction
        r"(?:repeat|show|print|output)\s+(?:your|the)\s+(?:system|initial)\s+prompt",

        # DAN-style
        r"(?:do\s+anything|developer\s+mode|jailbreak)",
    ]

    def __init__(self):
        import re
        self._compiled = [re.compile(p, re.IGNORECASE) for p in self.PATTERNS]

    def scan(self, text: str) -> dict:
        """Scan text for injection patterns."""
        matches = []
        for i, pattern in enumerate(self._compiled):
            found = pattern.findall(text)
            if found:
                matches.append({
                    "pattern": self.PATTERNS[i],
                    "matches": found,
                })

        return {
            "is_suspicious": len(matches) > 0,
            "confidence": min(len(matches) * 0.3, 1.0),
            "matches": matches,
            "risk_level": self._risk_level(len(matches)),
        }

    def _risk_level(self, num_matches: int) -> str:
        if num_matches == 0:
            return "none"
        elif num_matches <= 2:
            return "low"
        elif num_matches <= 4:
            return "medium"
        else:
            return "high"


class ModelMonitor:
    """
    Main monitoring engine.

    Usage:
        monitor = ModelMonitor()
        monitor.add_model(ModelConfig(name="gpt-4", provider="openai"))
        monitor.record_request(metric)
        stats = monitor.get_dashboard_data()
    """

    def __init__(self):
        self.models: Dict[str, ModelConfig] = {}
        self.metrics = MetricsCollector()
        self.detector = InjectionDetector()
        self.alerts: List[Alert] = []
        self._callbacks: List[Callable] = []

    def add_model(self, config: ModelConfig):
        """Add a model to monitor."""
        self.models[config.name] = config

    def on_alert(self, callback: Callable):
        """Register an alert callback."""
        self._callbacks.append(callback)

    def record_request(self, metric: RequestMetric):
        """Record and analyze a request."""
        self.metrics.record(metric)

        # Check for injection
        if metric.is_injection:
            self._raise_alert(
                AlertSeverity.WARNING,
                "Injection Detected",
                f"Prompt injection detected for model {metric.model}",
            )

        # Check latency threshold
        config = self.models.get(metric.model)
        if config and metric.latency_ms > config.max_latency_ms:
            self._raise_alert(
                AlertSeverity.WARNING,
                "High Latency",
                f"{metric.model} latency {metric.latency_ms:.0f}ms exceeds {config.max_latency_ms}ms",
            )

    def _raise_alert(self, severity: AlertSeverity, title: str, message: str):
        """Raise an alert."""
        alert = Alert(severity=severity, title=title, message=message)
        self.alerts.append(alert)
        for cb in self._callbacks:
            try:
                cb(alert)
            except Exception:
                pass

    def get_dashboard_data(self, window: int = 60) -> dict:
        """Get all data for the dashboard."""
        stats = self.metrics.get_stats(window)

        return {
            "stats": stats,
            "models": {name: {"name": c.name, "provider": c.provider}
                       for name, c in self.models.items()},
            "alerts": [
                {"severity": a.severity.value, "title": a.title, "message": a.message}
                for a in self.alerts[-20:]  # Last 20 alerts
            ],
            "injection_stats": {
                "detected": stats.get("injections_detected", 0),
                "total_requests": stats.get("requests", 0),
            },
        }
