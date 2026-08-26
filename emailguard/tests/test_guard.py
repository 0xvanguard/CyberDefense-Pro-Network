"""Tests for EmailGuard"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src.guard import EmailGuard, SpamFilter, ThreatDetection

def test_spam_clean():
    g = EmailGuard()
    result = g.check_spam("Meeting tomorrow", "Hi, let's discuss the project.")
    assert result.is_spam is False
    print("✅ Clean email: not spam")

def test_spam_detected():
    g = EmailGuard()
    result = g.check_spam("YOU WON!!!", "Congratulations! Click here to claim your free prize! Act now!")
    assert result.is_spam is True
    print(f"✅ Spam detected: score={result.score:.2f}")

def test_spam_reasons():
    g = EmailGuard()
    result = g.check_spam("FREE!!!", "Winner! Click here! Act now!")
    assert len(result.reasons) > 0
    print(f"✅ Spam reasons: {len(result.reasons)}")

def test_threat_spf_fail():
    g = EmailGuard()
    threats = g.detect_threats({"authentication-results": "spf=fail"}, "Hello")
    assert any(t.threat_type == "spoofing" for t in threats)
    print("✅ SPF fail detected")

def test_threat_dkim_fail():
    g = EmailGuard()
    threats = g.detect_threats({"authentication-results": "dkim=fail"}, "Hello")
    assert len(threats) > 0
    print("✅ DKIM fail detected")

def test_threat_phishing():
    g = EmailGuard()
    threats = g.detect_threats({}, "Please verify your account by clicking here")
    assert any(t.threat_type == "phishing" for t in threats)
    print("✅ Phishing detected")

def test_threat_clean():
    g = EmailGuard()
    threats = g.detect_threats({}, "Meeting at 3pm tomorrow")
    assert len(threats) == 0
    print("✅ Clean email: no threats")

def test_statistics():
    g = EmailGuard()
    g.check_spam("test", "test")
    g.check_spam("FREE!!!", "Winner! Click here!")
    stats = g.get_statistics()
    assert stats["scans"] == 2
    print("✅ Statistics OK")

def test_spam_score_range():
    g = EmailGuard()
    result = g.check_spam("normal", "normal content")
    assert 0 <= result.score <= 1
    print("✅ Score range OK")

def test_threat_severity():
    g = EmailGuard()
    threats = g.detect_threats({"authentication-results": "dmarc=fail"}, "text")
    assert any(t.severity == "critical" for t in threats)
    print("✅ Threat severity OK")

if __name__ == "__main__":
    test_spam_clean()
    test_spam_detected()
    test_spam_reasons()
    test_threat_spf_fail()
    test_threat_dkim_fail()
    test_threat_phishing()
    test_threat_clean()
    test_statistics()
    test_spam_score_range()
    test_threat_severity()
    print("\n🎉 All 10 tests passed!")
