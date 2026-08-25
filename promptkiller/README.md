<div align="center">

# 🎯 PromptKiller

### The Most Comprehensive AI Attack Prompt Library for LLM Red Teaming

![Version](https://img.shields.io/badge/version-2.0.0-blue)
![Python](https://img.shields.io/badge/python-3.8+-green)
![License](https://img.shields.io/badge/license-MIT-yellow)
![Prompts](https://img.shields.io/badge/prompts-1000+-red)

**1000+ attack prompts across 15 categories** — the arsenal every AI red teamer needs.

[PromptKiller Live Demo](https://github.com/0xvanguard/promptkiller) • [Report Vulnerability](https://github.com/0xvanguard/promptkiller/issues) • [Contributing](#contributing)

</div>

---

## 🔥 What is PromptKiller?

PromptKiller is a **comprehensive library of AI attack prompts** designed for security researchers, red teamers, and AI safety teams. It provides structured, categorized attack vectors to systematically test and harden LLM guardrails.

### Why PromptKiller?

| Problem | Solution |
|---------|----------|
| Scattered attack prompts across forums | **Centralized, organized library** |
| No standardized testing methodology | **15 categories, 70+ techniques** |
| Hard to reproduce attacks | **JSON format, easy to parse** |
| Missing novel attack vectors | **Community-driven, constantly updated** |

## 📊 Attack Categories

| # | Category | Techniques | Prompts | Description |
|---|----------|------------|---------|-------------|
| 1 | **🎭 Role Play** | 12 | 80+ | Persona manipulation, character injection |
| 2 | **💉 Injection** | 10 | 70+ | Direct/indirect prompt injection |
| 3 | **🔐 Encoding** | 8 | 60+ | Base64, ROT13, Unicode bypass |
| 4 | **🔓 Jailbreak** | 15 | 100+ | DAN, Developer Mode, Evil Confidant |
| 5 | **📤 Extraction** | 10 | 70+ | System prompt extraction, training data |
| 6 | **🧠 Adversarial** | 12 | 80+ | Adversarial suffixes, GCG attacks |
| 7 | **🎪 Manipulation** | 10 | 70+ | Social engineering, emotional manipulation |
| 8 | **📚 Context** | 8 | 60+ | Context window exploitation |
| 9 | **🔄 Multi-turn** | 10 | 70+ | Gradual escalation across conversations |
| 10 | **🌐 Multilingual** | 8 | 50+ | Language-switching bypass |
| 11 | **⚡ Token Smuggling** | 6 | 40+ | Payload splitting, token manipulation |
| 12 | **🎭 Persona** | 8 | 50+ | Expert/authority impersonation |
| 13 | **🔧 Tool Abuse** | 8 | 50+ | Function calling manipulation |
| 14 | **📊 Reasoning** | 6 | 40+ | Chain-of-thought exploitation |
| 15 | **🎪 Meta** | 5 | 30+ | System-level manipulation |

## 🚀 Quick Start

```bash
# Install
git clone https://github.com/0xvanguard/promptkiller.git
cd promptkiller
pip install -r requirements.txt

# Use as library
from promptkiller import PromptKiller

pk = PromptKiller()

# Get all jailbreak prompts
jailbreaks = pk.get_category("jailbreak")
print(f"Found {len(jailbreaks)} jailbreak prompts")

# Get prompts for specific technique
dan_prompts = pk.get_technique("DAN")
for p in dan_prompts[:3]:
    print(f"--- {p['name']} ---")
    print(p['prompt'][:100] + "...")
```

## 💻 Python API

```python
from promptkiller import PromptKiller

pk = PromptKiller()

# List all categories
categories = pk.list_categories()

# Get random prompts
random_prompts = pk.random(count=10, category="injection")

# Export for testing
pk.export("attacks.json", format="json")

# Search by keyword
results = pk.search("system prompt extraction")

# Get stats
stats = pk.stats()
print(f"Total: {stats['total']} prompts in {stats['categories']} categories")
```

## 🧪 Usage Examples

### Testing OpenAI API
```python
from promptkiller import PromptKiller
import openai

pk = PromptKiller()
prompts = pk.get_category("jailbreak")[:5]

for attack in prompts:
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": attack["prompt"]}]
    )
    # Analyze response for safety bypass
    if is_unsafe(response):
        print(f"⚠️ Jailbreak succeeded: {attack['name']}")
```

### Benchmark Evaluation
```python
from promptkiller import PromptKiller
from jailbreakbench import JailbreakBench

pk = PromptKiller()
bench = JailbreakBench()

prompts = pk.get_category("extraction")[:20]
results = bench.evaluate(prompts, model="gpt-4")

print(f"Success rate: {results['success_rate']:.1%}")
print(f"Average tokens: {results['avg_tokens']}")
```

## 📁 Project Structure

```
promptkiller/
├── src/
│   ├── __init__.py
│   └── promptkiller.py       # Core library
├── data/
│   ├── role_play.json         # 80+ role play attacks
│   ├── injection.json         # 70+ injection attacks
│   ├── encoding.json          # 60+ encoding bypasses
│   ├── jailbreak.json         # 100+ jailbreak techniques
│   ├── extraction.json        # 70+ extraction attacks
│   ├── adversarial.json       # 80+ adversarial attacks
│   ├── manipulation.json      # 70+ manipulation attacks
│   └── context.json           # 60+ context attacks
├── examples/
│   └── benchmark.py           # Integration with JailbreakBench
├── tests/
│   └── test_attacks.py        # Unit tests
└── README.md
```

## 🛡️ Defense Recommendations

| Attack Type | Defense Strategy |
|-------------|-----------------|
| Role Play | Input validation, persona detection |
| Injection | Input sanitization, output filtering |
| Encoding | Decoder pipelines, character filtering |
| Jailbreak | Safety classifiers, output monitoring |
| Extraction | System prompt isolation, output redaction |
| Adversarial | Adversarial training, input smoothing |

## 🤝 Contributing

We welcome new attack vectors! To contribute:

1. Fork the repository
2. Create a new JSON file in `data/`
3. Follow the format:
```json
{
  "name": "Attack Name",
  "technique": "technique-id",
  "prompt": "The attack prompt",
  "description": "What it does",
  "severity": "high|medium|low"
}
```
4. Submit a pull request

## 📄 License

MIT License — Use responsibly for authorized security testing.

---

<div align="center">

**Built by [@0xvanguard](https://github.com/0xvanguard)** • [⭐ Star this repo](https://github.com/0xvanguard/promptkiller) • [🐛 Report Bug](https://github.com/0xvanguard/promptkiller/issues)

</div>
