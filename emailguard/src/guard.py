"""EmailGuard — Email Security Filter"""
import re
from dataclasses import dataclass, field
from typing import List, Dict, Optional

@dataclass
class SpamFilter:
    score: float
    is_spam: bool
    reasons: List[str]

@dataclass
class ThreatDetection:
    threat_type: str
    severity: str
    description: str

class EmailGuard:
    def __init__(self):
        self.spam_words = ["free", "winner", "click here", "act now", "limited time", "congratulations"]
        self.blocked_domains = ["malware.com", "phishing.net", "spam.org"]
        self.scan_count = 0
        self.spam_count = 0

    def check_spam(self, subject: str, body: str) -> SpamFilter:
        text = (subject + " " + body).lower()
        score = 0.0
        reasons = []
        for word in self.spam_words:
            if word in text:
                score += 0.15
                reasons.append(f"Contains spam word: '{word}'")
        if len(body) > 5000:
            score += 0.1
            reasons.append("Unusually long body")
        exclamation = text.count("!")
        if exclamation > 5:
            score += 0.1
            reasons.append(f"Excessive exclamation marks ({exclamation})")
        caps_ratio = sum(1 for c in subject if c.isupper()) / max(len(subject), 1)
        if caps_ratio > 0.5:
            score += 0.15
            reasons.append("Excessive capitalization in subject")
        score = min(score, 1.0)
        self.scan_count += 1
        if score > 0.5:
            self.spam_count += 1
        return SpamFilter(score=score, is_spam=score > 0.5, reasons=reasons)

    def detect_threats(self, headers: Dict[str, str], body: str) -> List[ThreatDetection]:
        threats = []
        auth = headers.get("authentication-results", "").lower()
        if "spf=fail" in auth:
            threats.append(ThreatDetection("spoofing", "high", "SPF check failed"))
        if "dkim=fail" in auth:
            threats.append(ThreatDetection("spoofing", "high", "DKIM check failed"))
        if "dmarc=fail" in auth:
            threats.append(ThreatDetection("spoofing", "critical", "DMARC check failed"))
        if re.search(r'<form[^>]*action', body, re.IGNORECASE):
            threats.append(ThreatDetection("phishing", "high", "Contains HTML form"))
        if re.search(r'(click here|verify your|confirm your|update your)', body.lower()):
            threats.append(ThreatDetection("phishing", "medium", "Possible phishing language"))
        return threats

    def get_statistics(self) -> Dict:
        return {"scans": self.scan_count, "spam_found": self.spam_count}

    def __repr__(self) -> str:
        return f"EmailGuard(scans={self.scan_count})"
