<div align="center">

# 🧩 CryptoPuzzles

### Learn Cryptography by Breaking It

![Version](https://img.shields.io/badge/version-1.0.0-blue)
![Python](https://img.shields.io/badge/python-3.8+-green)
![License](https://img.shields.io/badge/license-MIT-yellow)
![Puzzles](https://img.shields.io/badge/puzzles-50+-purple)

**Interactive cryptography puzzles** that teach crypto through hands-on challenges.

[CryptoPuzzles](https://github.com/0xvanguard/cryptopuzzles) • [Try It Live](#quick-start) • [Puzzles](#puzzle-categories)

</div>

---

## 🧩 What is CryptoPuzzles?

CryptoPuzzles is an **educational cryptography platform** that teaches crypto concepts through interactive puzzles and challenges. Learn by breaking real crypto implementations.

### Why CryptoPuzzles?

| Traditional Learning | With CryptoPuzzles |
|---------------------|-------------------|
| Theoretical only | **Hands-on puzzles** |
| No practice | **50+ challenges** |
| Boring lectures | **Gamified learning** |
| No feedback | **Instant validation** |

## 🎯 Puzzle Categories

| Category | Puzzles | Difficulty |
|----------|---------|------------|
| **Classical** | 10 | Beginner |
| **Symmetric** | 12 | Intermediate |
| **Asymmetric** | 10 | Intermediate |
| **Hashing** | 8 | Beginner |
| **Attacks** | 10 | Advanced |

## 🚀 Quick Start

```bash
# Install
pip install cryptopuzzles

# Start puzzles
cryptopuzzles play
```

## 💻 Puzzle Example

```python
from cryptopuzzles import PuzzleEngine

engine = PuzzleEngine()

# Get a puzzle
puzzle = engine.get_puzzle("caesar_shift")
print(f"Challenge: {puzzle.ciphertext}")

# Submit solution
result = engine.solve(puzzle.id, "HELLO")
print(f"Correct: {result.correct}")
print(f"XP: {result.xp}")
```

## 📁 Project Structure

```
cryptopuzzles/
├── src/
│   ├── __init__.py
│   └── puzzles.py             # Core engine
├── data/
│   └── puzzles.json           # Puzzle definitions
├── examples/
│   └── quick_play.py          # Getting started
└── README.md
```

## 📄 License

MIT License — Learn cryptography.

---

<div align="center">

**Built by [@0xvanguard](https://github.com/0xvanguard)** • [⭐ Star this repo](https://github.com/0xvanguard/cryptopuzzles) • [🐛 Report Bug](https://github.com/0xvanguard/cryptopuzzles/issues)

</div>
