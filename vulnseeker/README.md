<div align="center">

# 🔍 VulnSeeker

### Smart CVE Search with Risk Context and Exploit Availability

![Version](https://img.shields.io/badge/version-1.0.0-blue)
![Python](https://img.shields.io/badge/python-3.8+-green)
![License](https://img.shields.io/badge/license-MIT-yellow)
![CVEs](https://img.shields.io/badge/CVEs-200000+-red)

**Search, analyze, and prioritize vulnerabilities** with context-aware results.

[VulnSeeker](https://github.com/0xvanguard/vulnseeker) • [Try It Live](#quick-start) • [Features](#features)

</div>

---

## 🔍 What is VulnSeeker?

VulnSeeker is a **smart CVE search engine** that provides context-aware vulnerability information including exploit availability, risk scoring, and remediation guidance.

### Why VulnSeeker?

| Without VulnSeeker | With VulnSeeker |
|--------------------|-----------------|
| Raw CVE data | **Context-rich results** |
| No exploit info | **Exploit availability** |
| Manual prioritization | **Risk-based scoring** |
| No remediation | **Fix recommendations** |

## 🔍 Features

| Feature | Description | Data Source |
|---------|-------------|-------------|
| **CVE Search** | Search by keyword, CVE ID | NVD, MITRE |
| **Exploit Check** | Check for public exploits | ExploitDB, GitHub |
| **Risk Scoring** | CVSS + context scoring | NVD, First.org |
| **Remediation** | Fix recommendations | NVD, Vendor advisories |
| **Trending** | Top vulnerabilities | Real-time analysis |

## 🚀 Quick Start

```bash
# Install
pip install vulnseeker

# Or from source
git clone https://github.com/0xvanguard/vulnseeker.git
cd vulnseeker
pip install -e .
```

```python
from vulnseeker import VulnSearch

searcher = VulnSearch()

# Search CVEs
results = searcher.search("apache log4j")

for vuln in results[:5]:
    print(f"{vuln.cve_id}: {vuln.severity}")
    print(f"  CVSS: {vuln.cvss_score}")
    print(f"  Exploits: {vuln.exploit_count}")
    print(f"  Fix: {vuln.remediation[:50]}...")
```

## 💻 Advanced Search

```python
from vulnseeker import AdvancedSearch

searcher = AdvancedSearch()

# Filter by severity
critical = searcher.filter(severity="CRITICAL", year=2024)

# Check specific software
vulns = searcher.check_software("nginx", "1.21.0")
print(f"Found {len(vulns)} vulnerabilities")

# Get exploit details
for vuln in vulns:
    if vuln.has_exploit:
        exploit = searcher.get_exploit(vuln.cve_id)
        print(f"Exploit: {exploit.url}")
```

## 📊 Risk Report

```python
from vulnseeker import RiskReport

report = RiskReport()

# Generate risk report for software stack
risk = report.analyze({
    "nginx": "1.21.0",
    "openssl": "1.1.1",
    "python": "3.9"
})

print(f"Overall risk: {risk.score}/100")
print(f"Critical vulns: {risk.critical}")
print(f"Recommendations: {len(risk.recommendations)}")
```

## 📁 Project Structure

```
vulnseeker/
├── src/
│   ├── __init__.py
│   └── vulnseeker.py          # Core search engine
├── data/
│   ├── cves.json              # CVE database
│   └── exploits.json          # Exploit database
├── examples/
│   └── quick_search.py        # Getting started
└── README.md
```

## 📄 License

MIT License — Seek vulnerabilities.

---

<div align="center">

**Built by [@0xvanguard](https://github.com/0xvanguard)** • [⭐ Star this repo](https://github.com/0xvanguard/vulnseeker) • [🐛 Report Bug](https://github.com/0xvanguard/vulnseeker/issues)

</div>
