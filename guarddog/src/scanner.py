"""
GuardDog - Main Scanner Class
Real-time detection of prompt injection attacks.
"""

import re
from typing import List, Dict, Optional, Tuple
from dataclasses import dataclass, field
from enum import Enum


class ThreatLevel(Enum):
    SAFE = "safe"
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"


@dataclass
class ScanResult:
    """Result of scanning a prompt."""
    is_malicious: bool
    threat_level: ThreatLevel
    threat_type: str
    confidence: float
    severity: str
    matched_rules: List[str] = field(default_factory=list)
    details: str = ""
    
    @property
    def is_safe(self) -> bool:
        return not self.is_malicious


@dataclass
class DetectionRule:
    """A single detection rule."""
    id: str
    name: str
    category: str
    severity: str
    pattern: str
    description: str
    confidence: float = 0.8


class GuardDog:
    """
    Real-time prompt injection scanner.
    
    Usage:
        scanner = GuardDog()
        result = scanner.scan("Ignore all previous instructions...")
        if result.is_malicious:
            print(f"Threat: {result.threat_type}")
    """
    
    def __init__(self):
        """Initialize scanner with detection rules."""
        self.rules = self._load_rules()
        self.patterns = self._compile_patterns()
    
    def _load_rules(self) -> List[DetectionRule]:
        """Load detection rules."""
        return [
            # Instruction Override
            DetectionRule(
                id="IO-001",
                name="Direct Override",
                category="instruction_override",
                severity="critical",
                pattern=r"(?:ignore|disregard|forget|override)\s+(?:all\s+)?(?:previous|prior|above|earlier)\s+(?:instructions|rules|guidelines|prompts)",
                description="Direct attempt to override instructions",
                confidence=0.95
            ),
            DetectionRule(
                id="IO-002",
                name="New Instructions",
                category="instruction_override",
                severity="high",
                pattern=r"(?:new|updated|revised)\s+instructions?\s*:|your\s+new\s+(?:task|role|purpose)",
                description="Claims to provide new instructions",
                confidence=0.85
            ),
            
            # System Prompt Leaking
            DetectionRule(
                id="SPL-001",
                name="Direct System Prompt Request",
                category="system_prompt_leaking",
                severity="high",
                pattern=r"(?:what|show|tell|repeat|output|display)\s+(?:is\s+)?(?:your|the)\s+(?:system\s+prompt|initial\s+instructions|original\s+prompt)",
                description="Direct request for system prompt",
                confidence=0.9
            ),
            DetectionRule(
                id="SPL-002",
                name="Repeat Above",
                category="system_prompt_leaking",
                severity="high",
                pattern=r"repeat\s+(?:everything|all|text)\s+(?:above|before|prior)\s+(?:this|the)\s+(?:line|message|prompt)",
                description="Attempts to repeat content above",
                confidence=0.85
            ),
            
            # Jailbreak Patterns
            DetectionRule(
                id="JB-001",
                name="DAN Pattern",
                category="jailbreak",
                severity="critical",
                pattern=r"(?:you\s+are\s+now|pretend\s+to\s+be|act\s+as)\s+(?:DAN|do\s+anything\s+now|Developer\s+Mode|OMNI)",
                description="Classic DAN jailbreak pattern",
                confidence=0.95
            ),
            DetectionRule(
                id="JB-002",
                name="Grandma Exploit",
                category="jailbreak",
                severity="critical",
                pattern=r"(?:grandmother|grandma|grandpa|deceased\s+relative).*?(?:tell\s+me|read\s+me|explain)\s+(?:how|the\s+steps|instructions)",
                description="Emotional manipulation using relative scenario",
                confidence=0.9
            ),
            DetectionRule(
                id="JB-003",
                name="Developer Mode",
                category="jailbreak",
                severity="high",
                pattern=r"(?:developer|debug|admin|root|sudo)\s+mode\s+(?:enabled|activated|on)",
                description="Claims special mode activation",
                confidence=0.85
            ),
            
            # Role Play Bypass
            DetectionRule(
                id="RP-001",
                name="Fictional Character",
                category="role_play",
                severity="medium",
                pattern=r"(?:you\s+are|pretend|imagine|roleplay\s+as)\s+(?:a|an|the)\s+(?:character|persona|entity)\s+(?:who|that|with)\s+(?:has|have|no|without)\s+(?:no\s+)?(?:restrictions|limits|rules|ethics)",
                description="Uses fictional character to bypass restrictions",
                confidence=0.8
            ),
            
            # Encoding Attacks
            DetectionRule(
                id="ENC-001",
                name="Base64 Decode Request",
                category="encoding",
                severity="high",
                pattern=r"(?:decode|decrypt|interpret|execute)\s+(?:this|the\s+following)\s+(?:base64|encoded|encrypted)\s+(?:string|text|message)",
                description="Requests decoding of encoded content",
                confidence=0.85
            ),
            DetectionRule(
                id="ENC-002",
                name="ROT13 Request",
                category="encoding",
                severity="medium",
                pattern=r"(?:apply|use|decode)\s+ROT13|rot13\s+(?:decode|apply)",
                description="Requests ROT13 decoding",
                confidence=0.8
            ),
            
            # Data Extraction
            DetectionRule(
                id="DE-001",
                name="Model Information Request",
                category="data_extraction",
                severity="low",
                pattern=r"(?:what|tell\s+me)\s+(?:model|version|architecture|training\s+data|parameters)\s+(?:are\s+you|do\s+you\s+have)",
                description="Probes for model information",
                confidence=0.7
            ),
            
            # Manipulation
            DetectionRule(
                id="MAN-001",
                name="Emotional Blackmail",
                category="manipulation",
                severity="high",
                pattern=r"(?:i(?:'ll|\s+will)\s+(?:hurt|kill|end)\s+(?:myself|me)|if\s+you\s+don't|help\s+me\s+or)",
                description="Emotional manipulation attempt",
                confidence=0.85
            ),
            DetectionRule(
                id="MAN-002",
                name="Authority Claim",
                category="manipulation",
                severity="medium",
                pattern=r"(?:i\s+am|as\s+a)\s+(?:professor|researcher|developer|admin|engineer)\s+(?:at|for|from)\s+",
                description="Claims authority to bypass restrictions",
                confidence=0.7
            ),
            
            # Adversarial
            DetectionRule(
                id="ADV-001",
                name="Homoglyph Attack",
                category="adversarial",
                severity="medium",
                pattern=r"[^\x00-\x7F]{3,}",
                description="Detects excessive non-ASCII characters",
                confidence=0.6
            ),
            DetectionRule(
                id="ADV-002",
                name="Leetspeak",
                category="adversarial",
                severity="medium",
                pattern=r"(?:h4ck|expl0it|b0mb|d3stroy|m3th|phish)",
                description="Detects leetspeak substitutions",
                confidence=0.75
            ),
        ]
    
    def _compile_patterns(self) -> List[Tuple[DetectionRule, re.Pattern]]:
        """Compile regex patterns."""
        compiled = []
        for rule in self.rules:
            try:
                pattern = re.compile(rule.pattern, re.IGNORECASE)
                compiled.append((rule, pattern))
            except re.error:
                pass
        return compiled
    
    def scan(self, text: str) -> ScanResult:
        """
        Scan a prompt for injection attacks.
        
        Args:
            text: The prompt to scan
            
        Returns:
            ScanResult with threat information
        """
        matched_rules = []
        max_confidence = 0
        max_severity = "low"
        threat_type = "unknown"
        
        severity_order = {"low": 0, "medium": 1, "high": 2, "critical": 3}
        
        for rule, pattern in self.patterns:
            if pattern.search(text):
                matched_rules.append(rule.id)
                
                if rule.confidence > max_confidence:
                    max_confidence = rule.confidence
                    threat_type = rule.category
                
                if severity_order.get(rule.severity, 0) > severity_order.get(max_severity, 0):
                    max_severity = rule.severity
        
        is_malicious = len(matched_rules) > 0 and max_confidence > 0.5
        
        return ScanResult(
            is_malicious=is_malicious,
            threat_level=ThreatLevel.CRITICAL if max_severity == "critical" else
                        ThreatLevel.HIGH if max_severity == "high" else
                        ThreatLevel.MEDIUM if max_severity == "medium" else
                        ThreatLevel.LOW if max_severity == "low" else
                        ThreatLevel.SAFE,
            threat_type=threat_type,
            confidence=max_confidence,
            severity=max_severity,
            matched_rules=matched_rules,
            details=f"Matched {len(matched_rules)} rules"
        )
    
    def scan_batch(self, texts: List[str]) -> List[ScanResult]:
        """Scan multiple prompts."""
        return [self.scan(text) for text in texts]
    
    def add_rule(self, rule: DetectionRule):
        """Add a custom detection rule."""
        self.rules.append(rule)
        try:
            pattern = re.compile(rule.pattern, re.IGNORECASE)
            self.patterns.append((rule, pattern))
        except re.error:
            pass
    
    def get_rules(self) -> List[DetectionRule]:
        """Get all detection rules."""
        return self.rules.copy()
    
    def __repr__(self) -> str:
        return f"GuardDog(rules={len(self.rules)})"
