# 0xv — 0xvanguard Cybersecurity CLI

> **35 tools. One empire. One terminal.**

A command-line tool to manage, audit, search, and sync all 35 repos in the [0xvanguard](https://github.com/0xvanguard) cybersecurity arsenal.

## ⚡ Quick Start

```bash
# Clone this repo
git clone https://github.com/0xvanguard/0xvanguard-cli.git
cd 0xvanguard-cli

# Run directly
python3 0xv help

# Or install globally
chmod +x 0xv
sudo cp 0xv /usr/local/bin/

# Now run from anywhere
0xv help
```

## 📋 Commands

| Command | Description |
|---------|-------------|
| `0xv list` | List all 35 repos by category |
| `0xv list --category ai-security` | Filter by category |
| `0xv search <query>` | Search repos by name, description, or tags |
| `0xv info <repo>` | Show detailed info about a repo |
| `0xv status` | Show portfolio status (local vs GitHub) |
| `0xv categories` | List all categories with repos |
| `0xv audit` | Security scan — find hardcoded secrets, XSS, etc. |
| `0xv audit <repo>` | Audit a specific repo |
| `0xv sync status` | Check sync status with GitHub |
| `0xv sync create-missing` | Create repos on GitHub that are missing |
| `0xv readme all` | Generate README.md for all repos |
| `0xv report` | Generate full portfolio report |

## 🛡️ Security Audit

Scans for 10 vulnerability patterns:

| Pattern | Severity | Description |
|---------|----------|-------------|
| Hardcoded secrets | 🔴 HIGH | API keys, tokens, passwords in code |
| eval() usage | 🔴 HIGH | Code injection risk |
| SQL injection | 🔴 HIGH | String interpolation in queries |
| Unsafe deserialization | 🔴 HIGH | Pickle.loads usage |
| innerHTML | 🟡 MEDIUM | XSS risk in JavaScript |
| Insecure HTTP | 🟡 MEDIUM | URLs should use HTTPS |
| Weak crypto | 🟡 MEDIUM | MD5/SHA1 usage |
| CORS wildcard | 🟡 MEDIUM | Allow any origin |
| Open redirect | 🟡 MEDIUM | User-controlled redirects |
| Debug mode | ⚪ LOW | Debug enabled in code |

### Example

```bash
# Audit everything
0xv audit all

# Only HIGH severity
0xv audit all --severity HIGH

# Audit one category
0xv audit ai-security

# Audit one repo
0xv audit promptkiller
```

## 📂 Categories

| Category | Color | Repos |
|----------|-------|-------|
| 🛡️ AI Security | Red | medscan, promptkiller, jailbreakbench, guarddog, constitutionalkit, injectionmapper, redteamos |
| 🔐 Security Tools | Blue | vulnseeker, zerotrustkit, passgenpro, threatmap, riskcalculator |
| 📚 Education | Green | cyberlabs, ctf-builder, hacktheclass, cybermentor, cryptopuzzles, securecoding101, threatmodeler, vulnviz, policywriter |
| ⚡ Productivity | Yellow | securenotes, passwordvault, securechat, privacyvpn, emailguard, filesync, backupcloud, devsecops, codesigning, iotsentinel |
| 💚 AI for Good | Cyan | agribot, languagepreserver, disasterrelief |

## 🔧 Requirements

- Python 3.8+
- `gh` CLI authenticated (for GitHub operations)
- No pip dependencies — pure Python stdlib

## 📁 Structure

```
0xvanguard-cli/
├── 0xv                 ← Main CLI (run directly)
├── cli.py              ← Entry point wrapper
├── setup.py            ← pip install support
├── README.md           ← This file
├── src/
│   ├── repos.py        ← Registry of 35 repos
│   └── categories.py   ← Category definitions
├── commands/
│   ├── repos_cmd.py    ← list, search, info, status
│   ├── audit_cmd.py    ← Security scanning
│   ├── generate_cmd.py ← README & report generation
│   └── sync_cmd.py     ← GitHub sync operations
└── utils/
    ├── display.py      ← Terminal colors & formatting
    └── github.py       ← GitHub API wrapper
```

## 📄 License

MIT

---

*Protecting the world, one command at a time.* 🛡️
