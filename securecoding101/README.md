<p align="center">
  <img src="https://img.shields.io/badge/version-2.0.0-blue?style=for-the-badge">
  <img src="https://img.shields.io/badge/python-3.10+-yellow?style=for-the-badge&logo=python&logoColor=white">
  <img src="https://img.shields.io/badge/license-MIT-green?style=for-the-badge">
  <img src="https://img.shields.io/badge/tests-31-passing-brightgreen?style=for-the-badge">
  <img src="https://img.shields.io/badge/lessons-12-blue?style=for-the-badge">
  <img src="https://img.shields.io/github/stars/0xvanguard/securecoding101?style=for-the-badge">
</p>

# 📚 SecureCoding101

**Interactive Secure Coding Course — Learn by fixing real vulnerabilities.**

SecureCoding101 teaches secure coding through 12 hands-on lessons with vulnerable/secure code examples, quizzes, and automated code checking. Covers SQL injection, XSS, CSRF, authentication, cryptography, and more.

## ✨ Features

| Feature | Description |
|---------|-------------|
| **12 Lessons** | SQL injection, XSS, CSRF, auth, crypto, SSRF, etc. |
| **Vulnerable/Secure Code** | Side-by-side examples |
| **Code Checker** | Automated vulnerability detection |
| **Quiz System** | 5 quiz questions with explanations |
| **Progress Tracking** | Points, completion, quiz scores |
| **3 Difficulty Levels** | Beginner, Intermediate, Advanced |
| **8 Categories** | Injection, Web, Auth, Crypto, Validation, etc. |

## 🚀 Quick Start

```bash
pip install -r requirements.txt

# List lessons
python cli.py lessons

# View a lesson
python cli.py lesson sql_injection

# Take a quiz
python cli.py quiz sql_injection --answer 1

# Check your code
python cli.py check sql_injection --code "cursor.execute(query, (username,))"

# Progress
python cli.py progress

# Categories
python cli.py categories
```

## 🐍 Python API

```python
from src.course import SecureCoding

sc = SecureCoding()

# Get a lesson
lesson = sc.get_lesson("sql_injection")
print(lesson.vulnerable_code)
print(lesson.secure_code)

# Check your code
result = sc.check_fix("sql_injection", "cursor.execute(query, (username,))")
print(f"Secure: {result['is_secure']}, Points: {result['points']}")

# Take a quiz
result = sc.answer_quiz("q1", 1)
print(f"Correct: {result['correct']}")
```

## 📚 Lessons

| ID | Topic | Category | Difficulty |
|----|-------|----------|------------|
| sql_injection | SQL Injection | injection | 🟢 Beginner |
| xss_prevention | XSS | web | 🟢 Beginner |
| auth_security | Authentication | auth | 🟡 Intermediate |
| input_validation | Input Validation | validation | 🟢 Beginner |
| crypto_basics | Cryptography | crypto | 🟡 Intermediate |
| csrf_prevention | CSRF | web | 🟡 Intermediate |
| file_upload | File Upload | file_security | 🟡 Intermediate |
| ssrf_prevention | SSRF | network | 🔴 Advanced |
| command_injection | Command Injection | injection | 🟡 Intermediate |
| path_traversal | Path Traversal | file_security | 🟢 Beginner |
| hardcoded_secrets | Hardcoded Secrets | configuration | 🟢 Beginner |
| insecure_deserialization | Deserialization | web | 🔴 Advanced |

## 📁 Structure

```
securecoding101/
├── src/
│   ├── __init__.py
│   └── course.py           # Core engine
├── tests/
│   └── test_course.py      # 31 tests
├── cli.py                  # CLI tool
├── requirements.txt
└── README.md
```

## 📄 License

MIT License — see [LICENSE](LICENSE)
