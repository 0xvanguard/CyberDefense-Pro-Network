<p align="center">
  <img src="https://img.shields.io/badge/version-2.0.0-blue?style=for-the-badge">
  <img src="https://img.shields.io/badge/python-3.10+-yellow?style=for-the-badge&logo=python&logoColor=white">
  <img src="https://img.shields.io/badge/license-MIT-green?style=for-the-badge">
  <img src="https://img.shields.io/badge/tests-22-passing-brightgreen?style=for-the-badge">
  <img src="https://img.shields.io/github/stars/0xvanguard/cyberguard?style=for-the-badge">
</p>

# 🛡️ CyberGuard

**Automated Security Policy Enforcement — SOC2, HIPAA, PCI-DSS, GDPR, NIST, ISO27001.**

CyberGuard scans infrastructure against compliance frameworks, detects policy violations, auto-remediates where possible, and generates compliance reports with risk scores.

## ✨ Features

| Feature | Description |
|---------|-------------|
| **6 Frameworks** | SOC2, HIPAA, PCI-DSS, GDPR, NIST, ISO27001 |
| **Policy Engine** | Custom rules with condition evaluation |
| **Auto-Remediation** | Fix violations automatically |
| **Risk Scoring** | 0–100 compliance score |
| **Compliance Reports** | Text and JSON export |
| **Custom Policies** | Load rules from JSON files |
| **Multi-Framework** | Scan against multiple frameworks |
| **Violation Tracking** | Severity, action, remediation status |

## 🚀 Quick Start

```bash
pip install -r requirements.txt

# Scan against SOC2
python cli.py scan --framework SOC2

# Scan against multiple frameworks
python cli.py scan -f HIPAA -f PCI-DSS

# Auto-remediate
python cli.py scan -f SOC2 --auto-fix

# Generate report
python cli.py report -f GDPR

# List frameworks
python cli.py frameworks

# View rules
python cli.py rules --framework HIPAA
```

## 🐍 Python API

```python
from src.enforcer import CyberGuard

guard = CyberGuard(frameworks=["SOC2", "HIPAA"])

# Scan
result = guard.scan()
print(f"Score: {result.score}/100")
print(f"Violations: {len(result.violations)}")

# Remediate
count = guard.remediate()

# Report
print(guard.report())

# Custom resources
result = guard.scan(resources={
    "my-db": {"type": "storage", "encryption_at_rest": True},
    "my-api": {"type": "iam", "mfa_enabled": True},
})
```

## 📋 Frameworks

| Framework | Rules | Focus |
|-----------|-------|-------|
| **SOC2** | 4 | Encryption, MFA, audit logging |
| **HIPAA** | 4 | PHI encryption, access control |
| **PCI-DSS** | 4 | Cardholder data, network segmentation |
| **GDPR** | 4 | Data encryption, retention, erasure |
| **NIST** | 4 | RBAC, incident response, risk assessment |
| **ISO27001** | 4 | ISMS, crypto controls, access management |

## 📁 Structure

```
cyberguard/
├── src/
│   ├── __init__.py
│   └── enforcer.py          # Core engine
├── tests/
│   └── test_enforcer.py     # 22 tests
├── cli.py                   # CLI tool
├── requirements.txt
└── README.md
```

## 📄 License

MIT License — see [LICENSE](LICENSE)
