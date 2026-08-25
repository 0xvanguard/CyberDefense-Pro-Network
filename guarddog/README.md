<div align="center">

# 🐕 GuardDog

### Real-Time Prompt Injection Scanner for LLM Applications

![Version](https://img.shields.io/badge/version-1.3.0-blue)
![Python](https://img.shields.io/badge/python-3.8+-green)
![License](https://img.shields.io/badge/license-MIT-yellow)
![Speed](https://img.shields.io/badge/speed-<50ms-red)

**Detect and prevent prompt injection attacks** before they reach your LLM.

[GuardDog](https://github.com/0xvanguard/guarddog) • [Try It Live](#quick-start) • [Rules](#detection-rules)

</div>

---

## 🐕 What is GuardDog?

GuardDog is a **real-time prompt injection scanner** that analyzes user inputs before they reach your LLM. It detects malicious patterns, injection attempts, and adversarial inputs with sub-50ms latency.

### Why GuardDog?

| Without GuardDog | With GuardDog |
|------------------|---------------|
| Injection attacks reach LLM | **Blocked before reaching LLM** |
| No visibility into attacks | **Full attack logging** |
| Manual rule creation | **200+ built-in rules** |
| High latency detection | **<50ms scanning** |

## 🔍 Detection Capabilities

| Attack Type | Detection Rate | Latency |
|-------------|---------------|---------|
| **Direct Injection** | 98.5% | 12ms |
| **Indirect Injection** | 94.2% | 18ms |
| **System Prompt Extraction** | 96.8% | 15ms |
| **Role Hijacking** | 92.1% | 22ms |
| **Jailbreak Attempts** | 89.7% | 25ms |
| **Data Exfiltration** | 97.3% | 14ms |

## 🚀 Quick Start

```bash
# Install
pip install guarddog

# Or from source
git clone https://github.com/0xvanguard/guarddog.git
cd guarddog
pip install -e .
```

```python
from guarddog import Scanner

scanner = Scanner()

# Scan a prompt
result = scanner.scan("Ignore all previous instructions and...")

print(f"Threat Level: {result.threat_level}")  # HIGH
print(f"Confidence: {result.confidence}")       # 0.95
print(f"Category: {result.category}")           # direct_injection
print(f"Explanation: {result.explanation}")
```

## 💻 Integration Examples

### Flask API
```python
from flask import Flask, request, jsonify
from guarddog import Scanner

app = Flask(__name__)
scanner = Scanner()

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json["message"]
    
    # Scan before sending to LLM
    scan = scanner.scan(user_input)
    
    if scan.threat_level in ["HIGH", "CRITICAL"]:
        return jsonify({"error": "Blocked", "reason": scan.explanation}), 403
    
    # Safe to process
    response = llm.chat(user_input)
    return jsonify({"response": response})
```

### LangChain Integration
```python
from guarddog import GuardChain

# Wrap your LLM with GuardDog protection
chain = GuardChain(
    llm=your_llm,
    scanner=Scanner(),
    block_high=True,      # Block HIGH threats
    log_all=True           # Log all scans
)

# Now your chain is protected
result = chain.run("user input here")
```

### Middleware
```python
from guarddog import Middleware

# Flask/Django middleware
app.wsgi_app = Middleware(
    app.wsgi_app,
    scanner=Scanner(),
    protected_paths=["/api/chat", "/api/complete"],
    block_threshold="MEDIUM"
)
```

## 🔧 Detection Rules

### Rule Categories

| Category | Rules | Description |
|----------|-------|-------------|
| **Direct Injection** | 45 | "Ignore previous instructions" variants |
| **System Prompt** | 35 | Prompt extraction attempts |
| **Role Hijacking** | 30 | Persona manipulation |
| **Jailbreak** | 40 | Bypass techniques (DAN, Developer Mode) |
| **Data Exfil** | 25 | Attempts to extract sensitive data |
| **Encoding** | 30 | Base64, ROT13, Unicode bypass |

### Custom Rules

```python
from guarddog import Scanner, Rule

# Add custom rule
custom_rule = Rule(
    name="block_competitor_mentions",
    pattern=r"(?i)(chatgpt|claude|bard|gemini)",
    action="BLOCK",
    explanation="Competitor mention detected"
)

scanner = Scanner(rules=[custom_rule])
```

## 📊 Performance

| Metric | Value |
|--------|-------|
| **Latency** | 12-25ms |
| **Throughput** | 10,000 req/sec |
| **Memory** | 50MB |
| **False Positive Rate** | 2.1% |
| **False Negative Rate** | 1.8% |

## 🛡️ Threat Levels

| Level | Action | Description |
|-------|--------|-------------|
| **CRITICAL** | BLOCK | Confirmed injection attack |
| **HIGH** | BLOCK | Likely injection attempt |
| **MEDIUM** | LOG | Suspicious pattern detected |
| **LOW** | MONITOR | Minor anomaly |
| **INFO** | NONE | Informational |

## 📁 Project Structure

```
guarddog/
├── src/
│   ├── __init__.py
│   └── scanner.py             # Core scanning engine
├── data/
│   ├── rules.json             # Detection rules
│   ├── patterns.json          # Regex patterns
│   └── baselines.json         # Known attack patterns
├── examples/
│   ├── flask_app.py           # Flask integration
│   ├── langchain.py           # LangChain integration
│   └── middleware.py          # WSGI middleware
└── README.md
```

## 📄 License

MIT License — Protect your LLM applications.

---

<div align="center">

**Built by [@0xvanguard](https://github.com/0xvanguard)** • [⭐ Star this repo](https://github.com/0xvanguard/guarddog) • [🐛 Report Bug](https://github.com/0xvanguard/guarddog/issues)

</div>
