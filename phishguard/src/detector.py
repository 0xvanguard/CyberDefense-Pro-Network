"""
PhishGuard — Phishing Detection Engine

Analyzes URLs, emails, and messages for phishing indicators.
"""

import re
import time
import hashlib
from typing import Dict, List, Optional
from dataclasses import dataclass, field
from urllib.parse import urlparse
from enum import Enum


class Verdict(Enum):
    LEGITIMATE = "legitimate"
    SUSPICIOUS = "suspicious"
    PHISHING = "phishing"
    UNKNOWN = "unknown"


@dataclass
class Signal:
    """A detected phishing signal."""
    name: str
    weight: float
    description: str
    evidence: str = ""


@dataclass
class AnalysisResult:
    """Result of phishing analysis."""
    target: str
    verdict: Verdict
    confidence: float
    signals: List[Signal]
    risk_score: float
    recommendations: List[str]
    analysis_time_ms: float = 0

    def to_dict(self) -> dict:
        return {
            "target": self.target,
            "verdict": self.verdict.value,
            "confidence": round(self.confidence, 2),
            "risk_score": round(self.risk_score, 2),
            "signals": [{"name": s.name, "weight": s.weight, "evidence": s.evidence} for s in self.signals],
            "recommendations": self.recommendations,
        }


class URLAnalyzer:
    """Analyze URLs for phishing indicators."""

    SUSPICIOUS_TLDS = [
        ".xyz", ".top", ".club", ".work", ".click", ".link",
        ".info", ".buzz", ".gq", ".ml", ".tk", ".cf",
    ]

    SUSPICIOUS_KEYWORDS = [
        "login", "verify", "secure", "account", "update",
        "confirm", "password", "banking", "paypal", "amazon",
        "microsoft", "apple", "netflix", "facebook", "google",
    ]

    BRAND_KEYWORDS = [
        "paypal", "amazon", "microsoft", "apple", "netflix",
        "facebook", "google", "instagram", "twitter", "linkedin",
        "bank", "chase", "wellsfargo", "citibank", "boa",
    ]

    def analyze(self, url: str) -> List[Signal]:
        """Analyze a URL and return signals."""
        signals = []

        try:
            parsed = urlparse(url)
        except Exception:
            return [Signal("invalid-url", 0.5, "URL could not be parsed")]

        domain = parsed.netloc.lower()
        path = parsed.path.lower()

        # Check TLD
        for tld in self.SUSPICIOUS_TLDS:
            if domain.endswith(tld):
                signals.append(Signal(
                    "suspicious-tld", 0.3,
                    f"Uses suspicious TLD: {tld}",
                    f"Domain: {domain}",
                ))
                break

        # Check for brand impersonation
        for brand in self.BRAND_KEYWORDS:
            if brand in domain and f"{brand}.com" not in domain:
                signals.append(Signal(
                    "brand-impersonation", 0.4,
                    f"Possible impersonation of {brand}",
                    f"Domain contains '{brand}' but is not {brand}.com",
                ))
                break

        # Check for IP address
        ip_pattern = r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"
        if re.match(ip_pattern, domain):
            signals.append(Signal(
                "ip-address", 0.35,
                "Domain is an IP address",
                f"IP: {domain}",
            ))

        # Check for suspicious keywords in path
        for keyword in self.SUSPICIOUS_KEYWORDS:
            if keyword in path:
                signals.append(Signal(
                    "suspicious-path", 0.2,
                    f"Path contains suspicious keyword: {keyword}",
                    f"Path: {path}",
                ))
                break

        # Check for URL shorteners
        shorteners = ["bit.ly", "tinyurl.com", "goo.gl", "t.co", "ow.ly"]
        if any(s in domain for s in shorteners):
            signals.append(Signal(
                "url-shortener", 0.15,
                "URL uses a shortener service",
                f"Shortener: {domain}",
            ))

        # Check for multiple subdomains
        subdomain_count = domain.count(".")
        if subdomain_count > 3:
            signals.append(Signal(
                "excessive-subdomains", 0.2,
                f"Excessive subdomains ({subdomain_count})",
                f"Domain: {domain}",
            ))

        # Check for HTTP (no SSL)
        if parsed.scheme == "http":
            signals.append(Signal(
                "no-ssl", 0.25,
                "URL uses HTTP instead of HTTPS",
                f"Scheme: {parsed.scheme}",
            ))

        # Check for encoded characters
        if "%" in url:
            signals.append(Signal(
                "encoded-chars", 0.15,
                "URL contains encoded characters",
                f"URL: {url[:100]}",
            ))

        return signals


