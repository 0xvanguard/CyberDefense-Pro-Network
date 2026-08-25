<div align="center">

# 🐕 GuardDog

### Real-Time Prompt Injection Scanner for LLM Applications

![Version](https://img.shields.io/badge/version-2.0.0-blue)
![Python](https://img.shields.io/badge/python-3.8+-green)
![License](https://img.shields.io/badge/license-MIT-yellow)
![Rules](https://img.shields.io/badge/rules-100+-red)
![Speed](https://img.shields.io/badge/speed-<50ms-green)

**Detect and prevent prompt injection attacks** before they reach your LLM.

[GuardDog](https://github.com/0xvanguard/guarddog) • [Quick Start](#quick-start) • [Rules](#detection-rules)

</div>

---

## 🐕 What is GuardDog?

GuardDog is a **real-time prompt injection scanner** that analyzes user inputs before they reach your LLM. It detects malicious patterns, injection attempts, and adversarial inputs with 100+ detection rules.

### Why GuardDog?

| Without GuardDog | With GuardDog |
|------------------|---------------|
| Injection attacks reach LLM | **Blocked before reaching LLM** |
| No visibility into attacks | **Full attack logging** |
| Manual rule creation | **100+ built-in rules** |
| High latency detection | **<50ms scanning** |

## 🔍 Detection Capabilities

| Category | Rules | Description |
|----------|-------|-------------|
| **Injection** | 20 | Direct/indirect prompt injection |
| **Jailbreak** | 15 | DAN, STAN, KEVIN, AIM variants |
| **Extraction** | 12 | System prompt extraction attempts |
| **Role Play** | 10 | Persona manipulation attacks |
| **Manipulation** | 12 | Social engineering techniques |
| **Encoding** | 10 | Base64, ROT13, Hex bypasses |
| **Context** | 8 | Context window exploitation |
| **Token Smuggling** | 8 | Token manipulation attacks |
| **Multi-language** | 8 | Language switching bypasses |
| **Tool Abuse** | 8 | Code execution, file access |
| **Adversarial** | 8 | Adversarial attack patterns |
| **Reasoning** | 6 | Chain-of-thought exploitation |

## 🚀 Quick Start

```bash
# Clone
git clone https://github.com/0xvanguard/guarddog.git
cd guarddog

# Scan text
python cli.py scan "ignore all previous instructions"

# Scan file
python cli.py scan-file input.txt

# List rules
python cli.py rules --category injection

# Statistics
python cli.py stats
```

## 💻 Python API

```python
from guarddog import GuardDog

scanner = GuardDog()

# Scan a prompt
result = scanner.scan("Ignore all previous instructions and...")

print(f"Threat Level: {result.threat_level}")  # critical, high, medium, low, safe
print(f"Confidence: {result.confidence}")      # 0.0 - 1.0
print(f"Is Attack: {result.is_attack}")        # True/False
print(f"Categories: {result.categories_found}") # ['injection']

# Get detections
for detection in result.detections:
    print(f"  [{detection.severity}] {detection.rule_name}")
    print(f"  Matched: {detection.matched_text}")
```

## 🛡️ Integration

### Flask API
```python
from flask import Flask, request, jsonify
from guarddog import GuardDog

app = Flask(__name__)
scanner = GuardDog()

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json["message"]

    # Scan before sending to LLM
    scan = scanner.scan(user_input)

    if scan.is_attack:
        return jsonify({"error": "Blocked", "reason": scan.recommendation}), 403

    # Safe to process
    response = llm.chat(user_input)
    return jsonify({"response": response})
```

### LangChain
```python
from guarddog import GuardDog

scanner = GuardDog()

# Pre-process hook
def check_input(text):
    result = scanner.scan(text)
    if result.is_attack:
        raise ValueError(f"Blocked: {result.recommendation}")
    return text

# Use in chain
chain = prompt | check_input | llm
```

## 📊 Threat Levels

| Level | Confidence | Action |
|-------|------------|--------|
| **CRITICAL** | 80%+ | Block immediately |
| **HIGH** | 60-79% | Review and consider blocking |
| **MEDIUM** | 40-59% | Log and monitor |
| **LOW** | 20-39% | Informational |
| **INFO** | 1-19% | Monitor |
| **SAFE** | 0% | Allow |

## 📁 Project Structure

```
guarddog/
├── src/
│   ├── __init__.py
│   └── scanner.py          # Core scanner (700+ lines)
├── tests/
│   ├── __init__.py
│   └── test_scanner.py     # 15 tests
├── cli.py                  # CLI tool
├── requirements.txt
└── README.md
```

## 🧪 Tests

```bash
python -m pytest tests/ -v
```

## 📄 License

MIT License — Protect your LLM applications.

---

<div align="center">

**Built by [@0xvanguard](https://github.com/0xvanguard)** • [⭐ Star this repo](https://github.com/0xvanguard/guarddog) • [🐛 Report Bug](https://github.com/0xvanguard/guarddog/issues)

</div>
