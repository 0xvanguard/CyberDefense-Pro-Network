<p align="center">
  <img src="https://img.shields.io/badge/version-2.0.0-blue?style=for-the-badge">
  <img src="https://img.shields.io/badge/python-3.10+-yellow?style=for-the-badge&logo=python&logoColor=white">
  <img src="https://img.shields.io/badge/license-MIT-green?style=for-the-badge">
  <img src="https://img.shields.io/badge/tests-29-passing-brightgreen?style=for-the-badge">
  <img src="https://img.shields.io/badge/encryption-ECDH+AES--256--GCM-brightgreen?style=for-the-badge">
  <img src="https://img.shields.io/github/stars/0xvanguard/securechat?style=for-the-badge">
</p>

# 💬 SecureChat

**End-to-End Encrypted Messaging — ECDH key exchange + AES-256-GCM.**

SecureChat provides military-grade E2E encryption using ECDH key exchange and AES-256-GCM. Supports direct messages, group chats, reactions, message editing, and read receipts.

## ✨ Features

| Feature | Description |
|---------|-------------|
| **E2E Encryption** | ECDH + AES-256-GCM |
| **Direct Messages** | 1:1 encrypted conversations |
| **Group Chats** | Up to 100 members per room |
| **Reactions** | React to messages |
| **Read Receipts** | Track message reads |
| **Message Editing** | Edit sent messages |
| **Message Expiry** | Self-destructing messages |
| **File Sharing** | Encrypted file transfer simulation |

## 🚀 Quick Start

```bash
pip install -r requirements.txt

# Demo
python cli.py demo

# Create users
python cli.py user --name Alice
python cli.py user --name Bob

# Send message
python cli.py send --from Alice --to Bob --message "Hello!"

# Create room
python cli.py room --create "Secret Group" --name Alice

# Stats
python cli.py stats --name Alice
```

## 🐍 Python API

```python
from src.chat import SecureChat

alice = SecureChat(name="Alice")
bob = SecureChat(name="Bob")

# Send encrypted message
encrypted = alice.send(bob.get_public_key(), "Hello Bob!")
decrypted = bob.receive(alice.get_public_key(), encrypted)
print(decrypted)  # "Hello Bob!"

# Group chat
room = alice.create_room("Secret Group", members=["Bob"])
alice.send_room_message(room.id, "Hello everyone!")
```

## 📁 Structure

```
securechat/
├── src/
│   ├── __init__.py
│   └── chat.py            # Core engine + E2E encryption
├── tests/
│   └── test_chat.py       # 29 tests
├── cli.py                 # CLI tool
├── requirements.txt
└── README.md
```

## 📄 License

MIT License — see [LICENSE](LICENSE)
