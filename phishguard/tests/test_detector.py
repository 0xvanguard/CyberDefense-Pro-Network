"""Tests for PhishGuard"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.detector import (
    Verdict, Signal, AnalysisResult,
    URLAnalyzer, EmailAnalyzer, ContentAnalyzer, PhishDetector
)


url_analyzer = URLAnalyzer()
email_analyzer = EmailAnalyzer()
content_analyzer = ContentAnalyzer()
detector = PhishDetector()


def test_verdict_enum():
    assert Verdict.PHISHING.value == "phishing"
    assert Verdict.LEGITIMATE.value == "legitimate"
    assert Verdict.SUSPICIOUS.value == "suspicious"
    print("✅ Verdict enum OK")


def test_signal_creation():
    sig = Signal("test-signal", 0.5, "Test description", "Evidence here")
    assert sig.name == "test-signal"
    assert sig.weight == 0.5
    print("✅ Signal creation OK")


def test_signal_to_dict():
    sig = Signal("test", 0.3, "desc", "ev")
    d = sig.to_dict()
    assert d["name"] == "test"
    assert d["weight"] == 0.3
    print("✅ Signal to_dict OK")


def test_url_suspicious_tld():
    signals = url_analyzer.analyze("https://login-paypal.xyz/verify")
    names = {s.name for s in signals}
    assert "suspicious-tld" in names
    print("✅ URL suspicious TLD detected")


def test_url_brand_impersonation():
    signals = url_analyzer.analyze("https://paypal-secure.top/login")
    names = {s.name for s in signals}
    assert "brand-impersonation" in names
    print("✅ URL brand impersonation detected")


def test_url_ip_address():
    signals = url_analyzer.analyze("http://192.168.1.100/phish")
    names = {s.name for s in signals}
    assert "ip-address" in names
    print("✅ URL IP address detected")


def test_url_no_ssl():
    signals = url_analyzer.analyze("http://example.com")
    names = {s.name for s in signals}
    assert "no-ssl" in names
    print("✅ URL no SSL detected")


def test_url_shortener():
    signals = url_analyzer.analyze("https://bit.ly/abc123")
    names = {s.name for s in signals}
    assert "url-shortener" in names
    print("✅ URL shortener detected")


def test_url_clean():
    signals = url_analyzer.analyze("https://www.google.com/search?q=test")
    risk = sum(s.weight for s in signals)
    assert risk < 0.3
    print(f"✅ URL clean: risk={risk:.2f}")


def test_email_spf_fail():
    headers = {"from": "bad@phish.com", "authentication-results": "spf=fail"}
    signals = email_analyzer.analyze_headers(headers)
    names = {s.name for s in signals}
    assert "spf-fail" in names
    print("✅ Email SPF fail detected")


def test_email_dkim_fail():
    headers = {"from": "bad@phish.com", "authentication-results": "dkim=fail"}
    signals = email_analyzer.analyze_headers(headers)
    names = {s.name for s in signals}
    assert "dkim-fail" in names
    print("✅ Email DKIM fail detected")


def test_email_reply_to_mismatch():
    headers = {"from": "real@bank.com", "reply-to": "scam@phish.com"}
    signals = email_analyzer.analyze_headers(headers)
    names = {s.name for s in signals}
    assert "reply-to-mismatch" in names
    print("✅ Email Reply-To mismatch detected")


def test_email_urgency():
    body = "URGENT: Your account will be closed! Verify immediately or it expires!"
    signals = email_analyzer.analyze_content(body)
    names = {s.name for s in signals}
    assert "high-urgency" in names
    print("✅ Email urgency detected")


def test_email_credential_request():
    body = "Please verify your password and confirm your account credentials."
    signals = email_analyzer.analyze_content(body)
    names = {s.name for s in signals}
    assert "credential-request" in names
    print("✅ Email credential request detected")


def test_content_nigerian_prince():
    text = "I am a prince and I need your help to transfer 5 million dollars"
    signals = content_analyzer.analyze(text)
    names = {s.name for s in signals}
    assert "social-engineering" in names
    print("✅ Content Nigerian prince detected")


def test_content_prize_scam():
    text = "Congratulations! You have won a prize! Click here to claim your reward!"
    signals = content_analyzer.analyze(text)
    names = {s.name for s in signals}
    assert "social-engineering" in names
    print("✅ Content prize scam detected")


def test_detector_url_phishing():
    result = detector.analyze_url("http://paypal-login.xyz/verify?account=steal")
    assert isinstance(result, AnalysisResult)
    assert result.verdict in (Verdict.PHISHING, Verdict.SUSPICIOUS)
    assert len(result.signals) > 0
    print(f"✅ Detector URL: {result.verdict.value} (risk={result.risk_score:.2f})")


def test_detector_url_legit():
    result = detector.analyze_url("https://www.google.com")
    assert result.verdict == Verdict.LEGITIMATE
    print(f"✅ Detector URL legit: {result.verdict.value}")


def test_detector_email_phishing():
    headers = {
        "from": "PayPal Security <security@paypal-verify.xyz>",
        "authentication-results": "spf=fail dkim=fail dmarc=fail",
        "reply-to": "scam@phish.com",
    }
    body = "URGENT: Your account has been suspended! Verify your password immediately or it will be closed!"
    result = detector.analyze_email(headers, body)
    assert result.verdict in (Verdict.PHISHING, Verdict.SUSPICIOUS)
    assert len(result.signals) > 0
    print(f"✅ Detector email: {result.verdict.value} (risk={result.risk_score:.2f})")


def test_detector_text():
    result = detector.analyze_text("You have won a prize! Act now! Click here immediately!")
    assert isinstance(result, AnalysisResult)
    assert len(result.signals) > 0
    print(f"✅ Detector text: {result.verdict.value} (risk={result.risk_score:.2f})")


def test_batch_scan():
    urls = [
        "https://www.google.com",
        "http://paypal-verify.xyz/steal",
        "https://bit.ly/abc123",
    ]
    results = detector.batch_scan_urls(urls)
    assert len(results) == 3
    assert all(isinstance(r, AnalysisResult) for r in results)
    print(f"✅ Batch scan: {len(results)} URLs")


def test_stats():
    stats = detector.get_stats()
    assert "total_scans" in stats
    assert stats["total_scans"] > 0
    print(f"✅ Stats: {stats['total_scans']} scans")


def test_result_to_dict():
    result = detector.analyze_url("https://example.com")
    d = result.to_dict()
    assert "verdict" in d
    assert "signals" in d
    assert "recommendations" in d
    print("✅ Result to_dict OK")


def test_homograph_detection():
    signals = url_analyzer.analyze("https://gооgle.com")  # Cyrillic 'о'
    names = {s.name for s in signals}
    assert "homograph" in names
    print("✅ Homograph detection OK")


def test_at_symbol_detection():
    signals = url_analyzer.analyze("https://google.com@evil.com/login")
    names = {s.name for s in signals}
    assert "at-symbol" in names
    print("✅ @ symbol detection OK")


if __name__ == "__main__":
    test_verdict_enum()
    test_signal_creation()
    test_signal_to_dict()
    test_url_suspicious_tld()
    test_url_brand_impersonation()
    test_url_ip_address()
    test_url_no_ssl()
    test_url_shortener()
    test_url_clean()
    test_email_spf_fail()
    test_email_dkim_fail()
    test_email_reply_to_mismatch()
    test_email_urgency()
    test_email_credential_request()
    test_content_nigerian_prince()
    test_content_prize_scam()
    test_detector_url_phishing()
    test_detector_url_legit()
    test_detector_email_phishing()
    test_detector_text()
    test_batch_scan()
    test_stats()
    test_result_to_dict()
    test_homograph_detection()
    test_at_symbol_detection()
    print("\n🎉 All 25 tests passed!")
