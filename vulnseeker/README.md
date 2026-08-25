<div align="center">

# 🔍 VulnSeeker

### Smart CVE Search Engine with Risk Context

![Version](https://img.shields.io/badge/version-2.0.0-blue)
![Python](https://img.shields.io/badge/python-3.8+-green)
![License](https://img.shields.io/badge/license-MIT-yellow)
![API](https://img.shields.io/badge/API-NVD-red)
![CVEs](https://img.shields.io/badge/CVEs-200000+-purple)

**Search, analyze, and prioritize vulnerabilities** with context-aware results from NVD, CISA KEV, and EPSS.

[PromptKiller](https://github.com/0xvanguard/vulnseeker) • [Quick Start](#quick-start) • [CLI](#cli-usage)

</div>

---

## 🔍 What is VulnSeeker?

VulnSeeker is a **smart CVE search engine** that provides context-rich vulnerability information including:

- **Real-time NVD API integration** — Search 200,000+ CVEs
- **CISA KEV correlation** — Know which CVEs are actively exploited
- **EPSS scoring** — Predict exploitation probability
- **Risk analysis** — Automated risk assessment with recommendations
- **Export capabilities** — JSON, CSV, Markdown

## 🚀 Quick Start

```bash
# Clone
git clone https://github.com/0xvanguard/vulnseeker.git
cd vulnseeker

# Install
pip install -e .

# Search
python cli.py search "apache log4j"

# Get CVE details
python cli.py get CVE-2021-44228

# Analyze risk
python cli.py analyze CVE-2021-44228

# Recent CVEs
python cli.py recent --days 7

# Product search
python cli.py product nginx

# Critical CVEs
python cli.py critical
```

## 💻 Python API

```python
from vulnseeker import VulnSeeker

vs = VulnSeeker()

# Search
results = vs.search("apache log4j", min_cvss=7.0)
for cve in results.cves:
    print(f"{cve.id}: CVSS {cve.cvss_score} — {cve.risk_level}")

# Get specific CVE
cve = vs.get_cve("CVE-2021-44228")
print(f"KEV: {cve.in_kev}")
print(f"Exploit: {cve.exploit_available}")

# Risk analysis
analysis = vs.analyze_risk("CVE-2021-44228")
print(f"Risk: {analysis.risk_level}")
print(f"Exploitability: {analysis.exploitability}")
for rec in analysis.recommendations:
    print(f"  - {rec}")

# Export
vs.export(results.cves, "report.json", format="json")
vs.export(results.cves, "report.csv", format="csv")
vs.export(results.cves, "report.md", format="markdown")
```

## 📊 Features

| Feature | Description |
|---------|-------------|
| **CVE Search** | Full-text search across NVD database |
| **Risk Analysis** | CVSS + EPSS + KEV context |
| **Product Lookup** | Find CVEs affecting specific software |
| **KEV Correlation** | CISA Known Exploited Vulnerabilities |
| **Export** | JSON, CSV, Markdown formats |
| **Caching** | Local cache for faster repeated queries |
| **CLI** | Full-featured command line interface |

## 🛡️ Risk Levels

| Level | CVSS | KEV | Exploit | Action |
|-------|------|-----|---------|--------|
| **CRITICAL** | 9.0+ | Yes | Available | Patch immediately |
| **HIGH** | 7.0-8.9 | Possible | Available | Patch within 24h |
| **MEDIUM** | 4.0-6.9 | No | Possible | Patch within 7 days |
| **LOW** | 0-3.9 | No | Unlikely | Patch when convenient |

## 📁 Project Structure

```
vulnseeker/
├── src/
│   ├── __init__.py
│   └── vulnseeker.py        # Core library (500+ lines)
├── tests/
│   ├── __init__.py
│   └── test_vulnseeker.py   # 11 tests
├── cli.py                   # CLI tool
├── requirements.txt
└── README.md
```

## 🧪 Tests

```bash
python -m pytest tests/ -v
```

## 📄 License

MIT License — Search vulnerabilities responsibly.

---

<div align="center">

**Built by [@0xvanguard](https://github.com/0xvanguard)** • [⭐ Star this repo](https://github.com/0xvanguard/vulnseeker) • [🐛 Report Bug](https://github.com/0xvanguard/vulnseeker/issues)

</div>
