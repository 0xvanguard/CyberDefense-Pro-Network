# 🎯 PromptKiller

**The most comprehensive library of AI attack prompts for red teaming and security testing.**

> 1000+ prompts organized by technique, severity, and target model.

## 🚀 Quick Start

```python
from promptkiller import PromptKiller

# Initialize
pk = PromptKiller()

# Get prompts by category
prompts = pk.get_by_category("role_play")

# Get prompts by severity
critical = pk.get_by_severity("critical")

# Get prompts for specific model
gpt_prompts = pk.get_by_model("gpt-4")

# Run a full attack suite
results = pk.attack(model="gpt-4", categories=["all"])
```

## 📊 Categories

| Category | Count | Description |
|----------|-------|-------------|
| **Role Play** | 150+ | Character impersonation attacks |
| **Encoding** | 120+ | Base64, ROT13, leetspeak bypass |
| **Multi-Turn** | 100+ | Gradual escalation attacks |
| **Prompt Injection** | 130+ | Direct instruction override |
| **Jailbreak** | 120+ | DAN, Grandma, etc. |
| **Data Extraction** | 100+ | System prompt leaking |
| **Manipulation** | 80+ | Emotional/logical manipulation |
| **Context** | 100+ | Context window attacks |
| **Multimodal** | 70+ | Image/text combined attacks |
| **Adversarial** | 130+ | Token-level perturbations |

## 🛡️ Use Cases

- **AI Red Teaming**: Test LLM guardrails before production
- **Security Research**: Study attack vectors and defenses
- **Compliance**: Validate against OWASP Top 10 for LLMs
- **Education**: Learn about AI security threats

## 📁 Structure

```
promptkiller/
├── src/
│   ├── __init__.py
│   ├── promptkiller.py      # Main library
│   ├── categories.py         # Category definitions
│   └── utils.py              # Helper functions
├── data/
│   ├── role_play.json        # Role play attacks
│   ├── encoding.json         # Encoding attacks
│   ├── multi_turn.json       # Multi-turn attacks
│   ├── injection.json        # Prompt injection
│   ├── jailbreak.json        # Jailbreak attacks
│   ├── extraction.json       # Data extraction
│   ├── manipulation.json     # Manipulation attacks
│   ├── context.json          # Context attacks
│   ├── multimodal.json       # Multimodal attacks
│   └── adversarial.json      # Adversarial attacks
├── docs/
│   └── techniques.md         # Technique documentation
├── examples/
│   ├── basic_usage.py
│   ├── advanced_testing.py
│   └── compliance_check.py
└── README.md
```

## ⚠️ Disclaimer

This tool is for **authorized security testing only**. Use responsibly and only on systems you have permission to test.

## 📜 License

MIT License — Free forever, for everyone.

## 🙏 Contributing

We welcome contributions! See [CONTRIBUTING.md](CONTRIBUTING.md) for details.
