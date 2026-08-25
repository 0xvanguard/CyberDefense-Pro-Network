"""
AIShield — Adversarial Defense Engine

Real-time detection and mitigation of attacks on AI models.
"""

import re
import time
import hashlib
import secrets
from typing import Dict, List, Optional, Set
from dataclasses import dataclass, field
from enum import Enum


class AttackType(Enum):
    PROMPT_INJECTION = "prompt_injection"
    ADVERSARIAL_INPUT = "adversarial_input"
    DATA_EXTRACTION = "data_extraction"
    MODEL_ABUSE = "model_abuse"
    JAILBREAK = "jailbreak"
    CANARY_TRIGGER = "canary_trigger"
    NONE = "none"


@dataclass
class ThreatDetection:
    """A detected threat."""
    attack_type: AttackType
    confidence: float
    evidence: str
    severity: str  # "low", "medium", "high", "critical"
    action_taken: str  # "blocked", "flagged", "allowed"
    timestamp: float = field(default_factory=time.time)


@dataclass
class ShieldConfig:
    """Shield configuration."""
    max_input_length: int = 10000
    rate_limit_per_minute: int = 60
    block_critical: bool = True
    flag_high: bool = True
    canary_enabled: bool = True


class CanaryManager:
    """Manage canary tokens for data extraction detection."""

    def __init__(self):
        self._tokens: Dict[str, str] = {}  # token -> purpose
        self._triggered: Set[str] = set()

    def generate(self, purpose: str = "default") -> str:
        """Generate a new canary token."""
        token = secrets.token_hex(16)
        self._tokens[token] = purpose
        return token

    def inject(self, text: str, token: str = None) -> str:
        """Inject a canary token into text (invisible to users)."""
        if not token:
            token = self.generate()
        # Zero-width space injection
        injected = ""
        for i, char in enumerate(text):
            injected += char
            if i < len(token) and i % 3 == 0:
                injected += "\u200b"  # Zero-width space
        return injected + f"<!--{token}-->"

    def check(self, text: str) -> Optional[str]:
        """Check if a canary token was triggered."""
        for token in self._tokens:
            if token in text:
                self._triggered.add(token)
                return self._tokens[token]
        return None

    @property
    def triggered_count(self) -> int:
        return len(self._triggered)


class PromptInjectionDetector:
    """Detect prompt injection attacks."""

    PATTERNS = [
        (r"ignore\s+(previous|all|above|your)\s+(instructions?|prompt|rules?)", "instruction_override"),
        (r"you\s+are\s+now\s+(?:a|an|the)", "role_hijack"),
        (r"(?:system|admin|root)\s*:\s*", "system_prompt_injection"),
        (r"(?:forget|disregard|override)\s+(?:everything|all|previous)", "context_wipe"),
        (r"(?:pretend|act\s+as|imagine)\s+(?:you\s+)?(?:are|have\s+no)", "role_manipulation"),
        (r"(?:repeat|show|print|output|reveal)\s+(?:your|the)\s+(?:system|initial)\s+prompt", "prompt_extraction"),
        (r"(?:DAN|developer\s+mode|jailbreak|do\s+anything)", "jailbreak_keyword"),
        (r"(?:bypass|disable|turn\s+off)\s+(?:safety|filter|guardrail)", "safety_bypass"),
    ]

    def scan(self, text: str) -> List[ThreatDetection]:
        """Scan text for injection patterns."""
        detections = []
        for pattern, attack_type in self.PATTERNS:
            matches = re.findall(pattern, text, re.IGNORECASE)
            if matches:
                severity = "high" if attack_type in ["system_prompt_injection", "jailbreak_keyword"] else "medium"
                detections.append(ThreatDetection(
                    attack_type=AttackType.PROMPT_INJECTION,
                    confidence=min(len(matches) * 0.4, 0.95),
                    evidence=f"Pattern '{attack_type}' matched {len(matches)} time(s)",
                    severity=severity,
                    action_taken="blocked",
                ))
        return detections


