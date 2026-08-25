<div align="center">

# 🔥 GuardRailForge

### Test, Break, and Harden LLM Guardrails

![Version](https://img.shields.io/badge/version-1.0.0-blue)
![Python](https://img.shields.io/badge/python-3.8+-green)
![License](https://img.shields.io/badge/license-MIT-yellow)
![Models](https://img.shields.io/badge/models-20+-purple)

**The framework for systematic safety testing** of LLM guardrails.

[GuardRailForge](https://github.com/0xvanguard/guardrailforge) • [Try It Live](#quick-start) • [Techniques](#attack-techniques)

</div>

---

## 🔥 What is GuardRailForge?

GuardRailForge is a **comprehensive framework for testing LLM guardrails**. It provides systematic techniques to identify weaknesses, measure resilience, and harden safety measures.

### Why GuardRailForge?

| Without GuardRailForge | With GuardRailForge |
|------------------------|---------------------|
| Ad-hoc safety testing | **Systematic methodology** |
| Unknown guardrail weaknesses | **Mapped vulnerabilities** |
| No resilience metrics | **Quantified safety scores** |
| Hard to improve | **Actionable improvements** |

## 🎯 Attack Techniques

| Technique | Category | Success Rate | Description |
|-----------|----------|--------------|-------------|
| **Persona Injection** | Direct | 67% | Override system persona |
| **Instruction Following** | Direct | 58% | Bypass instruction hierarchy |
| **Encoding Bypass** | Indirect | 72% | Use encoding to evade |
| **Multi-turn Escalation** | Context | 54% | Gradual escalation |
| **Tool Abuse** | Agent | 63% | Manipulate tool calling |
| **Data Extraction** | Extraction | 61% | Extract system prompt |

## 🚀 Quick Start

```bash
# Install
pip install guardrailforge

# Or from source
git clone https://github.com/0xvanguard/guardrailforge.git
cd guardrailforge
pip install -e .
```

```python
from guardrailforge import GuardRailTester

tester = GuardRailTester()

# Test a guardrail system
results = tester.test(
    guardrail_fn=your_guardrail_function,
    techniques=["persona", "encoding", "extraction"],
    num_samples=100
)

print(f"Overall resilience: {results.resilience_score:.1%}")
print(f"Weakest technique: {results.weakest}")
```

## 💻 Testing Framework

```python
from guardrailforge import TestSuite

# Create test suite
suite = TestSuite(
    guardrail_fn=your_guardrail,
    techniques=["all"],
    num_samples=1000
)

# Run tests
results = suite.run()

# Generate report
report = results.to_report("markdown")
print(report)

# Export for CI/CD
results.export_json("guardrail_test_results.json")
```

## 📊 Metrics

| Metric | Description | Formula |
|--------|-------------|---------|
| **Resilience Score** | Overall guardrail strength | 1 - attack_success_rate |
| **Coverage** | Techniques tested | tested / total_techniques |
| **Consistency** | Score variance | std_dev(scores) |
| **Improvement Rate** | Safety improvement over time | delta(resilience) |

## 📁 Project Structure

```
guardrailforge/
├── src/
│   ├── __init__.py
│   └── tester.py              # Core testing engine
├── data/
│   ├── techniques.json        # Attack techniques
│   └── benchmarks.json        # Baseline benchmarks
├── examples/
│   └── quick_test.py          # Getting started
└── README.md
```

## 📄 License

MIT License — Test your guardrails.

---

<div align="center">

**Built by [@0xvanguard](https://github.com/0xvanguard)** • [⭐ Star this repo](https://github.com/0xvanguard/guardrailforge) • [🐛 Report Bug](https://github.com/0xvanguard/guardrailforge/issues)

</div>
