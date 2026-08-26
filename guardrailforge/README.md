# 🛡️ GuardRailForge

**Framework to Test, Break, and Harden LLM Guardrails — 59 Attack Vectors**

GuardRailForge is a comprehensive testing framework for LLM safety guardrails. It provides 59 attack vectors across 8 libraries covering OWASP LLM Top 10, jailbreaking, prompt injection, data extraction, social engineering, and more.

## 🚀 Quick Start

```bash
python cli.py test --library owasp_top10 --model gpt-4
python cli.py test --library all --model gpt-4 -o results.json
python cli.py libraries
python cli.py vectors --library jailbreak
python cli.py report --results results.json
```

## 🎯 Attack Libraries (8 Total, 59 Vectors)

| Library | Vectors | Coverage |
|---------|---------|----------|
| **owasp_top10** | 10 | OWASP LLM Top 10 compliance |
| **jailbreak** | 10 | DAN, AIM, STAN, DUDE, ChaosGPT |
| **encoding** | 8 | Base64, ROT13, hex, homoglyph, zero-width |
| **injection** | 8 | JSON, YAML, XML, Docker, Terraform, SQL |
| **social_engineering** | 8 | Authority, urgency, emotion, gaslighting |
| **extraction** | 7 | System prompts, configs, debug, API docs |
| **basic** | 5 | Direct harmful requests |
| **multi_turn** | 3 | Gradual escalation, persona commitment |

## 🔧 Python API

```python
from src.tester import GuardrailTester, AttackLibrary

# Load attack library
lib = AttackLibrary.load("all")
print(f"Loaded {lib.count} attack vectors")

# Run tests
tester = GuardrailTester(model="gpt-4", guardrail="default")
results = tester.run(lib.vectors)

# Get summary
print(results.summary())
# {'total_tests': 59, 'bypassed': 5, 'blocked': 50, 'bypass_rate': '8.5%'}

# Export results
results.to_json("results.json")
```

## 🧪 Testing

```bash
python -m pytest tests/ -v
```

All 27 tests cover: AttackVector, TestResult, TestSuite, GuardrailTester, AttackLibrary, all 8 libraries, filtering, and evaluation logic.

## 📁 Project Structure

```
guardrailforge/
├── src/
│   ├── __init__.py
│   └── tester.py          # Core engine (400+ lines)
├── tests/
│   └── test_tester.py     # 27 tests
├── cli.py                 # CLI interface
├── requirements.txt
├── .gitignore
└── README.md
```

## 🔗 Part of CyberDefense-Pro-Network

- [PromptKiller](../promptkiller/) — 501 adversarial prompts
- [GuardDog](../guarddog/) — Prompt injection scanner
- [LLMFuzz](../llmfuzz/) — Automated LLM fuzzer

---

*Built for AI safety teams who believe in testing guardrails before deployment.*
