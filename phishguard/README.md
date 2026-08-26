<p align="center">
  <img src="https://img.shields.io/badge/version-2.0.0-blue?style=for-the-badge">
  <img src="https://img.shields.io/badge/python-3.10+-yellow?style=for-the-badge&logo=python&logoColor=white">
  <img src="https://img.shields.io/badge/license-MIT-green?style=for-the-badge">
  <img src="https://img.shields.io/badge/tests-25-passing-brightgreen?style=for-the-badge">
  <img src="https://img.shields.io/github/stars/0xvanguard/phishguard?style=for-the-badge">
</p>

# 🛡️ PhishGuard

**Phishing Detection Engine — URL, Email, and Content Analysis.**

PhishGuard detects phishing attempts using lexical analysis, pattern matching, and heuristic scoring. Analyzes URLs for suspicious TLDs, brand impersonation, and homograph attacks. Scans emails for SPF/DKIM failures, urgency patterns, and credential harvesting. Detects social engineering in text content.

## ✨ Features

| Feature | Description |
|---------|-------------|
| **URL Analysis** | TLD, brand impersonation, IP domains, homographs |
| **Email Analysis** | SPF/DKIM/DMARC, urgency, credential requests |
| **Content Analysis** | Social engineering patterns, scam detection |
| **Batch Scanning** | Scan multiple URLs at once |
| **Risk Scoring** | 0.0–1.0 composite risk score |
| **Verdict System** | Legitimate / Suspicious / Phishing |
| **Homograph Detection** | Cyrillic character substitution attacks |
| **@ Symbol Detection** | URL confusion phishing technique |

## 🚀 Quick Start

```bash
pip install -r requirements.txt

# Analyze URL
python cli.py url "https://paypal-verify.xyz/login"

# Analyze email
python cli.py email --from "bad@phish.com" --body "Verify your password!"

# Analyze text
python cli.py text "You have won a prize! Act now!"

# Batch scan
python cli.py batch --file urls.txt

# Stats
python cli.py stats
```

## 🐍 Python API

```python
from src.detector import PhishDetector

detector = PhishDetector()

# URL analysis
result = detector.analyze_url("http://paypal-login.xyz/steal")
print(f"Verdict: {result.verdict.value}, Risk: {result.risk_score:.2f}")

# Email analysis
result = detector.analyze_email(
    headers={"from": "PayPal <security@paypal-verify.xyz>", "authentication-results": "spf=fail"},
    body="URGENT: Verify your password immediately!"
)

# Text analysis
result = detector.analyze_text("I am a prince and need your help transferring money")

# Batch scan
results = detector.batch_scan_urls(["https://google.com", "http://phish.xyz"])
```

## 📁 Structure

```
phishguard/
├── src/
│   ├── __init__.py
│   └── detector.py        # Core engine (URL, Email, Content analyzers)
├── tests/
│   └── test_detector.py   # 25 tests
├── cli.py                 # CLI tool
├── requirements.txt
└── README.md
```

## 📄 License

MIT License — see [LICENSE](LICENSE)
