<div align="center">

# 📝 SecureNotes

### Encrypted Notes with AI-Powered Organization

![Version](https://img.shields.io/badge/version-1.0.0-blue)
![Python](https://img.shields.io/badge/python-3.8+-green)
![License](https://img.shields.io/badge/license-MIT-yellow)
![Encryption](https://img.shields.io/badge/encryption-AES--256-green)

**Take notes securely** with end-to-end encryption and AI-powered organization.

[SecureNotes](https://github.com/0xvanguard/securenotes) • [Try It Live](#quick-start) • [Features](#features)

</div>

---

## 📝 What is SecureNotes?

SecureNotes is an **encrypted note-taking application** with AI-powered organization, tagging, and search capabilities. Your notes stay private with AES-256 encryption.

### Why SecureNotes?

| Without SecureNotes | With SecureNotes |
|---------------------|------------------|
| Unencrypted notes | **AES-256 encryption** |
| Manual organization | **AI-powered tagging** |
| No search | **Encrypted search** |
| Sync issues | **Cross-device sync** |

## 🔐 Features

| Feature | Description |
|---------|-------------|
| **E2E Encryption** | AES-256 encryption |
| **AI Tagging** | Automatic note categorization |
| **Encrypted Search** | Search without decryption |
| **Cross-device Sync** | Sync across devices |
| **Secure Sharing** | Share encrypted notes |

## 🚀 Quick Start

```bash
# Install
pip install securenotes

# Start app
securenotes start
```

## 💻 Programmatic Usage

```python
from securenotes import SecureNotebook

notebook = SecureNotebook(master_password="my_password")

# Create note
note = notebook.create(
    title="Meeting Notes",
    content="Discussed Q4 security strategy...",
    tags=["meeting", "security"]
)

# Search notes
results = notebook.search("security strategy")
print(f"Found {len(results)} notes")

# Export encrypted
notebook.export("backup.enc")
```

## 📁 Project Structure

```
securenotes/
├── src/
│   ├── __init__.py
│   └── notes.py               # Core notes engine
├── data/
│   └── defaults.json          # Default settings
├── examples/
│   └── quick_start.py         # Getting started
└── README.md
```

## 📄 License

MIT License — Take secure notes.

---

<div align="center">

**Built by [@0xvanguard](https://github.com/0xvanguard)** • [⭐ Star this repo](https://github.com/0xvanguard/securenotes) • [🐛 Report Bug](https://github.com/0xvanguard/securenotes/issues)

</div>
