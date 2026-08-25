"""RiskCalculator - Cybersecurity Risk Calculator"""
from dataclasses import dataclass
from typing import Optional


@dataclass
class CVSSScore:
    """CVSS v3.1 score result."""
    score: float
    severity: str
    vector: str
    exploitability: float
    impact: float


@dataclass
class FAIRAnalysis:
    """FAIR risk analysis result."""
    loss_event_frequency: float
    loss_magnitude: float
    ale: float  # Annual Loss Expectancy
    risk_level: str
    recommendation: str


@dataclass
class RiskMatrix:
    """Risk matrix assessment."""
    likelihood: str
    impact: str
    risk_level: str
    color: str


class RiskCalculator:
    """
    Cybersecurity risk calculator.
    
    Usage:
        rc = RiskCalculator()
        cvss = rc.calculate_cvss(attack_vector="network", ...)
        fair = rc.fair_analysis(loss_event_frequency=10, loss_magnitude=50000)
    """
    
    CVSS_WEIGHTS = {
        "attack_vector": {"network": 0.85, "adjacent": 0.62, "local": 0.55, "physical": 0.20},
        "attack_complexity": {"low": 0.77, "high": 0.44},
        "privileges_required": {"none": 0.85, "low": 0.62, "high": 0.27},
        "user_interaction": {"none": 0.85, "required": 0.62},
        "scope": {"changed": 1.08, "unchanged": 1.0},
        "confidentiality": {"high": 0.56, "low": 0.22, "none": 0.0},
        "integrity": {"high": 0.56, "low": 0.22, "none": 0.0},
        "availability": {"high": 0.56, "low": 0.22, "none": 0.0}
    }
    
    SEVERITY_MAP = {
        (0.0, 0.1): "None",
        (0.1, 4.0): "Low",
        (4.0, 7.0): "Medium",
        (7.0, 9.0): "High",
        (9.0, 10.1): "Critical"
    }
    
    def calculate_cvss(self, attack_vector: str = "network",
                       attack_complexity: str = "low",
                       privileges_required: str = "none",
                       user_interaction: str = "none",
                       scope: str = "unchanged",
                       confidentiality: str = "low",
                       integrity: str = "low",
                       availability: str = "low") -> CVSSScore:
        """Calculate CVSS v3.1 score."""
        # Exploitability
        av = self.CVSS_WEIGHTS["attack_vector"][attack_vector]
        ac = self.CVSS_WEIGHTS["attack_complexity"][attack_complexity]
        pr = self.CVSS_WEIGHTS["privileges_required"][privileges_required]
        ui = self.CVSS_WEIGHTS["user_interaction"][user_interaction]
        
        exploitability = 8.22 * av * ac * pr * ui
        
        # Impact
        c = self.CVSS_WEIGHTS["confidentiality"][confidentiality]
        i = self.CVSS_WEIGHTS["integrity"][integrity]
        a = self.CVSS_WEIGHTS["availability"][availability]
        
        isc_base = 1 - ((1 - c) * (1 - i) * (1 - a))
        
        if scope == "changed":
            impact = 7.52 * (isc_base - 0.029) - 3.25 * ((isc_base - 0.02) ** 15)
        else:
            impact = 6.42 * isc_base
        
        # Round up to nearest 0.1
        import math
        if impact <= 0:
            score = 0.0
        else:
            score = math.ceil(min((exploitability + impact) * 10, 100)) / 10
        
        # Determine severity
        severity = "None"
        for (low, high), sev in self.SEVERITY_MAP.items():
            if low <= score < high:
                severity = sev
                break
        
        vector = f"CVSS:3.1/AV:{attack_vector[0].upper()}/AC:{attack_complexity[0].upper()}/PR:{privileges_required[0].upper()}/UI:{user_interaction[0].upper()}/S:{scope[0].upper()}/C:{confidentiality[0].upper()}/I:{integrity[0].upper()}/A:{availability[0].upper()}"
        
        return CVSSScore(
            score=score,
            severity=severity,
            vector=vector,
            exploitability=round(exploitability, 2),
            impact=round(max(impact, 0), 2)
        )
    
    def fair_analysis(self, loss_event_frequency: float,
                      loss_magnitude: float) -> FAIRAnalysis:
        """Perform FAIR risk analysis."""
        ale = loss_event_frequency * loss_magnitude
        
        if ale > 1000000:
            risk_level = "CRITICAL"
            recommendation = "Immediate action required. Consider risk transfer or avoidance."
        elif ale > 100000:
            risk_level = "HIGH"
            recommendation = "Priority mitigation needed. Implement controls."
        elif ale > 10000:
            risk_level = "MEDIUM"
            recommendation = "Monitor and implement basic controls."
        else:
            risk_level = "LOW"
            recommendation = "Accept risk or implement cost-effective controls."
        
        return FAIRAnalysis(
            loss_event_frequency=loss_event_frequency,
            loss_magnitude=loss_magnitude,
            ale=ale,
            risk_level=risk_level,
            recommendation=recommendation
        )
    
    def risk_matrix(self, likelihood: str, impact: str) -> RiskMatrix:
        """Assess risk using likelihood/impact matrix."""
        matrix = {
            ("low", "low"): ("Low", "#22c55e"),
            ("low", "medium"): ("Low", "#22c55e"),
            ("low", "high"): ("Medium", "#f59e0b"),
            ("low", "critical"): ("Medium", "#f59e0b"),
            ("medium", "low"): ("Low", "#22c55e"),
            ("medium", "medium"): ("Medium", "#f59e0b"),
            ("medium", "high"): ("High", "#ef4444"),
            ("medium", "critical"): ("Critical", "#dc2626"),
            ("high", "low"): ("Medium", "#f59e0b"),
            ("high", "medium"): ("High", "#ef4444"),
            ("high", "high"): ("Critical", "#dc2626"),
            ("high", "critical"): ("Critical", "#dc2626"),
        }
        
        risk_level, color = matrix.get((likelihood.lower(), impact.lower()), ("Unknown", "#6b7280"))
        
        return RiskMatrix(
            likelihood=likelihood,
            impact=impact,
            risk_level=risk_level,
            color=color
        )
    
    def __repr__(self) -> str:
        return "RiskCalculator()"
