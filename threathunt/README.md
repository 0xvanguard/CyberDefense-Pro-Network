<p align="center">
  <img src="https://img.shields.io/badge/version-2.0.0-blue?style=for-the-badge">
  <img src="https://img.shields.io/badge/python-3.10+-yellow?style=for-the-badge&logo=python&logoColor=white">
  <img src="https://img.shields.io/badge/license-MIT-green?style=for-the-badge">
  <img src="https://img.shields.io/badge/tests-24-passing-brightgreen?style=for-the-badge">
  <img src="https://img.shields.io/github/stars/0xvanguard/threathunt?style=for-the-badge">
</p>

# 🔍 ThreatHunt

**AI-Powered Automated Threat Hunting — MITRE ATT&CK mapped.**

ThreatHunt proactively searches for hidden threats using behavioral analysis, anomaly detection, beaconing detection, and MITRE ATT&CK framework mapping. Includes 12 built-in hunt queries covering lateral movement, credential dumping, C2 beaconing, ransomware, and more.

## ✨ Features

| Feature | Description |
|---------|-------------|
| **12 Hunt Queries** | Pre-built MITRE-mapped detection rules |
| **MITRE ATT&CK** | 12 tactics, 12 techniques mapped |
| **Beaconing Detection** | Periodic C2 communication analysis |
| **Anomaly Detection** | Z-score based anomaly scoring |
| **IoC Matching** | Load and match against IoC feeds |
| **Multi-Format Export** | JSON, STIX, CSV, Markdown |
| **Demo Data** | Synthetic events for testing |
| **Custom Hunts** | Add your own detection queries |

## 🚀 Quick Start

```bash
pip install -r requirements.txt

# Run threat hunt
python cli.py hunt

# List hunt queries
python cli.py queries

# View MITRE tactics
python cli.py tactics

# View MITRE techniques
python cli.py techniques

# Export findings
python cli.py export --format markdown --output report.md

# Summary
python cli.py summary
```

## 🐍 Python API

```python
from src.hunter import ThreatHunter, IoC

hunter = ThreatHunter(data_sources=["all"])

# Add IoCs
hunter.add_ioc(IoC(type="ip", value="10.0.0.1", confidence=0.9))

# Run hunt
result = hunter.hunt(timeframe="24h")
print(f"Findings: {len(result.findings)}")

# Export
print(hunter.export(format="markdown"))
```

## 🎯 MITRE ATT&CK Coverage

| Tactic | Technique | Hunt Query |
|--------|-----------|------------|
| Initial Access | T1078 | Stolen credentials |
| Initial Access | T1190 | App exploitation |
| Execution | T1059 | PowerShell abuse |
| Persistence | T1053 | Scheduled tasks |
| Defense Evasion | T1027 | Obfuscated payloads |
| Credential Access | T1003 | Credential dumping |
| Discovery | T1082 | System enumeration |
| Lateral Movement | T1021 | Remote services |
| C2 | T1071 | Beaconing detection |
| C2 | T1105 | Tool transfer |
| Exfiltration | T1048 | DNS tunneling |
| Impact | T1486 | Ransomware encryption |

## 📁 Structure

```
threathunt/
├── src/
│   ├── __init__.py
│   └── hunter.py           # Core engine
├── tests/
│   └── test_hunter.py      # 24 tests
├── cli.py                  # CLI tool
├── requirements.txt
└── README.md
```

## 📄 License

MIT License — see [LICENSE](LICENSE)
