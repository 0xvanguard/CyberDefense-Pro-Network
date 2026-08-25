<div align="center">

# 🛡️ 0xv CLI

### The Unified Command Line Interface for All 0xvanguard Security Projects

![Version](https://img.shields.io/badge/version-1.0.0-blue)
![Python](https://img.shields.io/badge/python-3.8+-green)
![License](https://img.shields.io/badge/license-MIT-yellow)
![Projects](https://img.shields.io/badge/projects-46-red)

**Manage, audit, and monitor all 46 security projects** from a single terminal.

[0xv CLI](https://github.com/0xvanguard/0xvanguard-cli) • [Try It Live](#quick-start) • [Commands](#commands)

</div>

---

## 🛡️ What is 0xv CLI?

0xv CLI is a **unified command line interface** that provides a single entry point to manage, audit, and monitor all 0xvanguard security projects.

### Why 0xv CLI?

| Without 0xv CLI | With 0xv CLI |
|-----------------|--------------|
| Manual repo management | **Automated management** |
| No portfolio view | **Unified dashboard** |
| Manual security checks | **Automated auditing** |
| No reporting | **Built-in reports** |

## 📋 Commands

| Command | Description |
|---------|-------------|
| `0xv list` | List all 46 projects |
| `0xv info <project>` | Get project details |
| `0xv audit <project>` | Security audit project |
| `0xv sync` | Sync all repos |
| `0xv report` | Generate portfolio report |
| `0xv search <query>` | Search projects |

## 🚀 Quick Start

```bash
# Install
git clone https://github.com/0xvanguard/0xvanguard-cli.git
cd 0xvanguard-cli
pip install -e .

# List all projects
0xv list

# Get project info
0xv info promptkiller

# Audit project
0xv audit promptkiller

# Generate report
0xv report
```

## 💻 Advanced Usage

```bash
# Search projects
0xv search "encryption"

# Audit all projects
0xv audit all

# Generate portfolio HTML
0xv report --format html --output portfolio.html

# Sync all repos
0xv sync --pull
```

## 📊 Project Statistics

| Category | Count |
|----------|-------|
| **AI Security** | 14 |
| **Security Tools** | 9 |
| **Education** | 9 |
| **Productivity** | 10 |
| **AI for Good** | 3 |
| **Total** | **46** |

## 📁 Project Structure

```
0xvanguard-cli/
├── src/
│   ├── __init__.py
│   └── repos.py               # Project registry
├── commands/
│   ├── repos_cmd.py           # List/info commands
│   ├── audit_cmd.py           # Security audit
│   ├── sync_cmd.py            # Sync commands
│   └── generate_cmd.py        # Report generation
├── utils/
│   ├── github.py              # GitHub API
│   └── display.py             # Display utilities
├── 0xv                        # CLI entry point
├── setup.py                   # Package setup
└── README.md
```

## 📄 License

MIT License — Manage your projects.

---

<div align="center">

**Built by [@0xvanguard](https://github.com/0xvanguard)** • [⭐ Star this repo](https://github.com/0xvanguard/0xvanguard-cli) • [🐛 Report Bug](https://github.com/0xvanguard/0xvanguard-cli/issues)

</div>
