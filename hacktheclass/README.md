<div align="center">

# 🎓 HackTheClass

### K-12 Cybersecurity Curriculum for Schools

![Version](https://img.shields.io/badge/version-1.0.0-blue)
![Python](https://img.shields.io/badge/python-3.8+-green)
![License](https://img.shields.io/badge/license-MIT-yellow)
![Grades](https://img.shields.io/badge/grades-K--12-green)

**Teach cybersecurity from day one** with age-appropriate curriculum.

[HackTheClass](https://github.com/0xvanguard/hacktheclass) • [Try It Live](#quick-start) • [Curriculum](#curriculum)

</div>

---

## 🎓 What is HackTheClass?

HackTheClass is a **K-12 cybersecurity curriculum** designed to teach students about cybersecurity from elementary through high school with age-appropriate content.

### Why HackTheClass?

| Without HackTheClass | With HackTheClass |
|----------------------|-------------------|
| No security education | **K-12 curriculum** |
| Too technical | **Age-appropriate** |
| No teacher resources | **Teacher guides included** |
| No student engagement | **Interactive activities** |

## 📚 Curriculum

| Grade | Topics | Activities |
|-------|--------|------------|
| **K-2** | Internet safety, passwords | Coloring, games |
| **3-5** | Phishing, privacy | Worksheets, quizzes |
| **6-8** | Network security, encryption | Labs, projects |
| **9-12** | Ethical hacking, forensics | CTFs, competitions |

## 🚀 Quick Start

```bash
# Install
pip install hacktheclass

# View curriculum
hacktheclass view --grade 6
```

## 💻 Teacher Resources

```python
from hacktheclass import Curriculum

curriculum = Curriculum(grade=6)

# Get lessons
lessons = curriculum.get_lessons()
print(f"Found {len(lessons)} lessons")

# Get lesson plan
plan = curriculum.get_lesson_plan("network_security")
print(f"Duration: {plan.duration}")
print(f"Objectives: {plan.objectives}")
print(f"Activities: {plan.activities}")

# Get assessment
assessment = curriculum.get_assessment("network_security")
print(f"Questions: {len(assessment.questions)}")
```

## 📊 Student Engagement

```python
from hacktheclass import StudentTracker

tracker = StudentTracker()

# Track progress
progress = tracker.get_progress(student_id="student_123")
print(f"Completed: {progress.completed}/{progress.total}")
print(f"Score: {progress.average_score}")

# Generate report card
report = tracker.report_card(student_id="student_123")
report.export("report_card.pdf")
```

## 📁 Project Structure

```
hacktheclass/
├── src/
│   ├── __init__.py
│   └── curriculum.py          # Core curriculum
├── data/
│   ├── k-2/                   # Elementary lessons
│   ├── 3-5/                   # Middle school lessons
│   └── 6-12/                  # High school lessons
├── examples/
│   └── quick_start.py         # Getting started
└── README.md
```

## 📄 License

MIT License — Teach cybersecurity.

---

<div align="center">

**Built by [@0xvanguard](https://github.com/0xvanguard)** • [⭐ Star this repo](https://github.com/0xvanguard/hacktheclass) • [🐛 Report Bug](https://github.com/0xvanguard/hacktheclass/issues)

</div>
