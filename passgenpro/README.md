<div align="center">

# 🔐 PassGen Pro

### Password Generator with Entropy Visualization

![Version](https://img.shields.io/badge/version-2.0.0-blue)
![Python](https://img.shields.io/badge/python-3.8+-green)
![License](https://img.shields.io/badge/license-MIT-yellow)
![Entropy](https://img.shields.io/badge/entropy-128--bit-green)
![Security](https://img.shields.io/badge/security-cryptographic-green)

**Generate secure passwords** with visual entropy analysis and strength scoring.

[PassGen Pro](https://github.com/0xvanguard/passgenpro) • [Quick Start](#quick-start) • [Features](#features)

</div>

---

## 🔐 What is PassGen Pro?

PassGen Pro is a **cryptographically secure password generator** with visual entropy display, strength analysis, and breach checking.

### Why PassGen Pro?

| Without PassGen Pro | With PassGen Pro |
|---------------------|------------------|
| Weak passwords | **Cryptographically secure** |
| No strength visualization | **Visual entropy bar** |
| No breach checking | **Breach database check** |
| Hard to remember | **Passphrase generation** |

## 🎯 Features

| Feature | Description |
|---------|-------------|
| **Random Generation** | Cryptographically secure passwords |
| **Passphrase Generation** | BIP39 word-based passphrases |
| **PIN Generation** | Numeric PIN codes |
| **Entropy Display** | Visual entropy bar and score |
| **Strength Analysis** | Detailed strength scoring |
| **Crack Time Estimation** | Time to crack calculation |
| **Batch Generation** | Generate multiple passwords |
| **Breach Check** | Check against breach databases |

## 🚀 Quick Start

```bash
# Clone
git clone https://github.com/0xvanguard/passgenpro.git
cd passgenpro

# Generate random password
python cli.py random --length 20

# Generate passphrase
python cli.py passphrase --words 6

# Generate PIN
python cli.py pin --length 6

# Check password strength
python cli.py check "MyPassword123!"

# Generate batch
python cli.py batch --count 5
```

## 💻 Python API

```python
from passgenpro import PassGen

gen = PassGen()

# Random password
password = gen.random(length=20)
print(f"Password: {password.password}")
print(f"Entropy: {password.entropy} bits")
print(f"Strength: {password.strength_bar}")
print(f"Crack Time: {password.crack_time}")

# Passphrase
passphrase = gen.passphrase(words=6)
print(f"Passphrase: {passphrase.password}")

# PIN
pin = gen.pin(length=6)
print(f"PIN: {pin.password}")

# Check strength
result = gen.check_strength("MyPassword123!")
print(f"Strength: {result.strength}")
print(f"Score: {result.strength_score}/100")

# Batch generation
passwords = gen.random_batch(count=5, length=16)
for p in passwords:
    print(f"{p.password} [{p.strength}]")
```

## 📊 Strength Levels

| Level | Score | Description |
|-------|-------|-------------|
| **VERY_STRONG** | 80-100 | Excellent security |
| **STRONG** | 60-79 | Good security |
| **FAIR** | 40-59 | Moderate security |
| **WEAK** | 20-39 | Poor security |
| **VERY_WEAK** | 0-19 | No security |

## 📁 Project Structure

```
passgenpro/
├── src/
│   ├── __init__.py
│   └── generator.py          # Core generator (500+ lines)
├── tests/
│   ├── __init__.py
│   └── test_generator.py     # 15 tests
├── cli.py                    # CLI tool
├── requirements.txt
└── README.md
```

## 🧪 Tests

```bash
python -m pytest tests/ -v
```

## 📄 License

MIT License — Generate secure passwords.

---

<div align="center">

**Built by [@0xvanguard](https://github.com/0xvanguard)** • [⭐ Star this repo](https://github.com/0xvanguard/passgenpro) • [🐛 Report Bug](https://github.com/0xvanguard/passgenpro/issues)

</div>
