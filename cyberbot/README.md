<div align="center">

# 🤖 CyberBot

### Interactive Cybersecurity Training Chatbot

![Version](https://img.shields.io/badge/version-1.0.0-blue)
![Python](https://img.shields.io/badge/python-3.8+-green)
![License](https://img.shields.io/badge/license-MIT-yellow)
![Topics](https://img.shields.io/badge/topics-50+-purple)

**Learn cybersecurity through conversation** — an AI tutor that teaches, tests, and guides.

[CyberBot](https://github.com/0xvanguard/cyberbot) • [Try It Live](#quick-start) • [Topics](#training-topics)

</div>

---

## 🤖 What is CyberBot?

CyberBot is an **AI-powered cybersecurity training chatbot** that teaches security concepts through interactive conversations, quizzes, and hands-on exercises.

### Why CyberBot?

| Traditional Learning | With CyberBot |
|---------------------|---------------|
| Passive reading | **Interactive conversations** |
| No feedback | **Instant explanations** |
| Generic content | **Personalized learning** |
| No practice | **Hands-on exercises** |

## 📚 Training Topics

| Module | Topics | Difficulty |
|--------|--------|------------|
| **Network Security** | Firewalls, IDS/IPS, VPN | Beginner |
| **Web Security** | OWASP Top 10, XSS, SQLi | Intermediate |
| **Cryptography** | Hashing, encryption, PKI | Intermediate |
| **Malware Analysis** | Static/dynamic analysis | Advanced |
| **Penetration Testing** | Recon, exploitation, post-exploitation | Advanced |
| **Incident Response** | Detection, containment, recovery | Intermediate |
| **Cloud Security** | AWS/Azure/GCP security | Intermediate |
| **AI Security** | Prompt injection, jailbreaks | Advanced |

## 🚀 Quick Start

```bash
# Install
pip install cyberbot

# Start chatbot
cyberbot chat

# Or run specific module
cyberbot module --topic "web-security"
```

## 💻 Interactive Learning

```python
from cyberbot import CyberBot

# Start learning session
bot = CyberBot(level="intermediate", topic="web-security")

# Ask questions
response = bot.ask("What is XSS?")
print(response)  # Interactive explanation with examples

# Take quiz
quiz = bot.quiz(num_questions=10)
print(f"Score: {quiz.score}/{quiz.total}")

# Get recommendations
next_topic = bot.recommend(current_score=0.75)
print(f"Recommended: {next_topic}")
```

## 🎯 Features

| Feature | Description |
|---------|-------------|
| **Adaptive Learning** | Adjusts difficulty based on performance |
| **Interactive Exercises** | Hands-on coding challenges |
| **Progress Tracking** | Track learning journey |
| **Certifications** | Earn completion certificates |
| **Real-world Scenarios** | Based on actual incidents |

## 📁 Project Structure

```
cyberbot/
├── src/
│   ├── __init__.py
│   └── chatbot.py             # Core chatbot engine
├── data/
│   ├── topics.json            # Training topics
│   └── quizzes.json           # Quiz questions
├── examples/
│   └── quick_start.py         # Getting started
└── README.md
```

## 📄 License

MIT License — Learn cybersecurity.

---

<div align="center">

**Built by [@0xvanguard](https://github.com/0xvanguard)** • [⭐ Star this repo](https://github.com/0xvanguard/cyberbot) • [🐛 Report Bug](https://github.com/0xvanguard/cyberbot/issues)

</div>
