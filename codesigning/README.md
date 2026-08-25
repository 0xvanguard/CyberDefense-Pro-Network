<div align="center">

# ✍️ CodeSigning

### Code Signing Toolkit for Open Source Projects

![Version](https://img.shields.io/badge/version-1.0.0-blue)
![Python](https://img.shields.io/badge/python-3.8+-green)
![License](https://img.shields.io/badge/license-MIT-yellow)
![Keys](https://img.shields.io/badge/keys-PGP%20SSH-green)

**Sign your code** to prove authenticity and integrity.

[CodeSigning](https://github.com/0xvanguard/codesigning) • [Try It Live](#quick-start) • [Features](#features)

</div>

---

## ✍️ What is CodeSigning?

CodeSigning is a **code signing toolkit** for open source projects that helps verify code authenticity and integrity using PGP and SSH signatures.

### Why CodeSigning?

| Without CodeSigning | With CodeSigning |
|---------------------|------------------|
| No code verification | **Signature verification** |
| Supply chain attacks | **Provenance tracking** |
| No trust chain | **Web of trust** |
| No integrity checks | **Hash verification** |

## 🔐 Features

| Feature | Description |
|---------|-------------|
| **PGP Signing** | GPG signature creation |
| **SSH Signing** | SSH key signatures |
| **Verification** | Signature validation |
| **Trust Chain** | Web of trust management |
| **CI/CD Integration** | Automated signing |

## 🚀 Quick Start

```bash
# Install
pip install codesigning

# Sign a release
codesigning sign --file release.tar.gz --key ~/.ssh/id_rsa
```

## 💻 Programmatic Usage

```python
from codesigning import CodeSigner

signer = CodeSigner(key_path="~/.ssh/id_rsa")

# Sign file
signature = signer.sign("release.tar.gz")
print(f"Signature: {signature.fingerprint}")

# Verify signature
valid = signer.verify("release.tar.gz", "release.tar.gz.sig")
print(f"Valid: {valid}")

# Sign git commit
signer.sign_commit()
```

## 📁 Project Structure

```
codesigning/
├── src/
│   ├── __init__.py
│   └── signing.py             # Core signing engine
├── data/
│   └── defaults.json          # Default settings
├── examples/
│   └── quick_sign.py          # Getting started
└── README.md
```

## 📄 License

MIT License — Sign your code.

---

<div align="center">

**Built by [@0xvanguard](https://github.com/0xvanguard)** • [⭐ Star this repo](https://github.com/0xvanguard/codesigning) • [🐛 Report Bug](https://github.com/0xvanguard/codesigning/issues)

</div>
