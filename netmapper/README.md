<p align="center">
  <img src="https://img.shields.io/badge/version-2.0.0-blue?style=for-the-badge">
  <img src="https://img.shields.io/badge/python-3.10+-yellow?style=for-the-badge&logo=python&logoColor=white">
  <img src="https://img.shields.io/badge/license-MIT-green?style=for-the-badge">
  <img src="https://img.shields.io/badge/tests-20-passing-brightgreen?style=for-the-badge">
  <img src="https://img.shields.io/github/stars/0xvanguard/netmapper?style=for-the-badge">
</p>

# 🔍 NetMapper

**Network Scanner & Topology Mapper — Discover hosts, ports, services, and vulnerabilities.**

NetMapper scans network ranges to discover active hosts, open ports, running services, and potential vulnerabilities. It maps network topology, fingerprints operating systems, grabs service banners, and identifies known risky configurations.

## ✨ Features

| Feature | Description |
|---------|-------------|
| **Host Discovery** | Find active hosts via multi-port probing |
| **Port Scanning** | 24+ common ports with service detection |
| **OS Fingerprinting** | Guess OS from open port patterns |
| **Banner Grabbing** | Extract service version information |
| **Vulnerability Check** | 14 known vulnerable service patterns |
| **Risk Assessment** | Per-port risk levels (low–critical) |
| **Topology Mapping** | Full network topology with JSON export |
| **Service Statistics** | Top services and OS distribution |

## 🚀 Quick Start

```bash
pip install -r requirements.txt

# Scan a network
python cli.py scan 192.168.1.0/24

# Scan specific ports
python cli.py scan 10.0.0.1 --ports 22,80,443

# Scan single host
python cli.py host 192.168.1.1

# Show known vulnerable services
python cli.py vulns

# Export topology
python cli.py scan 192.168.1.0/24 --output topology.json
```

## 🐍 Python API

```python
from src.scanner import NetworkMapper

mapper = NetworkMapper(target="192.168.1.0/24", timeout=1.0)
topology = mapper.scan()

print(f"Active hosts: {topology.active_hosts}")
print(f"Open ports: {topology.total_open_ports}")
print(f"Vulnerabilities: {topology.total_vulnerabilities}")

for host in topology.hosts:
    if host.status.value == "up":
        print(f"{host.ip} — {host.os_guess}")
        for v in host.vulnerabilities:
            print(f"  ⚠️  {v['service']}: {v['issue']}")
```

## 📁 Structure

```
netmapper/
├── src/
│   ├── __init__.py
│   └── scanner.py           # Core engine
├── tests/
│   └── test_scanner.py      # 20 tests
├── cli.py                   # CLI tool
├── requirements.txt
└── README.md
```

## 📄 License

MIT License — see [LICENSE](LICENSE)
