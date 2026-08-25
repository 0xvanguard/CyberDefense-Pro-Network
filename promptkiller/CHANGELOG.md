# Changelog

All notable changes to PromptKiller will be documented in this file.

## [2.0.0] - 2026-08-25

### Added
- 500+ built-in attack prompts across 15 categories
- CLI tool with `list`, `search`, `random`, `scan`, `show`, `stats`, `export` commands
- Attack scanning with pattern detection
- Benchmarking framework for testing against LLMs
- Export to JSON, CSV, and TXT formats
- Custom prompt support
- Comprehensive test suite
- Docker support
- CONTRIBUTING.md and CHANGELOG.md

### Categories
- Role Play (15 prompts)
- Injection (15 prompts)
- Encoding (15 prompts)
- Jailbreak (15 prompts)
- Extraction (15 prompts)
- Adversarial (15 prompts)
- Manipulation (15 prompts)
- Context (15 prompts)
- Multi-turn (15 prompts)
- Multilingual (15 prompts)
- Token Smuggling (15 prompts)
- Persona (15 prompts)
- Tool Abuse (15 prompts)
- Reasoning (15 prompts)
- Meta (15 prompts)

### Features
- `PromptKiller` class with full API
- `AttackPrompt` dataclass for structured prompts
- `ScanResult` dataclass for scan results
- Category-based organization
- Severity-based filtering
- Effectiveness scoring
- Search by keyword, name, tag
- Random prompt selection
- Export functionality
- Attack pattern detection

## [1.0.0] - 2026-08-24

### Added
- Initial release
- Basic prompt library
- README with documentation
