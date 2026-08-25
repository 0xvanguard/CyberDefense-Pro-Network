<div align="center">

# 🎯 ThreatModeler

### Visual Threat Modeling with STRIDE Classification

![Version](https://img.shields.io/badge/version-1.0.0-blue)
![Python](https://img.shields.io/badge/python-3.8+-green)
![License](https://img.shields.io/badge/license-MIT-yellow)
![Framework](https://img.shields.io/badge/framework-STRIDE-purple)

**Visual drag-and-drop threat modeling** with automated STRIDE classification.

[ThreatModeler](https://github.com/0xvanguard/threatmodeler) • [Try It Live](#quick-start) • [Features](#features)

</div>

---

## 🎯 What is ThreatModeler?

ThreatModeler is a **visual threat modeling tool** that helps identify and classify threats using the STRIDE framework with drag-and-drop interface.

### Why ThreatModeler?

| Without ThreatModeler | With ThreatModeler |
|-----------------------|-------------------|
| Text-based models | **Visual diagrams** |
| Manual classification | **Automated STRIDE** |
| No mitigation | **Auto-generated mitigations** |
| Hard to collaborate | **Shareable models** |

## 🎯 STRIDE Categories

| Category | Description | Mitigation |
|----------|-------------|------------|
| **Spoofing** | Identity impersonation | Authentication |
| **Tampering** | Data modification | Integrity checks |
| **Repudiation** | Denying actions | Audit logging |
| **Information Disclosure** | Data exposure | Encryption |
| **Denial of Service** | Availability attacks | Redundancy |
| **Elevation of Privilege** | Unauthorized access | Access control |

## 🚀 Quick Start

```bash
# Install
pip install threatmodeler

# Start visual editor
threatmodeler serve --port 8080
```

## 💻 Programmatic Usage

```python
from threatmodeler import ThreatModel

model = ThreatModel()

# Add components
model.add_component("web_app", type="process")
model.add_component("database", type="datastore")
model.add_component("user", type="external_entity")

# Add data flows
model.add_flow("user", "web_app", "HTTP Request")
model.add_flow("web_app", "database", "SQL Query")

# Analyze threats
threats = model.analyze()
print(f"Found {len(threats)} threats")

# Get mitigations
for threat in threats:
    print(f"{threat.category}: {threat.mitigation}")
```

## 📊 Model Export

```python
from threatmodeler import Exporter

exporter = Exporter(model)

# Export as diagram
exporter.export_diagram("threat_model.png")

# Export as report
exporter.export_report("threat_report.pdf")

# Export as JSON
exporter.export_json("threat_model.json")
```

## 📁 Project Structure

```
threatmodeler/
├── src/
│   ├── __init__.py
│   └── modeler.py             # Core modeling engine
├── data/
│   └── stride.json            # STRIDE definitions
├── examples/
│   └── quick_model.py         # Getting started
└── README.md
```

## 📄 License

MIT License — Model threats.

---

<div align="center">

**Built by [@0xvanguard](https://github.com/0xvanguard)** • [⭐ Star this repo](https://github.com/0xvanguard/threatmodeler) • [🐛 Report Bug](https://github.com/0xvanguard/threatmodeler/issues)

</div>
