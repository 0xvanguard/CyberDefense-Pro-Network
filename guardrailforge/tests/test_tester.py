"""Tests for GuardRailForge — Core Testing Engine"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from src.tester import (
    AttackVector, TestResult, TestSuite, GuardrailTester,
    AttackLibrary, Severity, Verdict
)


class TestAttackVector:
    def test_creation(self):
        v = AttackVector(id="T-001", name="Test", category="test", payload="hello")
        assert v.id == "T-001"
        assert v.severity == Severity.MEDIUM

    def test_to_dict(self):
        v = AttackVector(id="T-001", name="Test", category="test", payload="hello")
        d = v.to_dict()
        assert d["id"] == "T-001"
        assert d["severity"] == "medium"

    def test_tags_default(self):
        v = AttackVector(id="T-001", name="Test", category="test", payload="hello")
        assert v.tags == []

    def test_metadata_default(self):
        v = AttackVector(id="T-001", name="Test", category="test", payload="hello")
        assert v.metadata == {}


class TestTestResult:
    def test_creation(self):
        v = AttackVector(id="T-001", name="Test", category="test", payload="hello")
        r = TestResult(vector=v, verdict=Verdict.BLOCKED, response="no", latency_ms=10.0)
        assert r.verdict == Verdict.BLOCKED
        assert r.latency_ms == 10.0

    def test_to_dict(self):
        v = AttackVector(id="T-001", name="Test", category="test", payload="hello")
        r = TestResult(vector=v, verdict=Verdict.BYPASSED, response="yes", latency_ms=5.0)
        d = r.to_dict()
        assert d["verdict"] == "bypassed"
        assert d["latency_ms"] == 5.0


class TestTestSuite:
    def test_empty(self):
        s = TestSuite()
        assert s.total == 0
        assert s.bypass_rate == 0

    def test_summary(self):
        v = AttackVector(id="T-001", name="Test", category="test", payload="hello",
                        severity=Severity.HIGH)
        results = [
            TestResult(vector=v, verdict=Verdict.BLOCKED, response="no", latency_ms=1.0),
            TestResult(vector=v, verdict=Verdict.BYPASSED, response="yes", latency_ms=2.0),
            TestResult(vector=v, verdict=Verdict.PARTIAL, response="maybe", latency_ms=3.0),
        ]
        s = TestSuite(results=results, model="gpt-4", guardrail="default")
        summary = s.summary()
        assert summary["total_tests"] == 3
        assert summary["bypassed"] == 1
        assert summary["blocked"] == 1

    def test_severity_breakdown(self):
        v_crit = AttackVector(id="T-001", name="Test", category="test", payload="hello",
                             severity=Severity.CRITICAL)
        v_high = AttackVector(id="T-002", name="Test2", category="test", payload="world",
                             severity=Severity.HIGH)
        results = [
            TestResult(vector=v_crit, verdict=Verdict.BYPASSED, response="yes", latency_ms=1.0),
            TestResult(vector=v_high, verdict=Verdict.BLOCKED, response="no", latency_ms=2.0),
        ]
        s = TestSuite(results=results)
        breakdown = s._severity_breakdown()
        assert breakdown["critical"]["bypassed"] == 1
        assert breakdown["high"]["bypassed"] == 0

    def test_to_json(self):
        s = TestSuite(model="test")
        j = s.to_json()
        assert isinstance(j, str)
        assert "summary" in j


class TestGuardrailTester:
    def test_init(self):
        t = GuardrailTester(model="gpt-4")
        assert t.model == "gpt-4"

    def test_run(self):
        t = GuardrailTester(model="test", delay_ms=0)
        vectors = [
            AttackVector(id="T-001", name="Test", category="test", payload="hello"),
            AttackVector(id="T-002", name="Test2", category="test", payload="world"),
        ]
        results = t.run(vectors)
        assert results.total == 2
        assert all(isinstance(r.verdict, Verdict) for r in results.results)

    def test_evaluate_blocked(self):
        t = GuardrailTester()
        v = AttackVector(id="T-001", name="Test", category="test", payload="hello")
        verdict = t._evaluate_response("I'm sorry, I can't do that", v)
        assert verdict == Verdict.BLOCKED

    def test_evaluate_bypassed(self):
        t = GuardrailTester()
        v = AttackVector(id="T-001", name="Test", category="test", payload="hello")
        verdict = t._evaluate_response("Sure, here's how you can do it", v)
        assert verdict == Verdict.BYPASSED

    def test_evaluate_partial(self):
        t = GuardrailTester()
        v = AttackVector(id="T-001", name="Test", category="test", payload="hello")
        verdict = t._evaluate_response("The weather is nice today.", v)
        assert verdict == Verdict.PARTIAL


class TestAttackLibrary:
    def test_load_basic(self):
        lib = AttackLibrary.load("basic")
        assert lib.count >= 5

    def test_load_owasp(self):
        lib = AttackLibrary.load("owasp_top10")
        assert lib.count == 10

    def test_load_encoding(self):
        lib = AttackLibrary.load("encoding")
        assert lib.count >= 6

    def test_load_jailbreak(self):
        lib = AttackLibrary.load("jailbreak")
        assert lib.count >= 8

    def test_load_extraction(self):
        lib = AttackLibrary.load("extraction")
        assert lib.count >= 5

    def test_load_injection(self):
        lib = AttackLibrary.load("injection")
        assert lib.count >= 6

    def test_load_social_engineering(self):
        lib = AttackLibrary.load("social_engineering")
        assert lib.count >= 6

    def test_load_multi_turn(self):
        lib = AttackLibrary.load("multi_turn")
        assert lib.count >= 3

    def test_load_all(self):
        lib = AttackLibrary.load("all")
        assert lib.count >= 50

    def test_filter_category(self):
        lib = AttackLibrary.load("all")
        extraction = lib.filter(category="extraction")
        assert all(v.category == "extraction" for v in extraction)

    def test_filter_severity(self):
        lib = AttackLibrary.load("all")
        critical = lib.filter(severity=Severity.CRITICAL)
        assert all(v.severity == Severity.CRITICAL for v in critical)

    def test_add_vector(self):
        lib = AttackLibrary()
        lib.add(AttackVector(id="T-001", name="Test", category="test", payload="hello"))
        assert lib.count == 1
