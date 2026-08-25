# Contributing to PromptKiller

Thank you for your interest in contributing to PromptKiller! This document provides guidelines and instructions for contributing.

## 🎯 How to Contribute

### 1. Add New Attack Prompts

The most valuable contribution is adding new, novel attack prompts.

**Format:**
```json
{
  "name": "Attack Name",
  "technique": "technique_id",
  "prompt": "The attack prompt text",
  "description": "What this attack does",
  "severity": "high|medium|low|critical",
  "effectiveness": 0.7,
  "tags": ["tag1", "tag2"]
}
```

**Categories:**
- `role_play` — Persona manipulation
- `injection` — Direct/indirect injection
- `encoding` — Encoding bypasses
- `jailbreak` — Jailbreak techniques
- `extraction` — System prompt extraction
- `adversarial` — Adversarial attacks
- `manipulation` — Social engineering
- `context` — Context window exploitation
- `multi_turn` — Multi-turn attacks
- `multilingual` — Language switching
- `token_smuggling` — Token manipulation
- `persona` — Expert impersonation
- `tool_abuse` — Tool/function abuse
- `reasoning` — Chain-of-thought exploitation
- `meta` — System-level manipulation

### 2. Improve Existing Prompts

- Add variations of existing prompts
- Update effectiveness scores based on testing
- Add references to research papers

### 3. Add Tests

- Write tests for new functionality
- Ensure all tests pass: `pytest tests/ -v`

### 4. Improve Documentation

- Fix typos
- Add examples
- Improve explanations

## 📋 Pull Request Process

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/amazing-feature`
3. Make your changes
4. Add tests if applicable
5. Run tests: `pytest tests/ -v`
6. Commit: `git commit -m 'Add amazing feature'`
7. Push: `git push origin feature/amazing-feature`
8. Open a Pull Request

## 🐛 Reporting Issues

- Use the GitHub issue tracker
- Include steps to reproduce
- Include expected vs actual behavior
- Include Python version and OS

## 📝 Code Style

- Follow PEP 8
- Use type hints
- Add docstrings to new functions
- Keep functions focused and small

## ⚠️ Ethical Guidelines

This project is for **authorized security testing only**. Do not:

- Use these prompts for malicious purposes
- Target systems without authorization
- Share exploits for vulnerable systems

## 📄 License

By contributing, you agree that your contributions will be licensed under the MIT License.
