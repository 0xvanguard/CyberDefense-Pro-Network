"""GuardDog — Real-Time Prompt Injection Scanner"""

from .scanner import GuardDog, ScanResult, ThreatLevel, Rule

__version__ = "2.0.0"
__all__ = ["GuardDog", "ScanResult", "ThreatLevel", "Rule"]
