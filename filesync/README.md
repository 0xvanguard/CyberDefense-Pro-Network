<div align="center">

# 📁 FileSync

### Secure File Synchronization with Encryption

![Version](https://img.shields.io/badge/version-1.0.0-blue)
![Python](https://img.shields.io/badge/python-3.8+-green)
![License](https://img.shields.io/badge/license-MIT-yellow)
![Encryption](https://img.shields.io/badge/encryption-E2E-green)

**Sync files securely** across devices with end-to-end encryption.

[FileSync](https://github.com/0xvanguard/filesync) • [Try It Live](#quick-start) • [Features](#features)

</div>

---

## 📁 What is FileSync?

FileSync is a **secure file synchronization tool** that syncs files across devices with end-to-end encryption and conflict resolution.

### Why FileSync?

| Without FileSync | With FileSync |
|------------------|---------------|
| Unencrypted sync | **E2E encryption** |
| No conflict resolution | **Smart merging** |
| No versioning | **File versioning** |
| No selective sync | **Selective sync** |

## ⚡ Features

| Feature | Description |
|---------|-------------|
| **E2E Encryption** | Files encrypted before sync |
| **Conflict Resolution** | Smart file merging |
| **Versioning** | Keep file history |
| **Selective Sync** | Choose what to sync |
| **Cross-platform** | Windows, Mac, Linux |

## 🚀 Quick Start

```bash
# Install
pip install filesync

# Start sync
filesync start --folder ~/Documents
```

## 💻 Programmatic Usage

```python
from filesync import SyncEngine

sync = SyncEngine()

# Add folder
sync.add_folder(
    path="~/Documents",
    encrypted=True,
    versioning=True
)

# Start sync
sync.start()

# Check status
status = sync.status()
print(f"Synced files: {status.synced}")
print(f"Pending: {status.pending}")
print(f"Conflicts: {status.conflicts}")
```

## 📁 Project Structure

```
filesync/
├── src/
│   ├── __init__.py
│   └── sync.py                # Core sync engine
├── data/
│   └── defaults.json          # Default settings
├── examples/
│   └── quick_sync.py          # Getting started
└── README.md
```

## 📄 License

MIT License — Sync files securely.

---

<div align="center">

**Built by [@0xvanguard](https://github.com/0xvanguard)** • [⭐ Star this repo](https://github.com/0xvanguard/filesync) • [🐛 Report Bug](https://github.com/0xvanguard/filesync/issues)

</div>
