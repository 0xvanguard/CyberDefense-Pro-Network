<div align="center">

# 🔒 PrivacyVPN

### Open Source VPN with WireGuard

![Version](https://img.shields.io/badge/version-1.0.0-blue)
![Python](https://img.shields.io/badge/python-3.8+-green)
![License](https://img.shields.io/badge/license-GPL--3.0-yellow)
![Protocol](https://img.shields.io/badge/protocol-WireGuard-green)

**Browse privately** with open source VPN powered by WireGuard.

[PrivacyVPN](https://github.com/0xvanguard/privacyvpn) • [Try It Live](#quick-start) • [Features](#features)

</div>

---

## 🔒 What is PrivacyVPN?

PrivacyVPN is an **open source VPN** built on WireGuard protocol for fast, secure, and private internet access.

### Why PrivacyVPN?

| Without PrivacyVPN | With PrivacyVPN |
|--------------------|-----------------|
| Unencrypted traffic | **Encrypted connection** |
| No privacy | **No-logs policy** |
| Slow VPN | **WireGuard speed** |
| Closed source | **Open source** |

## ⚡ Features

| Feature | Description |
|---------|-------------|
| **WireGuard Protocol** | Fast, modern VPN |
| **No-Logs Policy** | We don't track you |
| **Open Source** | Fully transparent |
| **Multi-platform** | Windows, Mac, Linux, Mobile |
| **Kill Switch** | Protect if VPN drops |

## 🚀 Quick Start

```bash
# Install
pip install privacyvpn

# Connect
privacyvpn connect --server us-east
```

## 💻 Programmatic Usage

```python
from privacyvpn import VPN

vpn = VPN()

# List servers
servers = vpn.list_servers(region="north-america")
print(f"Found {len(servers)} servers")

# Connect
connection = vpn.connect(server=servers[0])
print(f"Connected to {connection.server}")
print(f"IP: {connection.ip}")

# Disconnect
vpn.disconnect()
```

## 📁 Project Structure

```
privacyvpn/
├── src/
│   ├── __init__.py
│   └── vpn.py                 # Core VPN engine
├── data/
│   └── servers.json           # Server list
├── examples/
│   └── quick_connect.py       # Getting started
└── README.md
```

## 📄 License

GPL-3.0 — Open source VPN.

---

<div align="center">

**Built by [@0xvanguard](https://github.com/0xvanguard)** • [⭐ Star this repo](https://github.com/0xvanguard/privacyvpn) • [🐛 Report Bug](https://github.com/0xvanguard/privacyvpn/issues)

</div>
