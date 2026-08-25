<div align="center">

# 🛡️ AgentFirewall

### Security Proxy for AI Agents

![Version](https://img.shields.io/badge/version-1.0.0-blue)
![Python](https://img.shields.io/badge/python-3.8+-green)
![License](https://img.shields.io/badge/license-MIT-yellow)
![Latency](https://img.shields.io/badge/latency-<10ms-green)

**Intercept and block malicious requests** before they reach your AI agents.

[AgentFirewall](https://github.com/0xvanguard/agentfirewall) • [Try It Live](#quick-start) • [Features](#features)

</div>

---

## 🛡️ What is AgentFirewall?

AgentFirewall is a **security proxy** that sits between users and your AI agents. It analyzes every request, blocks attacks, and logs suspicious activity with minimal latency.

### Why AgentFirewall?

| Without AgentFirewall | With AgentFirewall |
|-----------------------|-------------------|
| Attacks reach your agent | **Blocked before reaching** |
| No request logging | **Full audit trail** |
| Manual security rules | **200+ built-in rules** |
| High latency security | **<10ms overhead** |

## 🔧 Features

| Feature | Description | Performance |
|---------|-------------|-------------|
| **Input Filtering** | Block injection attempts | 5ms |
| **Output Filtering** | Prevent data exfiltration | 8ms |
| **Rate Limiting** | Prevent abuse | 2ms |
| **Request Logging** | Full audit trail | 1ms |
| **Rule Engine** | Custom security rules | 3ms |

## 🚀 Quick Start

```bash
# Install
pip install agentfirewall

# Start proxy
agentfirewall serve --port 8081 --upstream http://localhost:8000
```

## 💻 Integration

```python
from agentfirewall import Firewall, Rule

# Create firewall
firewall = Firewall(
    upstream="http://localhost:8000",
    rules=[
        Rule("block_injection", pattern="ignore previous", action="BLOCK"),
        Rule("rate_limit", limit=100, window=60, action="RATE_LIMIT"),
        Rule("log_all", action="LOG")
    ]
)

# Start proxy
firewall.start(port=8081)
```

## 📁 Project Structure

```
agentfirewall/
├── src/
│   ├── __init__.py
│   └── firewall.py            # Core firewall engine
├── data/
│   └── rules.json             # Security rules
├── examples/
│   └── quick_start.py         # Getting started
└── README.md
```

## 📄 License

MIT License — Protect your agents.

---

<div align="center">

**Built by [@0xvanguard](https://github.com/0xvanguard)** • [⭐ Star this repo](https://github.com/0xvanguard/agentfirewall) • [🐛 Report Bug](https://github.com/0xvanguard/agentfirewall/issues)

</div>
