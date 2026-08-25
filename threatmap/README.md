<div align="center">

# 🌍 ThreatMap

### Real-Time Threat Intelligence Map with OSINT Data

![Version](https://img.shields.io/badge/version-1.0.0-blue)
![Python](https://img.shields.io/badge/python-3.8+-green)
![License](https://img.shields.io/badge/license-MIT-yellow)
![Feeds](https://img.shields.io/badge/feeds-20+-red)

**Visualize global threats in real-time** with OSINT data and threat intelligence.

[ThreatMap](https://github.com/0xvanguard/threatmap) • [Try It Live](#quick-start) • [Feeds](#threat-feeds)

</div>

---

## 🌍 What is ThreatMap?

ThreatMap is a **real-time threat intelligence map** that aggregates data from multiple OSINT feeds and displays global threats on an interactive map.

### Why ThreatMap?

| Without ThreatMap | With ThreatMap |
|-------------------|----------------|
| Scattered threat data | **Aggregated view** |
| No visualization | **Interactive map** |
| Manual correlation | **Automated analysis** |
| No real-time updates | **Live threat feed** |

## 📡 Threat Feeds

| Feed | Type | Update Frequency |
|------|------|------------------|
| **Abuse.ch** | Malware C2 | Real-time |
| **VirusTotal** | File/URL reputation | 5 min |
| **Shodan** | Internet scans | 15 min |
| **CIRCL** | DNS abuse | 30 min |
| **PhishTank** | Phishing URLs | 1 hour |
| **AlienVault OTX** | Threat intel | 5 min |

## 🚀 Quick Start

```bash
# Install
pip install threatmap

# Or from source
git clone https://github.com/0xvanguard/threatmap.git
cd threatmap
pip install -e .
```

```python
from threatmap import ThreatMap

# Create threat map
map = ThreatMap()

# Start live feed
map.start(port=8080)

# Access at http://localhost:8080
```

## 💻 API Usage

```python
from threatmap import ThreatAPI

api = ThreatAPI()

# Get current threats
threats = api.get_threats(
    region="north-america",
    type="malware",
    hours=24
)

# Get threat stats
stats = api.get_stats()
print(f"Active threats: {stats.active}")
print(f"New today: {stats.today}")

# Get specific IOCs
iocs = api.get_iocs(type="ip", limit=100)
```

## 📊 Dashboard Features

| Feature | Description |
|---------|-------------|
| **Live Map** | Real-time threat visualization |
| **Heatmap** | Threat density by region |
| **Timeline** | Threat activity over time |
| **Filters** | By type, severity, region |
| **Export** | Download threat data |

## 📁 Project Structure

```
threatmap/
├── src/
│   ├── __init__.py
│   └── map.py                 # Core map engine
├── data/
│   ├── feeds.json             # Threat feed sources
│   └── countries.json         # Country boundaries
├── dashboard/
│   └── index.html             # Web dashboard
├── examples/
│   └── quick_start.py         # Getting started
└── README.md
```

## 📄 License

MIT License — Visualize threats.

---

<div align="center">

**Built by [@0xvanguard](https://github.com/0xvanguard)** • [⭐ Star this repo](https://github.com/0xvanguard/threatmap) • [🐛 Report Bug](https://github.com/0xvanguard/threatmap/issues)

</div>
