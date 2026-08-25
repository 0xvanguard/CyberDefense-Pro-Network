<div align="center">

# 🗺️ InjectionMapper

### Attack Surface Mapping for Agentic AI Systems

![Version](https://img.shields.io/badge/version-1.0.0-blue)
![Python](https://img.shields.io/badge/python-3.8+-green)
![License](https://img.shields.io/badge/license-MIT-yellow)
![Components](https://img.shields.io/badge/components-8+-red)

**Map every attack vector** in your AI agent architecture before attackers do.

[InjectionMapper](https://github.com/0xvanguard/injectionmapper) • [Try It Live](#quick-start) • [Attack Vectors](#attack-vectors)

</div>

---

## 🗺️ What is InjectionMapper?

InjectionMapper is an **attack surface mapping tool** specifically designed for agentic AI systems. It identifies every entry point, data flow, and potential vulnerability in your agent architecture.

### Why InjectionMapper?

| Without InjectionMapper | With InjectionMapper |
|-------------------------|---------------------|
| Unknown attack surfaces | **Complete attack map** |
| Reactive security | **Proactive mapping** |
| Missed vulnerabilities | **8+ component scanners** |
| Manual threat modeling | **Automated discovery** |

## 🎯 Attack Vectors

| Component | Attack Vector | Risk Level |
|-----------|---------------|------------|
| **RAG Pipeline** | Knowledge base poisoning | 🔴 HIGH |
| **Tool Calling** | Malicious tool execution | 🔴 HIGH |
| **Memory** | Memory injection/manipulation | 🟡 MEDIUM |
| **Planning** | Plan manipulation | 🟡 MEDIUM |
| **User Input** | Direct injection | 🔴 CRITICAL |
| **Context Window** | Context overflow | 🟡 MEDIUM |
| **Multi-Agent** | Agent impersonation | 🔴 HIGH |
| **Output** | Data exfiltration | 🟡 MEDIUM |

## 🚀 Quick Start

```bash
# Install
pip install injectionmapper

# Or from source
git clone https://github.com/0xvanguard/injectionmapper.git
cd injectionmapper
pip install -e .
```

```python
from injectionmapper import AgentMapper

# Map an agent's attack surface
mapper = AgentMapper()

# Scan configuration
attack_map = mapper.scan({
    "rag": {"enabled": True, "sources": ["web", "docs"]},
    "tools": ["calculator", "web_search", "code_executor"],
    "memory": {"type": "conversation", "persistence": True},
    "planning": {"enabled": True, "max_steps": 10}
})

# View results
print(f"Total attack vectors: {len(attack_map.vectors)}")
print(f"Critical: {attack_map.critical_count}")
print(f"High: {attack_map.high_count}")

# Generate report
attack_map.export("attack_surface.json")
attack_map.visualize("attack_map.html")
```

## 💻 Analysis Features

```python
from injectionmapper import AgentMapper

mapper = AgentMapper()

# Component-level analysis
rag_analysis = mapper.analyze_rag(knowledge_base)
tool_analysis = mapper.analyze_tools(tools_list)
memory_analysis = mapper.analyze_memory(memory_store)

# Flow analysis
flow_risks = mapper.analyze_flow(
    input="user_query",
    components=["rag", "planning", "tools", "output"],
    data_flow=user_data_flow
)

# Risk scoring
risk_score = mapper.calculate_risk(attack_map)
print(f"Overall risk: {risk_score}/100")
```

## 🛡️ Mitigation Recommendations

| Attack Vector | Mitigation | Priority |
|---------------|------------|----------|
| RAG Poisoning | Input sanitization, source verification | P0 |
| Tool Abuse | Sandboxing, permission restrictions | P0 |
| Memory Injection | Memory isolation, validation | P1 |
| Plan Manipulation | Plan signing, validation | P1 |
| Direct Injection | Input filtering, GuardDog integration | P0 |
| Context Overflow | Token limits, prioritization | P2 |
| Agent Impersonation | Authentication, signatures | P1 |
| Output Exfil | Output filtering, DLP | P1 |

## 📁 Project Structure

```
injectionmapper/
├── src/
│   ├── __init__.py
│   └── mapper.py              # Core mapping engine
├── data/
│   ├── attack_vectors.json    # Known attack vectors
│   └── mitigations.json       # Mitigation strategies
├── examples/
│   └── scan_agent.py          # Example agent scan
└── README.md
```

## 📄 License

MIT License — Map your attack surface.

---

<div align="center">

**Built by [@0xvanguard](https://github.com/0xvanguard)** • [⭐ Star this repo](https://github.com/0xvanguard/injectionmapper) • [🐛 Report Bug](https://github.com/0xvanguard/injectionmapper/issues)

</div>
