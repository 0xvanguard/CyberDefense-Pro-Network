<div align="center">

# ⚡ ThreatSim

### Synthetic Attack Scenario Generator

![Version](https://img.shields.io/badge/version-1.0.0-blue)
![Python](https://img.shields.io/badge/python-3.8+-green)
![License](https://img.shields.io/badge/license-MIT-yellow)
![Scenarios](https://img.shields.io/badge/scenarios-1000+-red)

**Generate realistic attack scenarios** for training, testing, and validation.

[ThreatSim](https://github.com/0xvanguard/threatsim) • [Try It Live](#quick-start) • [Scenarios](#scenario-types)

</div>

---

## ⚡ What is ThreatSim?

ThreatSim is a **synthetic attack scenario generator** that creates realistic attack narratives for training security teams, testing defenses, and validating incident response procedures.

### Why ThreatSim?

| Without ThreatSim | With ThreatSim |
|-------------------|----------------|
| Generic attack scenarios | **Realistic, specific scenarios** |
| Manual scenario creation | **Automated generation** |
| Limited variety | **1000+ scenario templates** |
| No progression | **Adaptive difficulty** |

## 🎯 Scenario Types

| Category | Scenarios | Complexity |
|----------|-----------|------------|
| **Ransomware** | 150+ | High |
| **APT** | 120+ | Critical |
| **Insider Threat** | 100+ | High |
| **Supply Chain** | 80+ | Critical |
| **DDoS** | 90+ | Medium |
| **Social Engineering** | 110+ | Medium |
| **Data Exfiltration** | 100+ | High |
| **Zero Day** | 50+ | Critical |

## 🚀 Quick Start

```bash
# Install
pip install threatsim

# Or from source
git clone https://github.com/0xvanguard/threatsim.git
cd threatsim
pip install -e .
```

```python
from threatsim import ScenarioGenerator

generator = ScenarioGenerator()

# Generate scenario
scenario = generator.generate(
    category="ransomware",
    complexity="high",
    industry="healthcare"
)

print(f"Scenario: {scenario.title}")
print(f"MITRE: {scenario.mitre_techniques}")
print(f"Steps: {len(scenario.attack_steps)}")
```

## 💻 Advanced Generation

```python
from threatsim import AdvancedGenerator

generator = AdvancedGenerator()

# Generate training campaign
campaign = generator.create_campaign(
    name="Q4 Security Training",
    scenarios=20,
    categories=["ransomware", "insider"],
    difficulty_progression="gradual"
)

# Export for LMS
campaign.export_scorm("training_package.zip")

# Generate report
report = campaign.summary()
print(f"Total scenarios: {report.total}")
print(f"Avg complexity: {report.avg_complexity}")
```

## 📊 Scenario Details

| Field | Description |
|-------|-------------|
| **Title** | Descriptive scenario name |
| **MITRE Techniques** | Mapped attack techniques |
| **Attack Steps** | Detailed attack progression |
| **Indicators** | IOCs for detection |
| **Mitigations** | Defense recommendations |
| **Difficulty** | Complexity rating |

## 📁 Project Structure

```
threatsim/
├── src/
│   ├── __init__.py
│   └── generator.py           # Core generation engine
├── data/
│   ├── scenarios.json         # Scenario templates
│   └── techniques.json        # MITRE techniques
├── examples/
│   └── quick_generate.py      # Getting started
└── README.md
```

## 📄 License

MIT License — Generate threats.

---

<div align="center">

**Built by [@0xvanguard](https://github.com/0xvanguard)** • [⭐ Star this repo](https://github.com/0xvanguard/threatsim) • [🐛 Report Bug](https://github.com/0xvanguard/threatsim/issues)

</div>
