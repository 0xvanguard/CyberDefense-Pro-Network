<div align="center">

# 🗺️ NetMapper

### Automated Network Mapping and Topology Visualization

![Version](https://img.shields.io/badge/version-1.0.0-blue)
![Python](https://img.shields.io/badge/python-3.8+-green)
![License](https://img.shields.io/badge/license-MIT-yellow)
![Speed](https://img.shields.io/badge/speed-fast-green)

**Discover and visualize your network** with automated scanning and topology mapping.

[NetMapper](https://github.com/0xvanguard/netmapper) • [Try It Live](#quick-start) • [Features](#features)

</div>

---

## 🗺️ What is NetMapper?

NetMapper is an **automated network mapping tool** that discovers devices, maps connections, and creates visual topology diagrams of your network infrastructure.

### Why NetMapper?

| Without NetMapper | With NetMapper |
|-------------------|----------------|
| Manual network discovery | **Automated scanning** |
| No visual topology | **Interactive diagrams** |
| Unknown devices | **Device fingerprinting** |
| Missing assets | **Complete inventory** |

## 🔍 Features

| Feature | Description | Speed |
|---------|-------------|-------|
| **Host Discovery** | Find all devices on network | 100 hosts/sec |
| **Port Scanning** | Open port detection | 1000 ports/sec |
| **Service Detection** | Identify services | 50 services/sec |
| **OS Fingerprinting** | Detect operating systems | 95% accuracy |
| **Topology Mapping** | Create visual diagrams | Real-time |

## 🚀 Quick Start

```bash
# Install
pip install netmapper

# Or from source
git clone https://github.com/0xvanguard/netmapper.git
cd netmapper
pip install -e .
```

```python
from netmapper import NetworkMapper

mapper = NetworkMapper()

# Scan network
topology = mapper.scan("192.168.1.0/24")

print(f"Hosts found: {len(topology.hosts)}")
print(f"Services: {len(topology.services)}")

# Export topology
topology.export("network_map.html")
topology.export("network_map.json")
```

## 💻 Visualization

```python
from netmapper import Visualizer

viz = Visualizer(topology)

# Create interactive map
viz.create_interactive(
    output="network_topology.html",
    layout="force",
    show_labels=True,
    color_by="os"
)

# Create static image
viz.create_static(
    output="network_topology.png",
    format="png",
    dpi=300
)
```

## 📊 Network Report

```python
from netmapper import ReportGenerator

report = ReportGenerator(topology)

# Generate report
report.generate(
    format="markdown",
    output="network_report.md",
    include_topology=True,
    include_vulnerabilities=True
)
```

## 📁 Project Structure

```
netmapper/
├── src/
│   ├── __init__.py
│   └── scanner.py             # Core scanning engine
├── data/
│   ├── os_fingerprints.json   # OS detection patterns
│   └── service_probes.json    # Service detection
├── examples/
│   └── quick_scan.py          # Getting started
└── README.md
```

## 📄 License

MIT License — Map your network.

---

<div align="center">

**Built by [@0xvanguard](https://github.com/0xvanguard)** • [⭐ Star this repo](https://github.com/0xvanguard/netmapper) • [🐛 Report Bug](https://github.com/0xvanguard/netmapper/issues)

</div>
