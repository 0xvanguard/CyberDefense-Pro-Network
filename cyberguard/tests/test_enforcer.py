"""Tests for CyberGuard"""

import os
import sys
import tempfile
import json

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.enforcer import (
    Severity, Action, ComplianceFramework,
    PolicyRule, Violation, ScanResult, CyberGuard
)


def test_severity_enum():
    assert Severity.CRITICAL.value == "critical"
    assert Severity.HIGH.value == "high"
    assert Severity.MEDIUM.value == "medium"
    assert Severity.LOW.value == "low"
    assert Severity.INFO.value == "info"
    print("✅ Severity enum OK")


def test_action_enum():
    assert Action.BLOCK.value == "block"
    assert Action.ALERT.value == "alert"
    assert Action.REMEDIATE.value == "remediate"
    assert Action.LOG.value == "log"
    print("✅ Action enum OK")


def test_compliance_frameworks():
    frameworks = list(ComplianceFramework)
    assert len(frameworks) == 6
    names = [fw.value for fw in frameworks]
    assert "SOC2" in names
    assert "HIPAA" in names
    assert "PCI-DSS" in names
    assert "GDPR" in names
    assert "NIST" in names
    assert "ISO27001" in names
    print(f"✅ Compliance frameworks: {len(frameworks)}")


def test_policy_rule_creation():
    rule = PolicyRule(
        name="test-rule", resource="storage",
        condition="encryption == true",
        action=Action.BLOCK, severity=Severity.CRITICAL,
        description="Test rule",
    )
    assert rule.name == "test-rule"
    assert rule.action == Action.BLOCK
    print("✅ PolicyRule creation OK")


def test_policy_rule_to_dict():
    rule = PolicyRule(
        name="test", resource="iam",
        condition="mfa == true", action=Action.REMEDIATE,
        framework=[ComplianceFramework.SOC2],
    )
    d = rule.to_dict()
    assert d["name"] == "test"
    assert d["action"] == "remediate"
    assert "SOC2" in d["frameworks"]
    print("✅ PolicyRule to_dict OK")


def test_violation_creation():
    v = Violation(
        rule_name="test", resource="db",
        current_value=False, expected_value=True,
        severity=Severity.HIGH, action=Action.BLOCK,
    )
    assert v.rule_name == "test"
    assert v.remediated is False
    print("✅ Violation creation OK")


def test_violation_to_dict():
    v = Violation(
        rule_name="test", resource="db",
        current_value=False, expected_value=True,
        severity=Severity.CRITICAL, action=Action.REMEDIATE,
    )
    d = v.to_dict()
    assert d["severity"] == "critical"
    assert d["remediated"] is False
    print("✅ Violation to_dict OK")


def test_cyberguard_init_soc2():
    guard = CyberGuard(frameworks=["SOC2"])
    assert len(guard.rules) > 0
    print(f"✅ CyberGuard SOC2: {len(guard.rules)} rules")


def test_cyberguard_init_hipaa():
    guard = CyberGuard(frameworks=["HIPAA"])
    assert len(guard.rules) > 0
    print(f"✅ CyberGuard HIPAA: {len(guard.rules)} rules")


def test_cyberguard_init_multi():
    guard = CyberGuard(frameworks=["SOC2", "HIPAA", "PCI-DSS"])
    assert len(guard.rules) >= 12
    print(f"✅ CyberGuard multi-framework: {len(guard.rules)} rules")


def test_cyberguard_scan():
    guard = CyberGuard(frameworks=["SOC2"])
    result = guard.scan()
    assert isinstance(result, ScanResult)
    assert result.total_resources > 0
    assert result.total_rules > 0
    assert 0 <= result.score <= 100
    print(f"✅ Scan: score={result.score:.0f}, violations={len(result.violations)}")


def test_scan_produces_violations():
    guard = CyberGuard(frameworks=["SOC2", "HIPAA"])
    result = guard.scan()
    assert len(result.violations) > 0
    print(f"✅ Scan violations: {len(result.violations)} found")


