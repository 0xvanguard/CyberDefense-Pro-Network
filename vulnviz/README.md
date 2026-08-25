<div align="center">

# 📈 VulnViz

### Interactive Vulnerability Visualizer and Graph Explorer

![Version](https://img.shields.io/badge/version-1.0.0-blue)
![Python](https://img.shields.io/badge/python-3.8+-green)
![License](https://img.shields.io/badge/license-MIT-yellow)
![Graphs](https://img.shields.io/badge/graphs-interactive-red)

**Visualize vulnerabilities** with interactive graphs and dependency mapping.

[VulnViz](https://github.com/0xvanguard/vulnviz) • [Try It Live](#quick-start) • [Features](#features)

</div>

---

## 📈 What is VulnViz?

VulnViz is an **interactive vulnerability visualizer** that creates visual dependency graphs and vulnerability maps for software projects.

### Why VulnViz?

| Without VulnViz | With VulnViz |
|-----------------|--------------|
| Text-based reports | **Visual graphs** |
| No dependency view | **Dependency mapping** |
| Hard to prioritize | **Visual prioritization** |
| No relationship view | **Relationship graphs** |

## 🎯 Features

| Feature | Description |
|---------|-------------|
| **Dependency Graph** | Visualize package dependencies |
| **Vulnerability Map** | Show vulnerable components |
| **Risk Heatmap** | Color-coded risk levels |
| **Interactive Explorer** | Click to drill down |
| **Export Formats** | PNG, SVG, JSON, PDF |

## 🚀 Quick Start

```bash
# Install
pip install vulnviz

# Visualize vulnerabilities
vulnviz scan --project ./my-app --output graph.html
```

## 💻 Programmatic Usage

```python
from vulnviz import VulnerabilityVisualizer

viz = VulnerabilityVisualizer()

# Scan project
graph = viz.scan("./my-app")

# Create visualization
viz.create_graph(
    graph,
    output="vulnerability_graph.html",
    layout="force",
    color_by="severity"
)

# Get stats
print(f"Total dependencies: {graph.total_deps}")
print(f"Vulnerable: {graph.vulnerable}")
print(f"Risk score: {graph.risk_score}")
```

## 📊 Visualization Options

```python
from vulnviz import Visualizer

viz = Visualizer()

# Dependency graph
viz.dependency_graph(project, "deps.html")

# Vulnerability heatmap
viz.vulnerability_heatmap(project, "heatmap.html")

# Risk timeline
viz.risk_timeline(history, "timeline.html")

# Combined view
viz.dashboard(project, "dashboard.html")
```

## 📁 Project Structure

```
vulnviz/
├── src/
│   ├── __init__.py
│   └── vulnviz.py             # Core visualizer
├── data/
│   └── dependencies.json      # Dependency data
├── examples/
│   └── quick_scan.py          # Getting started
└── README.md
```

## 📄 License

MIT License — Visualize vulnerabilities.

---

<div align="center">

**Built by [@0xvanguard](https://github.com/0xvanguard)** • [⭐ Star this repo](https://github.com/0xvanguard/vulnviz) • [🐛 Report Bug](https://github.com/0xvanguard/vulnviz/issues)

</div>
