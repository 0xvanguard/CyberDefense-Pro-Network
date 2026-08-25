<div align="center">

# 📊 RiskCalculator

### CVSS and FAIR Risk Quantification Calculator

![Version](https://img.shields.io/badge/version-1.0.0-blue)
![Python](https://img.shields.io/badge/python-3.8+-green)
![License](https://img.shields.io/badge/license-MIT-yellow)
![Frameworks](https://img.shields.io/badge/frameworks-CVSS%20FAIR-purple)

**Calculate and visualize risk** with industry-standard frameworks.

[RiskCalculator](https://github.com/0xvanguard/riskcalculator) • [Try It Live](#quick-start) • [Frameworks](#risk-frameworks)

</div>

---

## 📊 What is RiskCalculator?

RiskCalculator is a **risk quantification tool** that implements CVSS v3.1 and FAIR frameworks to calculate, visualize, and report security risks.

### Why RiskCalculator?

| Without RiskCalculator | With RiskCalculator |
|------------------------|---------------------|
| Subjective risk assessment | **Quantified scores** |
| No standardized framework | **CVSS/FAIR compliant** |
| Manual calculations | **Automated scoring** |
| No visualization | **Visual risk reports** |

## 🎯 Risk Frameworks

| Framework | Description | Use Case |
|-----------|-------------|----------|
| **CVSS v3.1** | Vulnerability scoring | CVE prioritization |
| **FAIR** | Risk quantification | Business risk analysis |
| **DREAD** | Damage, Reproducibility | Quick assessment |
| **OWASP Risk** | Web application risk | AppSec |

## 🚀 Quick Start

```bash
# Install
pip install riskcalculator

# Or from source
git clone https://github.com/0xvanguard/riskcalculator.git
cd riskcalculator
pip install -e .
```

```python
from riskcalculator import CVSSCalculator, FAIRCalculator

# CVSS v3.1 Calculation
cvss = CVSSCalculator()

score = cvss.calculate({
    "attack_vector": "network",
    "attack_complexity": "low",
    "privileges_required": "none",
    "user_interaction": "none",
    "scope": "changed",
    "confidentiality": "high",
    "integrity": "high",
    "availability": "high"
})

print(f"Score: {score.vector}")
print(f"Severity: {score.severity}")
print(f"Base: {score.base}")

# FAIR Calculation
fair = FAIRCalculator()

risk = fair.calculate({
    "threat_event_frequency": 1000,
    "vulnerability": 0.1,
    "loss_magnitude": 50000
})

print(f"Expected Loss: ${risk.expected_loss:,.0f}")
print(f"Risk Score: {risk.score}")
```

## 📊 Risk Visualization

```python
from riskcalculator import Visualizer

viz = Visualizer()

# Create risk matrix
viz.risk_matrix(
    vulnerabilities=vulns,
    output="risk_matrix.html"
)

# Create risk timeline
viz.risk_timeline(
    history=risk_history,
    output="risk_timeline.html"
)

# Export report
viz.export_report(
    format="pdf",
    output="risk_report.pdf"
)
```

## 📈 Metrics

| Metric | CVSS | FAIR |
|--------|------|------|
| **Score Range** | 0-10 | 0-100 |
| **Severity Levels** | 5 | 5 |
| **Temporal** | ✅ | ✅ |
| **Environmental** | ✅ | ✅ |
| **Monetary** | ❌ | ✅ |

## 📁 Project Structure

```
riskcalculator/
├── src/
│   ├── __init__.py
│   └── calculator.py          # Core calculator
├── data/
│   ├── cvss_metrics.json      # CVSS metrics
│   └── fair_parameters.json   # FAIR parameters
├── examples/
│   └── quick_calculate.py     # Getting started
└── README.md
```

## 📄 License

MIT License — Calculate risk.

---

<div align="center">

**Built by [@0xvanguard](https://github.com/0xvanguard)** • [⭐ Star this repo](https://github.com/0xvanguard/riskcalculator) • [🐛 Report Bug](https://github.com/0xvanguard/riskcalculator/issues)

</div>
