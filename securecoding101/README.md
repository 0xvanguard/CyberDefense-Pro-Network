<div align="center">

# 🛡️ SecureCoding101

### Interactive Secure Coding Course

![Version](https://img.shields.io/badge/version-1.0.0-blue)
![Python](https://img.shields.io/badge/python-3.8+-green)
![License](https://img.shields.io/badge/license-MIT-yellow)
![Lessons](https://img.shields.io/badge/lessons-30+-green)

**Learn secure coding practices** through interactive lessons and hands-on exercises.

[SecureCoding101](https://github.com/0xvanguard/securecoding101) • [Try It Live](#quick-start) • [Lessons](#lesson-topics)

</div>

---

## 🛡️ What is SecureCoding101?

SecureCoding101 is an **interactive secure coding course** that teaches developers how to write secure code through practical lessons and exercises.

### Why SecureCoding101?

| Without SecureCoding101 | With SecureCoding101 |
|-------------------------|---------------------|
| Security as afterthought | **Security by design** |
| No hands-on practice | **Interactive exercises** |
| Generic content | **Language-specific** |
| No validation | **Instant feedback** |

## 📚 Lesson Topics

| Module | Lessons | OWASP |
|--------|---------|-------|
| **Input Validation** | 5 | A03 |
| **Authentication** | 5 | A07 |
| **Authorization** | 5 | A01 |
| **Cryptography** | 5 | A02 |
| **Error Handling** | 5 | A09 |
| **Secure Design** | 5 | — |

## 🚀 Quick Start

```bash
# Install
pip install securecoding101

# Start course
securecoding101 learn
```

## 💻 Course Experience

```python
from securecoding101 import Course

course = Course(language="python")

# List lessons
lessons = course.list_lessons()
print(f"Found {len(lessons)} lessons")

# Start lesson
lesson = course.start("input_validation")

# Complete exercise
result = lesson.submit(code)
print(f"Correct: {result.correct}")
print(f"Feedback: {result.feedback}")
```

## 📁 Project Structure

```
securecoding101/
├── src/
│   ├── __init__.py
│   └── course.py              # Core course engine
├── lessons/
│   ├── input_validation/
│   └── authentication/
├── data/
│   └── lessons.json           # Lesson definitions
├── examples/
│   └── quick_learn.py         # Getting started
└── README.md
```

## 📄 License

MIT License — Learn secure coding.

---

<div align="center">

**Built by [@0xvanguard](https://github.com/0xvanguard)** • [⭐ Star this repo](https://github.com/0xvanguard/securecoding101) • [🐛 Report Bug](https://github.com/0xvanguard/securecoding101/issues)

</div>
