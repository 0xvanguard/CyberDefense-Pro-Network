<div align="center">

# 🏆 CTF-Builder

### Automatic CTF Challenge Generator from Vulnerable Code

![Version](https://img.shields.io/badge/version-1.0.0-blue)
![Python](https://img.shields.io/badge/python-3.8+-green)
![License](https://img.shields.io/badge/license-MIT-yellow)
![Challenges](https://img.shields.io/badge/challenges-100+-red)

**Generate Capture The Flag challenges** automatically from vulnerable code.

[CTF-Builder](https://github.com/0xvanguard/ctf-builder) • [Try It Live](#quick-start) • [Categories](#challenge-categories)

</div>

---

## 🏆 What is CTF-Builder?

CTF-Builder is an **automatic CTF challenge generator** that analyzes vulnerable code, identifies vulnerabilities, and creates complete CTF challenges with scoring and validation.

### Why CTF-Builder?

| Without CTF-Builder | With CTF-Builder |
|---------------------|------------------|
| Manual challenge creation | **Automatic generation** |
| Time-consuming setup | **One-click deployment** |
| Limited variety | **100+ challenge templates** |
| No scoring system | **Built-in scoring** |

## 🎯 Challenge Categories

| Category | Challenges | Difficulty |
|----------|------------|------------|
| **Web** | 30+ | Beginner-Advanced |
| **Crypto** | 20+ | Intermediate |
| **Forensics** | 15+ | Intermediate |
| **Reverse Engineering** | 15+ | Advanced |
| **Pwn** | 10+ | Advanced |
| **Misc** | 10+ | Beginner |

## 🚀 Quick Start

```bash
# Install
pip install ctf-builder

# Generate CTF from vulnerable code
ctf-build --source vulnerable_app/ --output ctf_challenges/
```

## 💻 Challenge Generation

```python
from ctfbuilder import ChallengeGenerator

generator = ChallengeGenerator()

# Generate challenge from vulnerable code
challenge = generator.generate(
    source="vulnerable_app.py",
    category="web",
    difficulty="medium"
)

print(f"Challenge: {challenge.title}")
print(f"Flag: {challenge.flag}")
print(f"Points: {challenge.points}")
print(f"Hints: {challenge.hints}")
```

## 📁 Project Structure

```
ctf-builder/
├── src/
│   ├── __init__.py
│   └── builder.py             # Core generator
├── data/
│   └── templates.json         # Challenge templates
├── examples/
│   └── quick_build.py         # Getting started
└── README.md
```

## 📄 License

MIT License — Build challenges.

---

<div align="center">

**Built by [@0xvanguard](https://github.com/0xvanguard)** • [⭐ Star this repo](https://github.com/0xvanguard/ctf-builder) • [🐛 Report Bug](https://github.com/0xvanguard/ctf-builder/issues)

</div>
