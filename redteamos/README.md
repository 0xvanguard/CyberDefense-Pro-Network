<div align="center">

# 🖥️ RedTeamOS

### Live Boot OS for AI Red Team Operations

![Version](https://img.shields.io/badge/version-1.0.0-blue)
![License](https://img.shields.io/badge/license-GPL--3.0-yellow)
![Size](https://img.shields.io/badge/size-2GB-red)
![Tools](https://img.shields.io/badge/tools-50+-purple)

**All-in-one live boot OS** for AI security testing, red teaming, and vulnerability assessment.

[RedTeamOS](https://github.com/0xvanguard/redteamos) • [Download](#installation) • [Tools](#included-tools)

</div>

---

## 🖥️ What is RedTeamOS?

RedTeamOS is a **purpose-built live boot operating system** for AI security researchers and red teamers. Boot from USB, connect to a network, and start testing immediately.

### Why RedTeamOS?

| Without RedTeamOS | With RedTeamOS |
|-------------------|----------------|
| Hours to set up tools | **Boot and go** |
| Inconsistent environments | **Standardized tools** |
| Missing dependencies | **Pre-configured** |
| Hard to share setups | **Portable USB** |

## 🔧 Included Tools

### AI Security Tools
| Tool | Purpose | Version |
|------|---------|---------|
| **PromptKiller** | Attack prompt library | 2.0.0 |
| **GuardDog** | Injection scanner | 1.3.0 |
| **LLMFuzz** | LLM fuzzer | 1.2.0 |
| **JailbreakBench** | Benchmark evaluation | 1.5.0 |

### Network Security Tools
| Tool | Purpose | Version |
|------|---------|---------|
| **Nmap** | Network scanning | 7.94 |
| **Wireshark** | Packet analysis | 4.2 |
| **Burp Suite** | Web application testing | 2024.1 |
| **Metasploit** | Exploitation framework | 6.3 |

### Forensics Tools
| Tool | Purpose | Version |
|------|---------|---------|
| **Volatility** | Memory forensics | 3.0 |
| **Autopsy** | Disk forensics | 4.21 |
| **Binwalk** | Firmware analysis | 2.3 |

### Cryptography Tools
| Tool | Purpose | Version |
|------|---------|---------|
| **Hashcat** | Password cracking | 6.2 |
| **John** | Password cracking | 1.9 |
| **OpenSSL** | Crypto operations | 3.2 |

## 🚀 Installation

```bash
# Download ISO
wget https://github.com/0xvanguard/redteamos/releases/download/v1.0.0/RedTeamOS-v1.0.0.iso

# Write to USB (Linux)
sudo dd if=RedTeamOS-v1.0.0.iso of=/dev/sdX bs=4M status=progress

# Write to USB (macOS)
sudo dd if=RedTeamOS-v1.0.0.iso of=/dev/diskN bs=4m

# Boot from USB
# 1. Restart computer
# 2. Press F12/Boot menu
# 3. Select USB drive
```

## 💻 Usage

### Quick Start
```bash
# Boot RedTeamOS from USB
# Login: redteam / redteam

# Start AI security testing
$ redteam-ai-scan --target http://llm-api.local

# Start network recon
$ redteam-net-recon --range 192.168.1.0/24

# Start web app testing
$ redteam-web-test --target https://app.local
```

### AI Red Team Mode
```bash
# Interactive AI testing
$ redteam-ai

> Select target: http://llm-api.local
> Select attack category: jailbreak
> Running 50 attacks...
> Results: 42% success rate
> Report saved to /reports/llm_scan_2024.html
```

## 📁 Project Structure

```
redteamos/
├── src/
│   ├── __init__.py
│   └── tools.py               # Tool management
├── iso/
│   └── build.sh               # ISO build script
├── configs/
│   ├── tools.json             # Tool configurations
│   └── defaults.json          # Default settings
├── scripts/
│   ├── redteam-ai-scan.sh     # AI scanning script
│   ├── redteam-net-recon.sh   # Network recon script
│   └── redteam-web-test.sh    # Web testing script
└── README.md
```

## 📄 License

GPL-3.0 — Free for security researchers.

---

<div align="center">

**Built by [@0xvanguard](https://github.com/0xvanguard)** • [⭐ Star this repo](https://github.com/0xvanguard/redteamos) • [🐛 Report Bug](https://github.com/0xvanguard/redteamos/issues)

</div>
