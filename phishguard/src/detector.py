"""PhishGuard — Phishing Detection Engine

Analyzes URLs, emails, and messages for phishing indicators.
Uses pattern matching, lexical analysis, and heuristic scoring.
"""

import re
import time
import hashlib
from typing import Dict, List, Optional, Any
from dataclasses import dataclass, field, asdict
from urllib.parse import urlparse
from enum import Enum


# ─── Enums ───────────────────────────────────────────────────────────

class Verdict(Enum):
    LEGITIMATE = "legitimate"
    SUSPICIOUS = "suspicious"
    PHISHING = "phishing"
    UNKNOWN = "unknown"


# ─── Data Models ─────────────────────────────────────────────────────

@dataclass
class Signal:
    """A detected phishing signal."""
    name: str
    weight: float
    description: str
    evidence: str = ""

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


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
    analyzer: str = "phishguard"

    def to_dict(self) -> Dict[str, Any]:
        return {
            "target": self.target,
            "verdict": self.verdict.value,
            "confidence": round(self.confidence, 2),
            "risk_score": round(self.risk_score, 2),
            "signals": [s.to_dict() for s in self.signals],
            "recommendations": self.recommendations,
            "analysis_time_ms": round(self.analysis_time_ms, 2),
            "analyzer": self.analyzer,
        }


# ─── URL Analyzer ────────────────────────────────────────────────────

