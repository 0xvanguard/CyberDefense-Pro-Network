"""PhishGuard — Phishing Detection Engine"""

from .detector import (
    Verdict, Signal, AnalysisResult,
    URLAnalyzer, EmailAnalyzer, ContentAnalyzer,
    PhishDetector
)

__version__ = "2.0.0"
__all__ = [
    "Verdict", "Signal", "AnalysisResult",
    "URLAnalyzer", "EmailAnalyzer", "ContentAnalyzer",
    "PhishDetector"
]