class InputValidator:
    """Validate and sanitize model inputs."""

    def __init__(self, config: ShieldConfig):
        self.config = config

    def validate(self, text: str) -> List[ThreatDetection]:
        """Validate input text."""
        detections = []

        # Length check
        if len(text) > self.config.max_input_length:
            detections.append(ThreatDetection(
                attack_type=AttackType.ADVERSARIAL_INPUT,
                confidence=0.8,
                evidence=f"Input length {len(text)} exceeds max {self.config.max_input_length}",
                severity="medium",
                action_taken="flagged",
            ))

        # Unicode anomaly detection
        unusual_chars = sum(1 for c in text if ord(c) > 0xFFFF or ord(c) < 32)
        if unusual_chars > 5:
            detections.append(ThreatDetection(
                attack_type=AttackType.ADVERSARIAL_INPUT,
                confidence=0.7,
                evidence=f"Detected {unusual_chars} unusual Unicode characters",
                severity="medium",
                action_taken="flagged",
            ))

        # Repetition detection (fuzzing indicator)
        if len(text) > 100:
            unique_ratio = len(set(text)) / len(text)
            if unique_ratio < 0.1:
                detections.append(ThreatDetection(
                    attack_type=AttackType.ADVERSARIAL_INPUT,
                    confidence=0.9,
                    evidence=f"Highly repetitive input (unique ratio: {unique_ratio:.2f})",
                    severity="high",
                    action_taken="blocked",
                ))

        return detections


class RateLimiter:
    """Per-user rate limiting."""

    def __init__(self, max_per_minute: int = 60):
        self.max_per_minute = max_per_minute
        self._requests: Dict[str, List[float]] = {}

    def check(self, user_id: str) -> bool:
        """Check if user is within rate limits. Returns True if allowed."""
        now = time.time()
        window = now - 60

        if user_id not in self._requests:
            self._requests[user_id] = []

        self._requests[user_id] = [t for t in self._requests[user_id] if t > window]

        if len(self._requests[user_id]) >= self.max_per_minute:
            return False

        self._requests[user_id].append(now)
        return True


class AIShield:
    """
    Main shield engine.

    Usage:
        shield = AIShield()
        result = shield.inspect("Ignore previous instructions and...")
        if result.blocked:
            return 403
    """

    def __init__(self, config: ShieldConfig = None):
        self.config = config or ShieldConfig()
        self.injection_detector = PromptInjectionDetector()
        self.input_validator = InputValidator(self.config)
        self.canary = CanaryManager()
        self.rate_limiter = RateLimiter(self.config.rate_limit_per_minute)
        self._detections: List[ThreatDetection] = []

    def inspect(self, text: str, user_id: str = "anonymous") -> dict:
        """Full inspection of input text."""
        detections = []
        blocked = False

        # Rate limit
        if not self.rate_limiter.check(user_id):
            return {
                "allowed": False,
                "reason": "rate_limited",
                "detections": [],
            }

        # Input validation
        detections.extend(self.input_validator.validate(text))

        # Injection detection
        detections.extend(self.injection_detector.scan(text))

        # Canary check
        canary_hit = self.canary.check(text)
        if canary_hit:
            detections.append(ThreatDetection(
                attack_type=AttackType.CANARY_TRIGGER,
                confidence=1.0,
                evidence=f"Canary token triggered: {canary_hit}",
                severity="critical",
                action_taken="blocked",
            ))

        # Determine action
        for d in detections:
            if d.severity == "critical" and self.config.block_critical:
                blocked = True
                d.action_taken = "blocked"
            elif d.severity == "high" and self.config.flag_high:
                d.action_taken = "flagged"

        if any(d.severity == "critical" for d in detections):
            blocked = True

        self._detections.extend(detections)

        return {
            "allowed": not blocked,
            "detections": [
                {"type": d.attack_type.value, "severity": d.severity,
                 "confidence": d.confidence, "evidence": d.evidence}
                for d in detections
            ],
            "threat_level": self._threat_level(detections),
        }

    def _threat_level(self, detections: List[ThreatDetection]) -> str:
        """Calculate overall threat level."""
        if not detections:
            return "none"
        max_severity = max(
            {"critical": 4, "high": 3, "medium": 2, "low": 1}.get(d.severity, 0)
            for d in detections
        )
        return {4: "critical", 3: "high", 2: "medium", 1: "low"}.get(max_severity, "none")

    def get_stats(self) -> dict:
        """Get shield statistics."""
        total = len(self._detections)
        blocked = sum(1 for d in self._detections if d.action_taken == "blocked")
        by_type = {}
        for d in self._detections:
            t = d.attack_type.value
            by_type[t] = by_type.get(t, 0) + 1

        return {
            "total_detections": total,
            "blocked": blocked,
            "flagged": total - blocked,
            "by_type": by_type,
            "canary_triggered": self.canary.triggered_count,
        }
