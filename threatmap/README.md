<p align="center">
  <img src="https://img.shields.io/badge/version-2.0.0-blue?style=for-the-badge">
  <img src="https://img.shields.io/badge/python-3.10+-yellow?style=for-the-badge&logo=python&logoColor=white">
  <img src="https://img.shields.io/badge/license-MIT-green?style=for-the-badge">
  <img src="https://img.shields.io/github/stars/0xvanguard/threatmap?style=for-the-badge">
</p>

# 🗺️ ThreatMap

**Real-time threat intelligence visualization and OSINT aggregation platform.**

ThreatMap aggregates threat indicators from multiple OSINT sources (Abuse.ch, VirusTotal, Shodan, OTX, GreyNoise, CISA KEV), geolocates them, and generates comprehensive threat reports. It correlates indicators across sources and maps global threat landscape.

## ✨ Features

| Feature | Description |
|---------|-------------|
| **Multi-Source Aggregation** | Pull from 8+ OSINT sources |
| **Indicator Types** | IP, domain, URL, hash, email |
| **Geolocation** | Map indicators to countries/cities |
| **Correlation** | Link indicators across sources |
| **Risk Scoring** | Confidence-weighted threat scoring |
| **CLI Tool** | Full-featured command line interface |
| **Export** | JSON, CSV, Markdown reports |
| **Local DB** | SQLite cache for fast queries |

## 🚀 Quick Start

```bash
# Install dependencies
pip install -r requirements.txt

# Run CLI
python cli.py sources              # List all sources
python cli.py stats                # Show statistics
python cli.py recent --hours 24    # Recent indicators
python cli.py country US           # Indicators by country
python cli.py search "cobalt"      # Search indicators
python cli.py type ip              # Filter by type
python cli.py threat c2_server     # Filter by threat
python cli.py export --output report.json
```

## 🐍 Python API

```python
from src.map import ThreatMapEngine, ThreatIntelSource, ThreatIndicator

engine = ThreatMapEngine()

# Generate report
report = engine.generate_report(time_range="30d")
print(f"Total indicators: {report.summary['total_indicators']}")

# Filter indicators
c2_ips = engine.filter_indicators(indicator_type="ip", threat_type="c2_server")

# Search
results = engine.search("ransomware")

# Geolocate
geo = engine.geolocate("8.8.8.8")
print(f"{geo.city}, {geo.country}")
```

## 📁 Structure

```
threatmap/
├── src/
│   ├── __init__.py
│   └── map.py              # Core engine
├── tests/
│   └── test_map.py         # 16 tests
├── cli.py                   # CLI tool
├── requirements.txt
└── README.md
```

## 📄 License

MIT License — see [LICENSE](LICENSE)
