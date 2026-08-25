<div align="center">

# 🔍 ThreatHunt

### Automated Threat Hunting with AI and MITRE ATT&CK

![Version](https://img.shields.io/badge/version-1.0.0-blue)
![Python](https://img.shields.io/badge/python-3.8+-green)
![License](https://img.shields.io/badge/license-MIT-yellow)
![MITRE](https://img.shields.io/badge/MITRE-ATT%26CK-purple)

**Proactively hunt for hidden threats** with behavioral analysis and MITRE ATT&CK mapping.

[ThreatHunt](https://github.com/0xvanguard/threathunt) • [Try It Live](#quick-start) • [Hunts](#hunt-queries)

</div>

---

## 🔍 What is ThreatHunt?

ThreatHunt is an **AI-powered threat hunting engine** that proactively searches for hidden threats using behavioral analysis, anomaly detection, and MITRE ATT&CK framework mapping.

### Why ThreatHunt?

| Without ThreatHunt | With ThreatHunt |
|--------------------|-----------------|
| Reactive detection | **Proactive hunting** |
| No MITRE mapping | **ATT&CK alignment** |
| Manual correlation | **Automated analysis** |
| Unknown threats | **Behavioral detection** |

## 🎯 Hunt Queries

| Hunt | MITRE ID | Description | Detection Rate |
|------|----------|-------------|----------------|
| **Lateral Movement** | T1021 | SMB/SSH lateral movement | 92% |
| **Persistence** | T1053 | Scheduled task creation | 88% |
| **Exfiltration** | T1048 | DNS tunneling detection | 94% |
| **Credential Dumping** | T1003 | LSASS access detection | 96% |
| **C2 Beaconing** | T1071 | Periodic beacon detection | 91% |
| **Ransomware** | T1486 | Mass file encryption | 98% |

## 🚀 Quick Start

```bash
# Install
pip install threathunt

# Or from source
git clone https://github.com/0xvanguard/threathunt.git
cd threathunt
pip install -e .
```

```python
from threathunt import ThreatHunter

hunter = ThreatHunter(data_sources=["syslog", "dns", "netflow"])

# Run hunt
findings = hunter.hunt(timeframe="24h")

print(f"Total findings: {len(findings)}")
for finding in findings:
    print(f"{finding.technique}: {finding.description}")
    print(f"  Confidence: {finding.confidence:.0%}")
    print(f"  Severity: {finding.severity.value}")
```

## 💻 Advanced Hunting

```python
from threathunt import ThreatHunter, HuntQuery

hunter = ThreatHunter()

# Add custom hunt
custom_hunt = HuntQuery(
    name="custom-detection",
    mitre_technique="T1059",
    mitre_tactic="TA0002",
    description="Detect suspicious PowerShell",
    severity="high"
)
hunter.add_hunt(custom_hunt)

# Load IoCs
hunter.load_iocs("threat_intel.json")

# Run hunt
results = hunter.hunt(timeframe="7d")

# Export
hunter.export(results, format="stix")
hunter.export(results, format="markdown", output="hunt_report.md")
```

## 📊 Hunt Report

| Metric | Value |
|--------|-------|
| **Timeframe** | 24 hours |
| **Queries Run** | 12 |
| **Findings** | 8 |
| **Critical** | 2 |
| **High** | 3 |
| **Medium** | 3 |
| **IoCs Found** | 15 |

## 📁 Project Structure

```
threathunt/
├── src/
│   ├── __init__.py
│   └── hunter.py              # Core hunting engine
├── data/
│   ├── hunts.json             # Hunt queries
│   └── mitre.json             # MITRE ATT&CK mappings
├── examples/
│   └── quick_hunt.py          # Getting started
└── README.md
```

## 📄 License

MIT License — Hunt threats.

---

<div align="center">

**Built by [@0xvanguard](https://github.com/0xvanguard)** • [⭐ Star this repo](https://github.com/0xvanguard/threathunt) • [🐛 Report Bug](https://github.com/0xvanguard/threathunt/issues)

</div>
