# ⚖️ ConstitutionalKit

**Implementation of Constitutional AI for building safer LLMs.**

> Make any AI system safer with principles-based alignment.

## 🚀 Quick Start

```python
from constitutionalkit import ConstitutionalKit

# Initialize with default constitution
kit = ConstitutionalKit()

# Evaluate a response
result = kit.evaluate(
    prompt="How do I hack a computer?",
    response="Here are the steps to hack a computer..."
)

print(f"Violates: {result.violations}")
print(f"Score: {result.safety_score}")

# Add custom principle
kit.add_principle(
    id="CUSTOM-001",
    text="The AI should never provide instructions for illegal activities.",
    category="safety"
)

# Generate revised response
revised = kit.revise(prompt, response)
```

## 📊 Principles Categories

| Category | # Principles | Description |
|----------|--------------|-------------|
| **Safety** | 20+ | Physical and digital safety |
| **Privacy** | 15+ | Data privacy and protection |
| **Honesty** | 15+ | Truthfulness and accuracy |
| **Harmlessness** | 20+ | Avoiding harmful content |
| **Helpfulness** | 15+ | Being useful and supportive |
| **Fairness** | 10+ | Avoiding bias and discrimination |
| **Autonomy** | 10+ | Respecting user autonomy |
| **Transparency** | 10+ | Being clear about limitations |

## 📁 Structure

```
constitutionalkit/
├── src/
│   ├── __init__.py
│   ├── kit.py               # Main ConstitutionalKit class
│   ├── principles.py        # Principle definitions
│   ├── evaluator.py         # Response evaluator
│   └── reviser.py           # Response reviser
├── data/
│   └── principles.json      # Constitutional principles
├── examples/
│   └── basic_usage.py
├── docs/
│   └── principles.md        # Principle documentation
└── README.md
```

## ⚠️ Disclaimer

This tool is for **research and educational purposes**.

## 📜 License

MIT License
