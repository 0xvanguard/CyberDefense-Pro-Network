<p align="center">
  <img src="https://img.shields.io/badge/version-2.0.0-blue?style=for-the-badge">
  <img src="https://img.shields.io/badge/python-3.10+-yellow?style=for-the-badge&logo=python&logoColor=white">
  <img src="https://img.shields.io/badge/license-MIT-green?style=for-the-badge">
  <img src="https://img.shields.io/badge/tests-23-passing-brightgreen?style=for-the-badge">
  <img src="https://img.shields.io/github/stars/0xvanguard/zerotrustkit?style=for-the-badge">
</p>

# 🛡️ ZeroTrustKit

**Zero Trust Security Implementation Toolkit — Never trust, always verify.**

ZeroTrustKit provides a complete framework for implementing Zero Trust architecture: identity verification, device profiling, network microsegmentation, session management, policy enforcement, and audit logging.

## ✨ Features

| Feature | Description |
|---------|-------------|
| **Identity Verification** | Multi-factor risk scoring engine |
| **Device Profiling** | Register, trust, revoke, quarantine devices |
| **Session Management** | Create, validate, revoke sessions |
| **Network Segmentation** | Microsegment definitions with CIDR |
| **Policy Engine** | Customizable access policies |
| **Audit Logging** | Full audit trail of all decisions |
| **IP Blocklist** | Block known malicious IPs |
| **Risk Scoring** | Composite risk from device + location + time + role |

## 🚀 Quick Start

```bash
pip install -r requirements.txt

# Verify a request
python cli.py verify --user john@example.com --device iPhone-14 --ip 10.0.1.5

# Register a device
python cli.py register --device-id dev-001 --name "MacBook Pro" --trust high --mfa

# Create a session
python cli.py session --user john@example.com --create

# View policies
python cli.py policies

# View network segments
python cli.py segments

# Block an IP
python cli.py block --ip 192.168.1.100

# Audit log
python cli.py audit --limit 20

# Stats
python cli.py stats
```

## 🐍 Python API

```python
from src.kit import ZeroTrustKit, TrustLevel

ztk = ZeroTrustKit()

# Register a trusted device
ztk.register_device("dev-001", "MacBook Pro", trust_level=TrustLevel.HIGH, mfa_enabled=True)

# Verify a request
result = ztk.verify(user="john@example.com", device="dev-001", ip="10.0.1.5", location="US")
print(f"Action: {result.action.value}, Risk: {result.risk_score:.2f}")

# Create session
session = ztk.create_session(user="john@example.com", device_id="dev-001")

# Network access check
access = ztk.check_network_access("10.0.1.5", "ssh")
print(f"Allowed: {access['allowed']}, Zone: {access['zone']}")
```

## 🔐 Zero Trust Principles

| Principle | Implementation |
|-----------|---------------|
| **Verify Explicitly** | Identity + device + location + time verification |
| **Least Privilege** | Role-based policies with step-up auth |
| **Assume Breach** | Device quarantine, network segmentation |
| **Continuous Verification** | Session validation, audit logging |

## 📁 Structure

```
zerotrustkit/
├── src/
│   ├── __init__.py
│   └── kit.py              # Core engine
├── tests/
│   └── test_kit.py         # 23 tests
├── cli.py                  # CLI tool
├── requirements.txt
└── README.md
```

## 📄 License

MIT License — see [LICENSE](LICENSE)
