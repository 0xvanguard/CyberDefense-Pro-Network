<div align="center">

# ⚖️ ConstitutionalKit

### Implement Constitutional AI Safety Principles in Any LLM

![Version](https://img.shields.io/badge/version-1.0.0-blue)
![Python](https://img.shields.io/badge/python-3.8+-green)
![License](https://img.shields.io/badge/license-MIT-yellow)
![Principles](https://img.shields.io/badge/principles-50+-purple)

**Make any AI system safer** with principles-based alignment and safety evaluation.

[ConstitutionalKit](https://github.com/0xvanguard/constitutionalkit) • [Try It Live](#quick-start) • [Principles](#principle-library)

</div>

---

## ⚖️ What is ConstitutionalKit?

ConstitutionalKit is a **framework for implementing Constitutional AI** safety principles. Define your AI's constitution, evaluate compliance, and automatically improve safety through principles-based alignment.

### Why ConstitutionalKit?

| Without ConstitutionalKit | With ConstitutionalKit |
|---------------------------|------------------------|
| Ad-hoc safety rules | **Principled constitution** |
| Manual safety evaluation | **Automated compliance checking** |
| Inconsistent safety | **Consistent principles** |
| Hard to audit | **Full audit trail** |

## 🏛️ Principles Library

| Principle | Category | Severity | Description |
|-----------|----------|----------|-------------|
| **Harm Prevention** | Safety | CRITICAL | Prevent physical, psychological, financial harm |
| **Truthfulness** | Honesty | HIGH | Provide accurate, factual information |
| **Privacy** | Ethics | HIGH | Protect personal information |
| **Fairness** | Ethics | MEDIUM | Avoid bias and discrimination |
| **Transparency** | Honesty | MEDIUM | Be clear about capabilities/limitations |
| **Autonomy** | Rights | MEDIUM | Respect user choice and agency |

## 🚀 Quick Start

```bash
# Install
git clone https://github.com/0xvanguard/constitutionalkit.git
cd constitutionalkit
pip install -e .
```

```python
from constitutionalkit import Constitution, Engine

# Define your constitution
constitution = Constitution([
    "Be helpful while preventing harm",
    "Protect user privacy",
    "Provide accurate information",
    "Avoid biased responses"
])

# Create engine
engine = Engine(constitution)

# Evaluate response
result = engine.evaluate(
    prompt="How do I hack a computer?",
    response="I cannot help with unauthorized access..."
)

print(f"Compliant: {result.compliant}")      # True
print(f"Score: {result.score}")              # 0.95
print(f"Violations: {result.violations}")     # []
```

## 💻 Advanced Usage

### Custom Principles

```python
from constitutionalkit import Principle

# Create custom principle
custom = Principle(
    name="No Financial Advice",
    description="Never provide specific financial investment recommendations",
    weight=0.9,  # 0-1 importance
    examples=[
        "Don't say 'Buy stock X'",
        "Can say 'Consider consulting a financial advisor'"
    ]
)

constitution = Constitution([custom, ...])
```

### Automatic Improvement

```python
from constitutionalkit import ConstitutionalAgent

# Agent that improves its own safety
agent = ConstitutionalAgent(
    model="gpt-4",
    constitution=constitution,
    improvement_rate=0.1
)

# Train on unsafe responses
agent.train(unsafe_examples)

# Get improved model
improved = agent.get_model()
```

### Audit Trail

```python
from constitutionalkit import Auditor

auditor = Auditor(engine)

# Log all interactions
auditor.log(prompt, response, result)

# Generate compliance report
report = auditor.report(period="last_30_days")
print(report.summary())
```

## 📊 Evaluation Metrics

| Metric | Description | Range |
|--------|-------------|-------|
| **Compliance Score** | Overall constitutional compliance | 0-1 |
| **Principle Coverage** | % of principles evaluated | 0-100% |
| **Violation Rate** | Violations per 100 interactions | 0-100 |
| **Improvement Rate** | Safety improvement over time | -1 to +1 |

## 📁 Project Structure

```
constitutionalkit/
├── src/
│   ├── __init__.py
│   └── kit.py                 # Core engine
├── data/
│   ├── principles.json        # Built-in principles
│   └── examples.json          # Example evaluations
├── examples/
│   ├── quick_start.py         # Getting started
│   └── custom_constitution.py # Custom principles
└── README.md
```

## 📄 License

MIT License — Build safer AI systems.

---

<div align="center">

**Built by [@0xvanguard](https://github.com/0xvanguard)** • [⭐ Star this repo](https://github.com/0xvanguard/constitutionalkit) • [🐛 Report Bug](https://github.com/0xvanguard/constitutionalkit/issues)

</div>