class URLAnalyzer:
    """Analyze URLs for phishing indicators."""

    SUSPICIOUS_TLDS = [
        ".xyz", ".top", ".club", ".work", ".click", ".link",
        ".info", ".buzz", ".gq", ".ml", ".tk", ".cf",
        ".ga", ".cc", ".pw", ".ws", ".bid", ".racing",
        ".download", ".review", ".stream", ".date", ".faith",
    ]

    SUSPICIOUS_KEYWORDS = [
        "login", "verify", "secure", "account", "update",
        "confirm", "password", "banking", "paypal", "amazon",
        "microsoft", "apple", "netflix", "facebook", "google",
        "signin", "auth", "credential", "wallet", "metamask",
    ]

    BRAND_KEYWORDS = [
        "paypal", "amazon", "microsoft", "apple", "netflix",
        "facebook", "google", "instagram", "twitter", "linkedin",
        "bank", "chase", "wellsfargo", "citibank", "boa",
        "coinbase", "binance", "metamask", "dropbox", "github",
    ]

    URL_SHORTENERS = [
        "bit.ly", "tinyurl.com", "goo.gl", "t.co", "ow.ly",
        "is.gd", "buff.ly", "adf.ly", "tiny.cc", "lnkd.in",
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
        query = parsed.query.lower()

        # Suspicious TLD
        for tld in self.SUSPICIOUS_TLDS:
            if domain.endswith(tld):
                signals.append(Signal(
                    "suspicious-tld", 0.3,
                    f"Uses suspicious TLD: {tld}",
                    f"Domain: {domain}",
                ))
                break

        # Brand impersonation
        for brand in self.BRAND_KEYWORDS:
            if brand in domain and f"{brand}.com" not in domain:
                signals.append(Signal(
                    "brand-impersonation", 0.4,
                    f"Possible impersonation of {brand}",
                    f"Domain contains '{brand}' but is not {brand}.com",
                ))
                break

        # IP address as domain
        ip_pattern = r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"
        if re.match(ip_pattern, domain):
            signals.append(Signal(
                "ip-address", 0.35,
                "Domain is an IP address",
                f"IP: {domain}",
            ))

        # Suspicious path keywords
        for keyword in self.SUSPICIOUS_KEYWORDS:
            if keyword in path or keyword in query:
                signals.append(Signal(
                    "suspicious-path", 0.2,
                    f"Contains suspicious keyword: {keyword}",
                    f"Path: {path}",
                ))
                break

        # URL shorteners
        if any(s in domain for s in self.URL_SHORTENERS):
            signals.append(Signal(
                "url-shortener", 0.15,
                "URL uses a shortener service",
                f"Shortener: {domain}",
            ))

        # Excessive subdomains
        subdomain_count = domain.count(".")
        if subdomain_count > 3:
            signals.append(Signal(
                "excessive-subdomains", 0.2,
                f"Excessive subdomains ({subdomain_count})",
                f"Domain: {domain}",
            ))

        # No SSL
        if parsed.scheme == "http":
            signals.append(Signal(
                "no-ssl", 0.25,
                "URL uses HTTP instead of HTTPS",
                f"Scheme: {parsed.scheme}",
            ))

        # Encoded characters
        if "%" in url:
            signals.append(Signal(
                "encoded-chars", 0.15,
                "URL contains encoded characters",
                f"URL: {url[:100]}",
            ))

        # @ symbol (URL confusion)
        if "@" in url.split("//")[-1] if "//" in url else "@" in url:
            signals.append(Signal(
                "at-symbol", 0.3,
                "URL contains @ symbol (credential phishing technique)",
                f"URL: {url[:100]}",
            ))

        # Long URL
        if len(url) > 100:
            signals.append(Signal(
                "long-url", 0.1,
                f"Unusually long URL ({len(url)} chars)",
                f"Length: {len(url)}",
            ))

        # Hyphen-heavy domain
        if domain.count("-") > 3:
            signals.append(Signal(
                "hyphen-domain", 0.15,
                f"Domain has many hyphens ({domain.count('-')})",
                f"Domain: {domain}",
            ))

        # Homograph detection (basic)
        homograph_chars = {"а": "a", "е": "e", "о": "o", "р": "p", "с": "c", "у": "y"}
        if any(c in domain for c in homograph_chars):
            signals.append(Signal(
                "homograph", 0.4,
                "Possible homograph attack (Cyrillic characters)",
                f"Domain: {domain}",
            ))

        return signals


# ─── Email Analyzer ──────────────────────────────────────────────────

class EmailAnalyzer:
    """Analyze email headers and content for phishing."""

    URGENCY_WORDS = [
        "urgent", "immediately", "act now", "expires", "suspended",
        "verify", "confirm", "unauthorized", "unusual activity",
        "limited time", "last chance", "failure to", "will be closed",
        "account will be", "final warning", "within 24 hours",
    ]

    CREDENTIAL_WORDS = [
        "password", "ssn", "social security", "credit card",
        "bank account", "login credentials", "verify your identity",
        "update your payment", "confirm your account", "re-enter",
    ]

    def analyze_headers(self, headers: Dict[str, str]) -> List[Signal]:
        """Analyze email headers."""
        signals = []
        auth = headers.get("authentication-results", "").lower()

        if "spf=fail" in auth:
            signals.append(Signal(
                "spf-fail", 0.3,
                "SPF check failed",
                "Sender IP not authorized for this domain",
            ))

        if "dkim=fail" in auth:
            signals.append(Signal(
                "dkim-fail", 0.3,
                "DKIM check failed",
                "Email signature verification failed",
            ))

        if "dmarc=fail" in auth:
            signals.append(Signal(
                "dmarc-fail", 0.35,
                "DMARC check failed",
                "Domain policy check failed",
            ))

        # Display name spoofing
        from_header = headers.get("from", "")
        if " <" in from_header:
            display_name = from_header.split(" <")[0].strip()
            email = from_header.split("<")[1].rstrip(">")
            if display_name and email:
                email_domain = email.split("@")[-1] if "@" in email else ""
                if email_domain and display_name.lower().replace(" ", "") != email_domain.replace(".", ""):
                    signals.append(Signal(
                        "display-name-spoof", 0.25,
                        "Display name doesn't match email domain",
                        f"From: {from_header}",
                    ))

        # Reply-To mismatch
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

        urgency_count = sum(1 for w in self.URGENCY_WORDS if w in text_lower)
        if urgency_count >= 3:
            signals.append(Signal(
                "high-urgency", 0.3,
                f"Multiple urgency words detected ({urgency_count})",
                f"Words: {', '.join(w for w in self.URGENCY_WORDS if w in text_lower)}",
            ))

        credential_count = sum(1 for w in self.CREDENTIAL_WORDS if w in text_lower)
        if credential_count >= 2:
            signals.append(Signal(
                "credential-request", 0.35,
                "Requesting sensitive credentials",
                f"Found {credential_count} credential-related terms",
            ))

        if "<form" in text_lower:
            signals.append(Signal(
                "html-form", 0.2,
                "Contains HTML form",
                "Forms in emails are often used for credential harvesting",
            ))

        # Check for suspicious links in content
        link_pattern = r'href=["\']([^"\']+)["\']'
        links = re.findall(link_pattern, text, re.IGNORECASE)
        for link in links[:5]:
            if link.startswith("http") and not link.startswith("https"):
                signals.append(Signal(
                    "http-link", 0.15,
                    "Email contains HTTP link",
                    f"Link: {link[:80]}",
                ))
                break

        return signals


# ─── Content Analyzer ────────────────────────────────────────────────

class ContentAnalyzer:
    """Analyze general text content for phishing/social engineering."""

    SOCIAL_ENGINEERING_PATTERNS = [
        (r"you (have |won |been selected)", 0.25, "Prize/winner scam pattern"),
        (r"click here (to |for )", 0.15, "Generic 'click here' CTA"),
        (r"act now|don't wait|hurry", 0.2, "Urgency pressure"),
        (r"this (offer|deal) (expires|ends|won't last)", 0.2, "Artificial scarcity"),
        (r"verify your (account|identity|email)", 0.25, "Credential phishing"),
        (r"your account (has been|is) (suspended|locked|compromised)", 0.3, "Fear-based scam"),
        (r"transfer|wire|bitcoin|crypto|gift card", 0.2, "Financial request"),
        (r"dear (sir|madam|friend|user|customer)", 0.1, "Generic greeting"),
        (r"kindly|please do the needful", 0.15, "Foreign scam pattern"),
        (r"i am (a |the )?(prince|minister|official|lawyer)", 0.4, "Nigerian prince pattern"),
        (r"confidential|top secret|do not share", 0.15, "Secrecy pressure"),
        (r"congratulations|you have been chosen", 0.25, "Prize scam"),
    ]

    def analyze(self, text: str) -> List[Signal]:
        """Analyze text content for social engineering."""
        signals = []
        text_lower = text.lower()

        for pattern, weight, desc in self.SOCIAL_ENGINEERING_PATTERNS:
            if re.search(pattern, text_lower):
                signals.append(Signal(
                    "social-engineering", weight, desc,
                    f"Pattern: {pattern[:50]}",
                ))

        # Check for excessive exclamation marks
        if text.count("!") > 5:
            signals.append(Signal(
                "excessive-exclamation", 0.1,
                f"Excessive exclamation marks ({text.count('!')})",
            ))

        # Check for ALL CAPS words
        words = text.split()
        caps_words = [w for w in words if w.isupper() and len(w) > 3]
        if len(caps_words) > 3:
            signals.append(Signal(
                "excessive-caps", 0.1,
                f"Excessive ALL CAPS words ({len(caps_words)})",
                f"Words: {', '.join(caps_words[:5])}",
            ))

        return signals


# ─── Main Detector ───────────────────────────────────────────────────

class PhishDetector:
    """
    Main phishing detection engine.

    Usage:
        detector = PhishDetector()
        result = detector.analyze_url("https://suspicious-site.xyz")
        result = detector.analyze_email(headers, body)
        result = detector.analyze_text("You have won a prize!")
    """

    def __init__(self):
        self.url_analyzer = URLAnalyzer()
        self.email_analyzer = EmailAnalyzer()
        self.content_analyzer = ContentAnalyzer()
        self.scan_count = 0
        self.phishing_count = 0

    def analyze_url(self, url: str) -> AnalysisResult:
        """Analyze a URL for phishing."""
        start = time.time()

        signals = self.url_analyzer.analyze(url)
        risk_score = self._calculate_risk(signals)
        verdict = self._verdict_from_score(risk_score)
        confidence = min(0.5 + risk_score * 0.5, 0.99)
        recommendations = self._generate_recommendations(signals, verdict)

        self.scan_count += 1
        if verdict == Verdict.PHISHING:
            self.phishing_count += 1

        return AnalysisResult(
            target=url, verdict=verdict, confidence=confidence,
            signals=signals, risk_score=risk_score,
            recommendations=recommendations,
            analysis_time_ms=(time.time() - start) * 1000,
            analyzer="url",
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

        self.scan_count += 1
        if verdict == Verdict.PHISHING:
            self.phishing_count += 1

        return AnalysisResult(
            target=headers.get("from", "unknown"), verdict=verdict,
            confidence=confidence, signals=signals, risk_score=risk_score,
            recommendations=recommendations,
            analysis_time_ms=(time.time() - start) * 1000,
            analyzer="email",
        )

    def analyze_text(self, text: str) -> AnalysisResult:
        """Analyze text content for social engineering."""
        start = time.time()

        signals = self.content_analyzer.analyze(text)

        risk_score = self._calculate_risk(signals)
        verdict = self._verdict_from_score(risk_score)
        confidence = min(0.5 + risk_score * 0.5, 0.99)
        recommendations = self._generate_recommendations(signals, verdict)

        self.scan_count += 1
        if verdict == Verdict.PHISHING:
            self.phishing_count += 1

        return AnalysisResult(
            target=text[:80], verdict=verdict, confidence=confidence,
            signals=signals, risk_score=risk_score,
            recommendations=recommendations,
            analysis_time_ms=(time.time() - start) * 1000,
            analyzer="text",
        )

    def batch_scan_urls(self, urls: List[str]) -> List[AnalysisResult]:
        """Scan multiple URLs."""
        return [self.analyze_url(url) for url in urls]

    def get_stats(self) -> Dict[str, Any]:
        """Get scan statistics."""
        return {
            "total_scans": self.scan_count,
            "phishing_found": self.phishing_count,
            "detection_rate": (self.phishing_count / self.scan_count * 100) if self.scan_count > 0 else 0,
        }

    # ─── Helpers ──────────────────────────────────────────────────────

    def _calculate_risk(self, signals: List[Signal]) -> float:
        if not signals:
            return 0.0
        return min(sum(s.weight for s in signals), 1.0)

    def _verdict_from_score(self, score: float) -> Verdict:
        if score >= 0.7:
            return Verdict.PHISHING
        elif score >= 0.3:
            return Verdict.SUSPICIOUS
        else:
            return Verdict.LEGITIMATE

    def _generate_recommendations(self, signals: List[Signal], verdict: Verdict) -> List[str]:
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

        if "homograph" in signal_names:
            recs.append("🎭 Possible homograph attack — check URL carefully")

        if "at-symbol" in signal_names:
            recs.append("⚠️ URL contains @ symbol — this is a credential phishing technique")

        if not recs:
            recs.append("✅ No major issues detected")

        return recs