def test_scan_score_decreases_with_violations():
    guard = CyberGuard(frameworks=["SOC2"])
    result = guard.scan()
    if result.violations:
        assert result.score < 100
    print(f"✅ Score decreases: {result.score:.0f}/100")


def test_remediate():
    guard = CyberGuard(frameworks=["SOC2"])
    guard.scan()
    count = guard.remediate()
    assert count >= 0
    print(f"✅ Remediated: {count} violations")


def test_report():
    guard = CyberGuard(frameworks=["SOC2"])
    guard.scan()
    report = guard.report()
    assert "CYBERGUARD" in report
    assert "Score:" in report
    print("✅ Report generated")


def test_report_to_file():
    guard = CyberGuard(frameworks=["SOC2"])
    guard.scan()
    with tempfile.NamedTemporaryFile(suffix=".txt", delete=False) as f:
        path = f.name
    try:
        guard.report(output_file=path)
        with open(path) as f:
            content = f.read()
        assert "CYBERGUARD" in content
    finally:
        os.unlink(path)
    print("✅ Report to file OK")


def test_summary():
    guard = CyberGuard(frameworks=["SOC2"])
    guard.scan()
    summary = guard.summary()
    assert "score" in summary
    assert "total_violations" in summary
    assert "by_severity" in summary
    print(f"✅ Summary: score={summary['score']:.0f}")


def test_framework_rules():
    for fw in ComplianceFramework:
        rules = CyberGuard.FRAMEWORK_RULES.get(fw, [])
        assert len(rules) > 0, f"No rules for {fw.value}"
    print(f"✅ All frameworks have rules")


def test_custom_resources():
    guard = CyberGuard(frameworks=["SOC2"])
    resources = {
        "my-db": {
            "type": "storage",
            "encryption_at_rest": True,
        },
        "my-api": {
            "type": "iam",
            "mfa_enabled": True,
            "audit_logging": True,
            "min_password_length": 16,
        },
    }
    result = guard.scan(resources=resources)
    assert result.total_resources == 2
    print(f"✅ Custom resources: {result.total_resources} scanned")


def test_add_rule():
    guard = CyberGuard(frameworks=["SOC2"])
    initial = len(guard.rules)
    guard.add_rule(PolicyRule(
        name="custom-rule", resource="storage",
        condition="backup == true", action=Action.ALERT,
    ))
    assert len(guard.rules) == initial + 1
    print("✅ Add custom rule")


def test_custom_policy_file():
    policy = {
        "rules": [
            {
                "name": "test-rule",
                "resource": "storage",
                "condition": "encryption == true",
                "action": "block",
                "severity": "critical",
                "description": "Test policy rule",
            }
        ]
    }
    with tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False) as f:
        json.dump(policy, f)
        path = f.name

    try:
        guard = CyberGuard(policy_file=path)
        assert len(guard.rules) >= 1
    finally:
        os.unlink(path)
    print("✅ Custom policy file loaded")


def test_scan_result_to_dict():
    guard = CyberGuard(frameworks=["SOC2"])
    result = guard.scan()
    d = result.to_dict()
    assert "score" in d
    assert "violations" in d
    assert "total_resources" in d
    print("✅ ScanResult to_dict OK")


if __name__ == "__main__":
    test_severity_enum()
    test_action_enum()
    test_compliance_frameworks()
    test_policy_rule_creation()
    test_policy_rule_to_dict()
    test_violation_creation()
    test_violation_to_dict()
    test_cyberguard_init_soc2()
    test_cyberguard_init_hipaa()
    test_cyberguard_init_multi()
    test_cyberguard_scan()
    test_scan_produces_violations()
    test_scan_score_decreases_with_violations()
    test_remediate()
    test_report()
    test_report_to_file()
    test_summary()
    test_framework_rules()
    test_custom_resources()
    test_add_rule()
    test_custom_policy_file()
    test_scan_result_to_dict()
    print("\n🎉 All 22 tests passed!")
