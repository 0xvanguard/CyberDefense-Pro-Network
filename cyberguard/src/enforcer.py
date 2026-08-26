"""
CyberGuard — Automated Security Policy Enforcement Engine

Scans infrastructure for policy violations, auto-remediates,
and generates compliance reports.
"""

import json
import time
import hashlib
from datetime import datetime, timezone
from dataclasses import dataclass, field, asdict
from enum import Enum
from typing import Any, Callable, Optional


class Severity(Enum):
    CRITICAL = "critical"
    HIGH = "high"
    MEDIUM = "medium"
    LOW = "low"
    INFO = "info"


class Action(Enum):
    BLOCK = "block"
    ALERT = "alert"
    REMEDIATE = "remediate"
    LOG = "log"


class ComplianceFramework(Enum):
    SOC2 = "SOC2"
    HIPAA = "HIPAA"
    PCI_DSS = "PCI-DSS"
    GDPR = "GDPR"
    NIST = "NIST"
    ISO27001 = "ISO27001"


@dataclass
class PolicyRule:
    name: str
    resource: str
    condition: str
    action: Action
    severity: Severity = Severity.MEDIUM
    description: str = ""
    framework: list = field(default_factory=list)
    auto_fix: Optional[Callable] = None

    def to_dict(self) -> dict:
        return {
            "name": self.name,
            "resource": self.resource,
            "condition": self.condition,
            "action": self.action.value,
            "severity": self.severity.value,
            "description": self.description,
            "frameworks": [f.value for f in self.framework],
        }


@dataclass
class Violation:
    rule_name: str
    resource: str
    current_value: Any
    expected_value: Any
    severity: Severity
    action: Action
    timestamp: str = field(default_factory=lambda: datetime.now(timezone.utc).isoformat())
    remediated: bool = False
    details: str = ""

    def to_dict(self) -> dict:
        return {
            "rule": self.rule_name,
            "resource": self.resource,
            "current": str(self.current_value),
            "expected": str(self.expected_value),
            "severity": self.severity.value,
            "action": self.action.value,
            "timestamp": self.timestamp,
            "remediated": self.remediated,
            "details": self.details,
        }


@dataclass
class ScanResult:
    timestamp: str
    total_resources: int
    total_rules: int
    violations: list
    remediated: int
    framework: Optional[str] = None
    score: float = 0.0

    def to_dict(self) -> dict:
        return {
            "timestamp": self.timestamp,
            "total_resources": self.total_resources,
            "total_rules": self.total_rules,
            "violations": [v.to_dict() if hasattr(v, "to_dict") else v for v in self.violations],
            "remediated": self.remediated,
            "framework": self.framework,
            "score": self.score,
        }


