<div align="center">

# 🔐 PassGen Pro

### Password Generator with Visual Entropy Display

![Version](https://img.shields.io/badge/version-1.0.0-blue)
![Python](https://img.shields.io/badge/python-3.8+-green)
![License](https://img.shields.io/badge/license-MIT-yellow)
![Entropy](https://img.shields.io/badge/entropy-128--bit-green)

**Generate secure passwords** with visual entropy analysis and strength scoring.

[PassGen Pro](https://github.com/0xvanguard/passgenpro) • [Try It Live](#quick-start) • [Features](#features)

</div>

---

## 🔐 What is PassGen Pro?

PassGen Pro is a **password generator** with visual entropy display, strength analysis, and breach checking. It helps users create and evaluate strong passwords.

### Why PassGen Pro?

| Without PassGen Pro | With PassGen Pro |
|---------------------|------------------|
| Weak passwords | **Cryptographically secure** |
| No strength visualization | **Visual entropy display** |
| No breach checking | **Breach database check** |
| Hard to remember | **Passphrase generation** |

## 🔍 Features

| Feature | Description |
|---------|-------------|
| **Random Generation** | Cryptographically secure passwords |
| **Passphrase Generation** | BIP39 word-based passphrases |
| **Entropy Display** | Visual entropy bar and score |
| **Breach Check** | Check against HaveIBeenPwned |
| **Custom Rules** | Define password requirements |
| **History** | Track generated passwords |

## 🚀 Quick Start

```bash
# Install
pip install passgenpro

# Or from source
git clone https://github.com/0xvanguard/passgenpro.git
cd passgenpro
pip install -e .
```

```python
from passgenpro import Generator

gen = Generator()

# Generate random password
password = gen.random(length=20)
print(f"Password: {password}")
print(f"Entropy: {password.entropy} bits")
print(f"Strength: {password.strength}")  # Visual bar

# Generate passphrase
passphrase = gen.passphrase(words=6)
print(f"Passphrase: {passphrase}")

# Check if breached
is_breached = gen.check_breach(password)
print(f"Breached: {is_breached}")
```

## 💻 Advanced Usage

```python
from passgenpro import AdvancedGenerator

gen = AdvancedGenerator()

# Custom rules
password = gen.generate(
    length=24,
    uppercase=True,
    lowercase=True,
    digits=True,
    symbols=True,
    exclude_similar=True,
    exclude_ambiguous=True
)

# Batch generation
passwords = gen.batch(count=10, length=20)

# Export
gen.export(passwords, format="csv", file="passwords.csv")
```

## 📊 Entropy Visualization

```
Password: J#8kL$mN2pQ!rT5vX@yZ
Length: 20 characters
Entropy: 128.5 bits
Strength: [████████████████████] Excellent
Time to crack: 10^38 years
```

## 📁 Project Structure

```
passgenpro/
├── src/
│   ├── __init__.py
│   └── generator.py           # Core generator
├── data/
│   └── wordlists.json         # BIP39 wordlists
├── examples/
│   └── quick_generate.py      # Getting started
└── README.md
```

## 📄 License

MIT License — Generate secure passwords.

---

<div align="center">

**Built by [@0xvanguard](https://github.com/0xvanguard)** • [⭐ Star this repo](https://github.com/0xvanguard/passgenpro) • [🐛 Report Bug](https://github.com/0xvanguard/passgenpro/issues)

</div>