class EmailAnalyzer:
    """Analyze email headers and content for phishing."""

    URGENCY_WORDS = [
        "urgent", "immediately", "act now", "expires", "suspended",
        "verify", "confirm", "unauthorized", "unusual activity",
        "limited time", "last chance", "failure to", "will be closed",
    ]

    CREDENTIAL_WORDS = [
        "password", "ssn", "social security", "credit card",
        "bank account", "login credentials", "verify your identity",
    ]

    def analyze_headers(self, headers: Dict[str, str]) -> List[Signal]:
        """Analyze email headers."""
        signals = []

        # Check SPF
        auth_results = headers.get("authentication-results", "").lower()
        if "spf=fail" in auth_results:
            signals.append(Signal(
                "spf-fail", 0.3,
                "SPF check failed",
                "Sender IP not authorized for this domain",
            ))

        # Check DKIM
        if "dkim=fail" in auth_results:
            signals.append(Signal(
                "dkim-fail", 0.3,
                "DKIM check failed",
                "Email signature verification failed",
            ))

        # Check DMARC
        if "dmarc=fail" in auth_results:
            signals.append(Signal(
                "dmarc-fail", 0.35,
                "DMARC check failed",
                "Domain policy check failed",
            ))

        # Check for display name spoofing
        from_header = headers.get("from", "")
        if " <" in from_header:
            display_name = from_header.split(" <")[0].strip()
            email = from_header.split("<")[1].rstrip(">")
            if display_name and email:
                name_domain = display_name.lower().replace(" ", "")
                email_domain = email.split("@")[-1] if "@" in email else ""
                if email_domain and name_domain != email_domain.replace(".", ""):
                    signals.append(Signal(
                        "display-name-spoof", 0.25,
                        "Display name doesn't match email domain",
                        f"From: {from_header}",
                    ))

        # Check Reply-To mismatch
        reply_to = headers.get("reply-to", "")
        if reply_to and reply_to != headers.get("from", ""):
            signals.append(Signal(
                "reply-to-mismatch", 0.2,
                "Reply-To differs from From address",
                f"From: {headers.get('from', '')}, Reply-To: {reply_to}",
            ))

        return signals

    def analyze_content(self, text: str) -> List[Signal]:
        """Analyze email body text."""
        signals = []
        text_lower = text.lower()

        # Urgency detection
        urgency_count = sum(1 for w in self.URGENCY_WORDS if w in text_lower)
        if urgency_count >= 3:
            signals.append(Signal(
                "high-urgency", 0.3,
                f"Multiple urgency words detected ({urgency_count})",
                f"Words found: {', '.join(w for w in self.URGENCY_WORDS if w in text_lower)}",
            ))

        # Credential harvesting
        credential_count = sum(1 for w in self.CREDENTIAL_WORDS if w in text_lower)
        if credential_count >= 2:
            signals.append(Signal(
                "credential-request", 0.35,
                "Requesting sensitive credentials",
                f"Found {credential_count} credential-related terms",
            ))

        # Check for HTML forms
        if "<form" in text.lower():
            signals.append(Signal(
                "html-form", 0.2,
                "Contains HTML form",
                "Forms in emails are often used for credential harvesting",
            ))

        return signals


class PhishDetector:
    """
    Main phishing detection engine.

    Usage:
        detector = PhishDetector()
        result = detector.analyze_url("https://suspicious-site.com")
    """

    def __init__(self):
        self.url_analyzer = URLAnalyzer()
        self.email_analyzer = EmailAnalyzer()

    def analyze_url(self, url: str) -> AnalysisResult:
        """Analyze a URL for phishing."""
        start = time.time()

        signals = self.url_analyzer.analyze(url)
        risk_score = self._calculate_risk(signals)
        verdict = self._verdict_from_score(risk_score)
        confidence = min(0.5 + risk_score * 0.5, 0.99)
        recommendations = self._generate_recommendations(signals, verdict)

        return AnalysisResult(
            target=url,
            verdict=verdict,
            confidence=confidence,
            signals=signals,
            risk_score=risk_score,
            recommendations=recommendations,
            analysis_time_ms=(time.time() - start) * 1000,
        )

    def analyze_email(self, headers: Dict[str, str], body: str) -> AnalysisResult:
        """Analyze an email for phishing."""
        start = time.time()

        signals = []
        signals.extend(self.email_analyzer.analyze_headers(headers))
        signals.extend(self.email_analyzer.analyze_content(body))

        risk_score = self._calculate_risk(signals)
        verdict = self._verdict_from_score(risk_score)
        confidence = min(0.5 + risk_score * 0.5, 0.99)
        recommendations = self._generate_recommendations(signals, verdict)

        from_header = headers.get("from", "unknown")

        return AnalysisResult(
            target=from_header,
            verdict=verdict,
            confidence=confidence,
            signals=signals,
            risk_score=risk_score,
            recommendations=recommendations,
            analysis_time_ms=(time.time() - start) * 1000,
        )

    def _calculate_risk(self, signals: List[Signal]) -> float:
        """Calculate risk score from signals."""
        if not signals:
            return 0.0
        return min(sum(s.weight for s in signals), 1.0)

    def _verdict_from_score(self, score: float) -> Verdict:
        """Convert risk score to verdict."""
        if score >= 0.7:
            return Verdict.PHISHING
        elif score >= 0.3:
            return Verdict.SUSPICIOUS
        else:
            return Verdict.LEGITIMATE

    def _generate_recommendations(self, signals: List[Signal], verdict: Verdict) -> List[str]:
        """Generate recommendations based on findings."""
        recs = []
        signal_names = {s.name for s in signals}

        if verdict == Verdict.PHISHING:
            recs.append("🚫 Do not click any links or provide credentials")
            recs.append("📧 Report this as phishing to your email provider")

        if "brand-impersonation" in signal_names:
            recs.append("🔍 Verify the domain is the official brand website")

        if "no-ssl" in signal_names:
            recs.append("🔒 Site does not use HTTPS — avoid entering sensitive data")

        if "spf-fail" in signal_names or "dkim-fail" in signal_names:
            recs.append("✉️ Email authentication failed — likely spoofed sender")

        if "credential-request" in signal_names:
            recs.append("🔐 Legitimate companies rarely ask for credentials via email")

        if "high-urgency" in signal_names:
            recs.append("⏰ Urgency is a common phishing tactic — take your time")

        if not recs:
            recs.append("✅ No major issues detected")

        return recs
