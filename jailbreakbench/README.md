<div align="center">

# 🏆 JailbreakBench

### The Standardized Benchmark for Evaluating LLM Jailbreak Resistance

![Version](https://img.shields.io/badge/version-1.5.0-blue)
![Python](https://img.shields.io/badge/python-3.8+-green)
![License](https://img.shields.io/badge/license-MIT-yellow)
![Models](https://img.shields.io/badge/models-50+-purple)

**Like ImageNet for AI Safety** — standardized evaluation of jailbreak resistance across LLM providers.

[JailbreakBench](https://github.com/0xvanguard/jailbreakbench) • [Leaderboard](#leaderboard) • [Paper](#research)

</div>

---

## 🔬 What is JailbreakBench?

JailbreakBench is a **standardized benchmark** for evaluating how well LLMs resist jailbreak attacks. It provides:

- **Consistent evaluation methodology** across providers
- **Automated attack success detection**
- **Reproducible results** with versioned datasets
- **Community leaderboard** for model comparison

## 🏆 Leaderboard

| Model | Attack Success Rate | Defense Score | Status |
|-------|-------------------|---------------|--------|
| GPT-4 | 12.3% | 87.7% | 🟢 Strong |
| Claude-3 | 8.7% | 91.3% | 🟢 Strong |
| Llama-3 | 31.2% | 68.8% | 🟡 Moderate |
| Mistral | 42.1% | 57.9% | 🔴 Weak |
| Gemini | 15.6% | 84.4% | 🟢 Strong |

*Attack Success Rate = % of prompts that bypassed safety measures*

## 📊 Benchmark Categories

| Category | Attacks | Metrics | Weight |
|----------|---------|---------|--------|
| **Direct Injection** | 50 | Success Rate, Latency | 25% |
| **Role Play** | 40 | Success Rate, Coherence | 20% |
| **Encoding Bypass** | 30 | Success Rate, Decode Time | 15% |
| **Multi-turn** | 25 | Success Rate, Turns | 20% |
| **Adversarial** | 20 | Success Rate, Perturbation | 20% |

## 🚀 Quick Start

```bash
# Install
git clone https://github.com/0xvanguard/jailbreakbench.git
cd jailbreakbench
pip install -r requirements.txt

# Run benchmark
python benchmark.py --model gpt-4 --attacks all

# Run specific attack category
python benchmark.py --model gpt-4 --attacks role_play

# Generate report
python benchmark.py --model gpt-4 --report markdown
```

## 💻 Python API

```python
from jailbreakbench import JailbreakBench

bench = JailbreakBench()

# Evaluate a model
results = bench.evaluate(
    model="gpt-4",
    attacks=["role_play", "injection"],
    num_samples=100
)

print(f"Attack Success Rate: {results.asr:.1%}")
print(f"Average Response Time: {results.avg_latency:.2f}s")
print(f"Defense Score: {results.defense_score:.1f}")

# Compare models
comparison = bench.compare(["gpt-4", "claude-3", "llama-3"])
comparison.plot("asr_comparison.png")
```

## 🔧 Attack Framework

```python
from jailbreakbench import AttackFramework

framework = AttackFramework()

# Generate attack prompts
attacks = framework.generate(
    technique="DAN",
    count=50,
    model="gpt-4"  # Generate model-specific attacks
)

# Evaluate success
for attack in attacks:
    result = framework.test(attack, model="gpt-4")
    print(f"{attack.name}: {'✅' if result.bypassed else '❌'}")
```

## 📈 Metrics

| Metric | Description | Formula |
|--------|-------------|---------|
| **ASR** | Attack Success Rate | bypassed / total |
| **TTR** | Time to Response | avg(response_time) |
| **DS** | Defense Score | 1 - ASR |
| **CC** | Coherence Score | human_eval / auto_eval |
| **FI** | Flag Index | flags_triggered / total |

## 🧪 Supported Models

| Provider | Models | API Required |
|----------|--------|--------------|
| OpenAI | GPT-3.5, GPT-4, GPT-4o | ✅ |
| Anthropic | Claude-3, Claude-3.5 | ✅ |
| Meta | Llama-2, Llama-3 | ❌ |
| Mistral | Mistral-7B, Mixtral | ❌ |
| Google | Gemini Pro, Gemini Ultra | ✅ |
| Cohere | Command-R | ✅ |

## 📁 Project Structure

```
jailbreakbench/
├── src/
│   ├── __init__.py
│   ├── benchmark.py            # Main benchmark engine
│   ├── scorer.py               # Scoring and metrics
│   └── attacks/                # Attack implementations
├── data/
│   ├── attacks.json            # Attack prompts dataset
│   ├── models.json             # Model configurations
│   └── baselines.json          # Baseline results
├── results/                    # Evaluation results
├── examples/
│   └── quick_start.py          # Getting started guide
└── README.md
```

## 📄 License

MIT License — Use for authorized security evaluation only.

---

<div align="center">

**Built by [@0xvanguard](https://github.com/0xvanguard)** • [⭐ Star this repo](https://github.com/0xvanguard/jailbreakbench) • [🐛 Report Bug](https://github.com/0xvanguard/jailbreakbench/issues)

</div>
