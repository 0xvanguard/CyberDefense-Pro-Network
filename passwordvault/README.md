<p align="center">
  <img src="https://img.shields.io/badge/version-2.0.0-blue?style=for-the-badge">
  <img src="https://img.shields.io/badge/python-3.10+-yellow?style=for-the-badge&logo=python&logoColor=white">
  <img src="https://img.shields.io/badge/license-MIT-green?style=for-the-badge">
  <img src="https://img.shields.io/badge/tests-32-passing-brightgreen?style=for-the-badge">
  <img src="https://img.shields.io/badge/encryption-AES--256-brightgreen?style=for-the-badge">
  <img src="https://img.shields.io/github/stars/0xvanguard/passwordvault?style=for-the-badge">
</p>

# 🔐 PasswordVault

**Zero-Knowledge Password Manager — AES-256 encrypted with strength analysis.**

PasswordVault provides military-grade AES-256 encryption for your passwords. Features include automatic strength analysis, breach detection, secure generation, passphrases, categories, and encrypted backup.

## ✨ Features

| Feature | Description |
|---------|-------------|
| **AES-256 Encryption** | PBKDF2 key derivation, 480K iterations |
| **Strength Analysis** | Entropy, crack time, feature detection |
| **Secure Generator** | Configurable password generation |
| **Passphrase Generator** | BIP39-style word passphrases |
| **Categories** | Organize passwords by type |
| **Favorites** | Star frequently used entries |
| **Encrypted Backup** | Full vault export/restore |
| **Statistics** | Strength distribution, category counts |

## 🚀 Quick Start

```bash
pip install -r requirements.txt

# Generate a password
python cli.py generate --length 20

# Analyze strength
python cli.py strength --password "MyPassword123!"

# Generate passphrase
python cli.py passphrase --words 5

# Add entry
python cli.py add -s github.com -u user@email.com -p mypass

# List entries
python cli.py list

# Statistics
python cli.py stats
```

## 🐍 Python API

```python
from src.vault import PasswordVault

vault = PasswordVault(master_password="my-secret")

# Add
entry = vault.add(service="github.com", username="user@email.com", password="mypass")

# Decrypt
password = vault.get_password(entry.id)

# Strength analysis
strength = vault.analyze_password("MyPassword123!")
print(f"Score: {strength.score}/100 ({strength.label})")
print(f"Crack time: {strength.crack_time}")

# Generate
pw = vault.generate_password(length=20)
pp = vault.generate_passphrase(words=5)
```

## 📁 Structure

```
passwordvault/
├── src/
│   ├── __init__.py
│   └── vault.py            # Core engine + encryption + strength
├── tests/
│   └── test_vault.py       # 32 tests
├── cli.py                  # CLI tool
├── requirements.txt
└── README.md
```

## 📄 License

MIT License — see [LICENSE](LICENSE)