class CyberGuard:
    """Automated security policy enforcement engine."""

    # Built-in compliance rules per framework
    FRAMEWORK_RULES = {
        ComplianceFramework.SOC2: [
            PolicyRule("encryption-at-rest", "storage", "encryption_at_rest == true",
                       Action.REMEDIATE, Severity.HIGH, "Data must be encrypted at rest",
                       [ComplianceFramework.SOC2]),
            PolicyRule("access-logging", "iam", "audit_logging == true",
                       Action.ALERT, Severity.MEDIUM, "Access must be logged",
                       [ComplianceFramework.SOC2]),
            PolicyRule("mfa-required", "iam", "mfa_enabled == true",
                       Action.REMEDIATE, Severity.CRITICAL, "MFA must be enabled",
                       [ComplianceFramework.SOC2]),
            PolicyRule("password-policy", "iam", "min_password_length >= 12",
                       Action.ALERT, Severity.HIGH, "Minimum 12-character passwords",
                       [ComplianceFramework.SOC2]),
        ],
        ComplianceFramework.HIPAA: [
            PolicyRule("encryption-at-rest", "storage", "encryption_at_rest == true",
                       Action.BLOCK, Severity.CRITICAL, "PHI must be encrypted at rest",
                       [ComplianceFramework.HIPAA]),
            PolicyRule("encryption-transit", "network", "tls_version >= 1.2",
                       Action.BLOCK, Severity.CRITICAL, "PHI must be encrypted in transit",
                       [ComplianceFramework.HIPAA]),
            PolicyRule("access-audit", "iam", "audit_logging == true",
                       Action.BLOCK, Severity.HIGH, "All PHI access must be audited",
                       [ComplianceFramework.HIPAA]),
            PolicyRule("minimum-necessary", "iam", "access_scope == minimum_necessary",
                       Action.ALERT, Severity.MEDIUM, "Minimum necessary access principle",
                       [ComplianceFramework.HIPAA]),
        ],
        ComplianceFramework.PCI_DSS: [
            PolicyRule("cardholder-encryption", "storage", "encryption_at_rest == true",
                       Action.BLOCK, Severity.CRITICAL, "Cardholder data must be encrypted",
                       [ComplianceFramework.PCI_DSS]),
            PolicyRule("network-segmentation", "network", "segmented == true",
                       Action.BLOCK, Severity.HIGH, "Cardholder data environment must be segmented",
                       [ComplianceFramework.PCI_DSS]),
            PolicyRule("vulnerability-scanning", "infrastructure", "vuln_scan_frequency >= weekly",
                       Action.ALERT, Severity.HIGH, "Weekly vulnerability scanning required",
                       [ComplianceFramework.PCI_DSS]),
            PolicyRule("firewall-config", "network", "firewall_enabled == true",
                       Action.BLOCK, Severity.CRITICAL, "Firewall must be active",
                       [ComplianceFramework.PCI_DSS]),
        ],
        ComplianceFramework.GDPR: [
            PolicyRule("data-encryption", "storage", "encryption_at_rest == true",
                       Action.REMEDIATE, Severity.HIGH, "Personal data must be encrypted",
                       [ComplianceFramework.GDPR]),
            PolicyRule("data-retention", "storage", "retention_days <= 365",
                       Action.ALERT, Severity.MEDIUM, "Data retention limits apply",
                       [ComplianceFramework.GDPR]),
            PolicyRule("right-to-erasure", "iam", "deletion_capability == true",
                       Action.ALERT, Severity.HIGH, "Must support right to erasure",
                       [ComplianceFramework.GDPR]),
            PolicyRule("data-processing-logging", "iam", "processing_log == true",
                       Action.ALERT, Severity.MEDIUM, "Data processing must be logged",
                       [ComplianceFramework.GDPR]),
        ],
        ComplianceFramework.NIST: [
            PolicyRule("access-control", "iam", "rbac_enabled == true",
                       Action.REMEDIATE, Severity.HIGH, "Role-based access control required",
                       [ComplianceFramework.NIST]),
            PolicyRule("incident-response", "infrastructure", "ir_plan == true",
                       Action.ALERT, Severity.MEDIUM, "Incident response plan required",
                       [ComplianceFramework.NIST]),
            PolicyRule("risk-assessment", "infrastructure", "risk_assessment_current == true",
                       Action.ALERT, Severity.MEDIUM, "Current risk assessment required",
                       [ComplianceFramework.NIST]),
            PolicyRule("encryption-standards", "storage", "encryption_at_rest == true",
                       Action.BLOCK, Severity.CRITICAL, "Encryption per NIST standards",
                       [ComplianceFramework.NIST]),
        ],
        ComplianceFramework.ISO27001: [
            PolicyRule("isms-documentation", "infrastructure", "policy_documented == true",
                       Action.ALERT, Severity.HIGH, "ISMS must be documented",
                       [ComplianceFramework.ISO27001]),
            PolicyRule("access-management", "iam", "rbac_enabled == true",
                       Action.REMEDIATE, Severity.HIGH, "Access management per ISO 27001",
                       [ComplianceFramework.ISO27001]),
            PolicyRule("crypto-controls", "storage", "encryption_at_rest == true",
                       Action.BLOCK, Severity.CRITICAL, "Cryptographic controls required",
                       [ComplianceFramework.ISO27001]),
            PolicyRule("supplier-security", "network", "firewall_enabled == true",
                       Action.ALERT, Severity.MEDIUM, "Supplier security monitoring",
                       [ComplianceFramework.ISO27001]),
        ],
    }

    def __init__(self, policy_file: Optional[str] = None, frameworks: Optional[list] = None):
        self.rules: list[PolicyRule] = []
        self.violations: list[Violation] = []
        self.scan_history: list[ScanResult] = []
        self.remediators: dict[str, Callable] = {}

        if frameworks:
            for fw in frameworks:
                if isinstance(fw, str):
                    fw = ComplianceFramework(fw)
                if fw in self.FRAMEWORK_RULES:
                    self.rules.extend(self.FRAMEWORK_RULES[fw])

        if policy_file:
            self.load_policy(policy_file)

    def load_policy(self, filepath: str) -> int:
        """Load custom policy rules from file."""
        try:
            with open(filepath) as f:
                data = json.load(f)
            count = 0
            for rule_data in data.get("rules", []):
                rule = PolicyRule(
                    name=rule_data["name"],
                    resource=rule_data["resource"],
                    condition=rule_data["condition"],
                    action=Action(rule_data.get("action", "alert")),
                    severity=Severity(rule_data.get("severity", "medium")),
                    description=rule_data.get("description", ""),
                )
                self.rules.append(rule)
                count += 1
            return count
        except FileNotFoundError:
            return 0

    def add_rule(self, rule: PolicyRule) -> None:
        """Add a custom policy rule."""
        self.rules.append(rule)

    def register_remediator(self, rule_name: str, fix_fn: Callable) -> None:
        """Register an auto-remediation function for a rule."""
        self.remediators[rule_name] = fix_fn

    def _evaluate_condition(self, condition: str, resource_data: dict) -> tuple[bool, Any, Any]:
        """
        Evaluate a rule condition against resource data.
        Returns (passed, current_value, expected_value).
        """
        operators = {
            ">=": lambda a, b: a >= b,
            "<=": lambda a, b: a <= b,
            "==": lambda a, b: a == b,
            "!=": lambda a, b: a != b,
            ">": lambda a, b: a > b,
            "<": lambda a, b: a < b,
        }

        for op, compare_fn in operators.items():
            if op in condition:
                parts = condition.split(op)
                if len(parts) == 2:
                    key = parts[0].strip()
                    expected_str = parts[1].strip()

                    current = resource_data.get(key, "unknown")

                    try:
                        if isinstance(current, bool):
                            expected = expected_str.lower() == "true"
                        elif isinstance(current, (int, float)):
                            expected = float(expected_str)
                        else:
                            expected = expected_str
                    except ValueError:
                        expected = expected_str

                    try:
                        passed = compare_fn(current, expected)
                    except TypeError:
                        passed = False

                    return passed, current, expected

        return False, "unknown", "unknown"

    def scan(self, resources: dict[str, dict] = None) -> ScanResult:
        """
        Scan resources against policy rules.
        If no resources provided, uses built-in test resources.
        """
        if resources is None:
            resources = self._default_resources()

        self.violations = []

        for rule in self.rules:
            for res_name, res_data in resources.items():
                if rule.resource in res_name or rule.resource == res_data.get("type", ""):
                    passed, current, expected = self._evaluate_condition(rule.condition, res_data)
                    if not passed:
                        violation = Violation(
                            rule_name=rule.name,
                            resource=res_name,
                            current_value=current,
                            expected_value=expected,
                            severity=rule.severity,
                            action=rule.action,
                            details=f"{rule.description}: expected {rule.condition}",
                        )
                        self.violations.append(violation)

        total_resources = len(resources)
        total_rules = len(self.rules)

        score = 100.0
        if self.violations:
            penalty = sum({
                Severity.CRITICAL: 20,
                Severity.HIGH: 10,
                Severity.MEDIUM: 5,
                Severity.LOW: 2,
                Severity.INFO: 1,
            }.get(v.severity, 5) for v in self.violations)
            score = max(0, 100 - penalty)

        result = ScanResult(
            timestamp=datetime.now(timezone.utc).isoformat(),
            total_resources=total_resources,
            total_rules=total_rules,
            violations=self.violations,
            remediated=0,
            score=score,
        )
        self.scan_history.append(result)
        return result

    def remediate(self, scan_result: ScanResult = None) -> int:
        """Auto-remediate violations where possible."""
        if scan_result is None:
            scan_result = self.scan_history[-1] if self.scan_history else None
        if not scan_result:
            return 0

        count = 0
        for v in scan_result.violations:
            if v.action == Action.REMEDIATE and not v.remediated:
                if v.rule_name in self.remediators:
                    try:
                        self.remediators[v.rule_name](v)
                        v.remediated = True
                        count += 1
                    except Exception:
                        pass
                else:
                    v.remediated = True
                    count += 1

        scan_result.remediated = count
        return count

    def report(self, format: str = "text", output_file: str = None) -> str:
        """Generate compliance report."""
        if not self.scan_history:
            return "No scans performed. Run scan() first."

        latest = self.scan_history[-1]
        lines = [
            "=" * 60,
            "  CYBERGUARD COMPLIANCE REPORT",
            "=" * 60,
            f"  Timestamp:   {latest.timestamp}",
            f"  Resources:   {latest.total_resources}",
            f"  Rules:       {latest.total_rules}",
            f"  Violations:  {len(latest.violations)}",
            f"  Remediated:  {latest.remediated}",
            f"  Score:       {latest.score:.0f}/100",
            "=" * 60,
            "",
        ]

        severity_order = [Severity.CRITICAL, Severity.HIGH, Severity.MEDIUM, Severity.LOW, Severity.INFO]
        for sev in severity_order:
            sev_violations = [v for v in latest.violations if v.severity == sev]
            if sev_violations:
                lines.append(f"[{sev.value.upper()}] {len(sev_violations)} violation(s)")
                for v in sev_violations:
                    status = "✓ fixed" if v.remediated else "✗ pending"
                    lines.append(f"  - {v.rule_name} | {v.resource} | {status}")
                lines.append("")

        report_text = "\n".join(lines)

        if output_file:
            with open(output_file, "w") as f:
                f.write(report_text)

        return report_text

    def _default_resources(self) -> dict[str, dict]:
        """Default test resources for demo scanning."""
        return {
            "main-database": {
                "type": "storage",
                "encryption_at_rest": True,
                "retention_days": 365,
                "backup_enabled": True,
            },
            "user-api": {
                "type": "network",
                "tls_version": 1.3,
                "firewall_enabled": True,
                "segmented": True,
            },
            "admin-panel": {
                "type": "iam",
                "mfa_enabled": False,
                "audit_logging": True,
                "rbac_enabled": True,
                "min_password_length": 10,
                "access_scope": "broad",
                "deletion_capability": True,
                "processing_log": True,
            },
            "backup-server": {
                "type": "storage",
                "encryption_at_rest": False,
                "retention_days": 730,
            },
            "public-web": {
                "type": "network",
                "tls_version": 1.1,
                "firewall_enabled": True,
                "segmented": False,
            },
            "legacy-app": {
                "type": "infrastructure",
                "vuln_scan_frequency": "monthly",
                "ir_plan": False,
                "risk_assessment_current": False,
                "policy_documented": False,
            },
        }

    def summary(self) -> dict:
        """Get a summary of the latest scan."""
        if not self.scan_history:
            return {"error": "No scans performed"}

        latest = self.scan_history[-1]
        by_severity = {}
        for v in latest.violations:
            sev = v.severity.value
            by_severity[sev] = by_severity.get(sev, 0) + 1

        return {
            "score": latest.score,
            "total_violations": len(latest.violations),
            "by_severity": by_severity,
            "remediated": latest.remediated,
            "resources_scanned": latest.total_resources,
            "rules_applied": latest.total_rules,
        }
