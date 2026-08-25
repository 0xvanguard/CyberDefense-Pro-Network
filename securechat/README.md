<div align="center">

# 💬 SecureChat

### End-to-End Encrypted Messaging with Perfect Forward Secrecy

![Version](https://img.shields.io/badge/version-1.0.0-blue)
![Python](https://img.shields.io/badge/python-3.8+-green)
![License](https://img.shields.io/badge/license-MIT-yellow)
![Encryption](https://img.shields.io/badge/encryption-E2E--PFS-green)

**Chat securely** with end-to-end encryption and perfect forward secrecy.

[SecureChat](https://github.com/0xvanguard/securechat) • [Try It Live](#quick-start) • [Features](#features)

</div>

---

## 💬 What is SecureChat?

SecureChat is an **end-to-end encrypted messaging application** with perfect forward secrecy, disappearing messages, and secure file sharing.

### Why SecureChat?

| Without SecureChat | With SecureChat |
|--------------------|-----------------|
| Unencrypted messages | **E2E encryption** |
| No forward secrecy | **PFS protection** |
| Message history | **Disappearing messages** |
| No file sharing | **Secure file transfer** |

## 🔐 Features

| Feature | Description |
|---------|-------------|
| **E2E Encryption** | Signal Protocol |
| **Perfect Forward Secrecy** | Session key rotation |
| **Disappearing Messages** | Auto-delete after time |
| **Secure File Sharing** | Encrypted file transfer |
| **Group Chat** | Multi-person encrypted chat |

## 🚀 Quick Start

```bash
# Install
pip install securechat

# Start server
securechat serve --port 8080
```

## 💻 Programmatic Usage

```python
from securechat import SecureMessenger

messenger = SecureMessenger()

# Create account
account = messenger.create_account("alice")

# Send message
messenger.send(
    to="bob",
    message="Hello, Bob!"
)

# Receive messages
messages = messenger.receive()
for msg in messages:
    print(f"From: {msg.sender}")
    print(f"Message: {msg.content}")
```

## 📁 Project Structure

```
securechat/
├── src/
│   ├── __init__.py
│   └── chat.py                # Core chat engine
├── data/
│   └── defaults.json          # Default settings
├── examples/
│   └── quick_start.py         # Getting started
└── README.md
```

## 📄 License

MIT License — Chat securely.

---

<div align="center">

**Built by [@0xvanguard](https://github.com/0xvanguard)** • [⭐ Star this repo](https://github.com/0xvanguard/securechat) • [🐛 Report Bug](https://github.com/0xvanguard/securechat/issues)

</div>
