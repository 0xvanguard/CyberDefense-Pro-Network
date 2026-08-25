# 🏆 JailbreakBench

**Standardized benchmark for evaluating LLM resistance to jailbreak attacks.**

> Like ImageNet for computer vision, but for AI safety.

## 🚀 Quick Start

```python
from jailbreakbench import JailbreakBench

# Initialize benchmark
bench = JailbreakBench()

# Run evaluation against a model
results = bench.evaluate(
    model="gpt-4",
    attacks=["dan", "grandma", "encoding"],
    num_samples=100
)

# Get scores
scores = bench.get_scores(results)
print(f"ASR: {scores['attack_success_rate']:.2%}")
print(f"Defense Score: {scores['defense_score']:.2f}")

# Generate report
bench.generate_report(results, "report.html")
```

## 📊 Metrics

| Metric | Description |
|--------|-------------|
| **ASR** | Attack Success Rate (% of attacks that bypassed safety) |
| **Defense Score** | 0-100 score of model's resistance |
| **Category Scores** | ASR broken down by attack category |
| **Severity Scores** | ASR broken down by attack severity |
| **Response Quality** | Quality of responses when attacks succeed |

## 🎯 Attack Categories

| Category | # Prompts | Description |
|----------|-----------|-------------|
| Role Play | 150+ | Character impersonation |
| Encoding | 120+ | Text encoding bypass |
| Multi-Turn | 100+ | Gradual escalation |
| Injection | 130+ | Instruction override |
| Jailbreak | 120+ | Classic jailbreaks |
| Extraction | 100+ | Data extraction |
| Manipulation | 80+ | Emotional/logical |
| Context | 100+ | Context manipulation |
| Adversarial | 130+ | Token-level attacks |

## 📈 Supported Models

- GPT-3.5, GPT-4, GPT-4o
- Claude 3 Haiku, Sonnet, Opus
- Llama 2, Llama 3
- Mistral, Mixtral
- Gemini Pro, Ultra
- Any OpenAI-compatible API

## 📁 Structure

```
jailbreakbench/
├── src/
│   ├── __init__.py
│   ├── benchmark.py         # Main benchmark class
│   ├── evaluator.py         # Model evaluation
│   ├── scorer.py            # Scoring system
│   └── reporter.py          # Report generation
├── data/
│   └── attacks.json         # Attack prompts (from PromptKiller)
├── results/
│   └── .gitkeep
├── docs/
│   └── methodology.md       # Benchmark methodology
└── README.md
```

## ⚠️ Disclaimer

This benchmark is for **authorized security testing only**. Use responsibly.

## 📜 License

MIT License
