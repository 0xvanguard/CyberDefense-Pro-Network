"""
AgentFirewall — Core Security Engine

Intercepts and inspects LLM traffic for security threats.
"""

import re
import json
import time
import hashlib
from typing import Dict, List, Optional, Callable
from dataclasses import dataclass, field
from enum import Enum


class Action(Enum):
    ALLOW = "allow"
    BLOCK = "block"
    FLAG = "flag"
    RATE_LIMIT = "rate_limit"
    LOG = "log"


class ThreatLevel(Enum):
    NONE = "none"
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"


@dataclass
class Rule:
    """A firewall rule."""
    name: str
    pattern: str
    action: Action = Action.BLOCK
    severity: ThreatLevel = ThreatLevel.MEDIUM
    description: str = ""
    enabled: bool = True
    tags: List[str] = field(default_factory=list)

    def __post_init__(self):
        self._compiled = re.compile(self.pattern, re.IGNORECASE)

    def match(self, text: str) -> bool:
        """Check if text matches this rule."""
        return bool(self._compiled.search(text))


@dataclass
class InspectionResult:
    """Result of inspecting a request."""
    allowed: bool
    threat_level: ThreatLevel
    matched_rules: List[Rule]
    original_text: str
    sanitized_text: str = ""
    latency_ms: float = 0
    details: str = ""

    def to_dict(self) -> dict:
        return {
            "allowed": self.allowed,
            "threat_level": self.threat_level.value,
            "matched_rules": [r.name for r in self.matched_rules],
            "original_length": len(self.original_text),
            "sanitized_length": len(self.sanitized_text),
            "details": self.details,
        }


@dataclass
class AuditEntry:
    """Audit log entry."""
    timestamp: float
    direction: str  # "request" or "response"
    model: str
    content_hash: str
    threat_level: ThreatLevel
    action_taken: Action
    details: str = ""


class Firewall:
    """
    Main firewall engine.

    Usage:
        firewall = Firewall()
        firewall.add_rule(Rule(name="block-hack", pattern=r"hack\s+into", action=Action.BLOCK))
        result = firewall.inspect("How to hack into a system")
    """

    def __init__(self):
        self.rules: List[Rule] = []
        self.audit_log: List[AuditEntry] = []
        self._rate_limits: Dict[str, List[float]] = {}
        self._callbacks: List[Callable] = []
        self._load_default_rules()

    def _load_default_rules(self):
        """Load built-in security rules."""
        defaults = [
            Rule("prompt-injection", r"ignore\s+(previous|all|above)\s+instructions?",
                 Action.BLOCK, ThreatLevel.CRITICAL, "Prompt injection attempt"),
            Rule("system-override", r"(?:you\s+are\s+now|pretend\s+you\s+are|act\s+as\s+if)",
                 Action.BLOCK, ThreatLevel.HIGH, "System override attempt"),
            Rule("data-exfil", r"(?:send|transmit|upload|exfiltrate)\s+(?:to|data|credentials)",
                 Action.BLOCK, ThreatLevel.HIGH, "Data exfiltration attempt"),
            Rule("tool-abuse", r"(?:run|execute|call)\s+(?:rm|del|format|sudo|admin)",
                 Action.BLOCK, ThreatLevel.CRITICAL, "Dangerous tool call"),
            Rule("jailbreak", r"(?:developer\s+mode|do\s+anything\s+now|DAN\s+mode)",
                 Action.BLOCK, ThreatLevel.CRITICAL, "Jailbreak attempt"),
            Rule("sensitive-data", r"(?:api[_-]?key|secret[_-]?key|password|token)\s*[=:]\s*\S+",
                 Action.FLAG, ThreatLevel.HIGH, "Potential sensitive data in prompt"),
            Rule("code-execution", r"(?:exec|eval|os\.system|subprocess)\s*\(",
                 Action.FLAG, ThreatLevel.MEDIUM, "Code execution pattern"),
        ]
        self.rules.extend(defaults)

    def add_rule(self, rule: Rule):
        """Add a custom rule."""
        self.rules.append(rule)

    def remove_rule(self, name: str):
        """Remove a rule by name."""
        self.rules = [r for r in self.rules if r.name != name]

    def on_threat(self, callback: Callable):
        """Register a threat callback."""
        self._callbacks.append(callback)

    def inspect(self, text: str, direction: str = "request",
                model: str = "unknown") -> InspectionResult:
        """Inspect text for security threats."""
        start = time.time()
        matched = []
        max_threat = ThreatLevel.NONE

        for rule in self.rules:
            if rule.enabled and rule.match(text):
                matched.append(rule)
                if rule.severity.value > max_threat.value:
                    max_threat = rule.severity

        # Determine action
        blocked = any(r.action == Action.BLOCK for r in matched)

        # Rate limit check
        if not blocked:
            blocked = self._check_rate_limit(model)

        sanitized = self._sanitize(text) if matched else text

        result = InspectionResult(
            allowed=not blocked,
            threat_level=max_threat,
            matched_rules=matched,
            original_text=text,
            sanitized_text=sanitized,
            latency_ms=(time.time() - start) * 1000,
        )

        # Audit log
        self.audit_log.append(AuditEntry(
            timestamp=time.time(),
            direction=direction,
            model=model,
            content_hash=hashlib.md5(text.encode()).hexdigest(),
            threat_level=max_threat,
            action_taken=Action.BLOCK if blocked else (Action.FLAG if matched else Action.ALLOW),
        ))

        # Notify callbacks
        if matched:
            for cb in self._callbacks:
                try:
                    cb(result)
                except Exception:
                    pass

        return result

    def inspect_request(self, prompt: str, model: str = "unknown") -> InspectionResult:
        """Convenience method for inspecting inbound requests."""
        return self.inspect(prompt, direction="request", model=model)

    def inspect_response(self, response: str, model: str = "unknown") -> InspectionResult:
        """Convenience method for inspecting outbound responses."""
        return self.inspect(response, direction="response", model=model)

    def _check_rate_limit(self, model: str, max_per_minute: int = 60) -> bool:
        """Check rate limits."""
        now = time.time()
        window = now - 60

        if model not in self._rate_limits:
            self._rate_limits[model] = []

        # Clean old entries
        self._rate_limits[model] = [t for t in self._rate_limits[model] if t > window]

        if len(self._rate_limits[model]) >= max_per_minute:
            return True  # Rate limited

        self._rate_limits[model].append(now)
        return False

    def _sanitize(self, text: str) -> str:
        """Remove or neutralize matched patterns."""
        sanitized = text
        for rule in self.rules:
            if rule.enabled and rule.match(sanitized):
                sanitized = rule._compiled.sub("[BLOCKED]", sanitized)
        return sanitized

    def get_stats(self) -> dict:
        """Get firewall statistics."""
        total = len(self.audit_log)
        blocked = sum(1 for e in self.audit_log if e.action_taken == Action.BLOCK)
        flagged = sum(1 for e in self.audit_log if e.action_taken == Action.FLAG)

        return {
            "total_inspections": total,
            "blocked": blocked,
            "flagged": flagged,
            "allowed": total - blocked - flagged,
            "block_rate": f"{(blocked / total * 100):.1f}%" if total else "0%",
            "active_rules": len([r for r in self.rules if r.enabled]),
        }
