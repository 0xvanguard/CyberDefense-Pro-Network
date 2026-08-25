"""
Commands: generate — READMEs, portfolio, reports
"""

import os
import json
from datetime import datetime

from src.repos import REPOS, CATEGORIES, GITHUB_USER
from utils.github import get_repos_from_github, get_repo_info, get_repo_stats
from utils.display import (
    C, print_header, print_subheader, print_success, print_error,
    print_warning, print_info, print_progress,
)


def generate_readme_for_repo(repo_name: str) -> str:
    """Generate a README.md for a specific repo."""
    data = REPOS.get(repo_name)
    if not data:
        return None

    url = f"https://github.com/{GITHUB_USER}/{repo_name}"
    tags_badge = " ".join([f"`{t}`" for t in data["tags"]])

    readme = f"""# {data['name']}

> {data['description']}

![Category](https://img.shields.io/badge/category-{data['category'].replace('-', '%20')}-blue)
![Language](https://img.shields.io/badge/language-{data['language']}-orange)
![License](https://img.shields.io/badge/license-MIT-green)

## 🔍 Overview

{data['name']} is part of the [0xvanguard](https://github.com/{GITHUB_USER}) cybersecurity toolkit — 35 open source tools protecting the world.

## 🚀 Quick Start

```bash
# Clone
git clone {url}.git
cd {repo_name}

# Install
pip install -e .
# or
npm install

# Run
python -m {repo_name}
```

## 📦 What's Inside

- **Core functionality** for {data['tags'][0] if data['tags'] else 'security'}
- **CLI interface** for easy integration
- **Python API** for programmatic access
- **Documentation** and examples

## 🏷️ Tags

{tags_badge}

## 📊 Stats

| Metric | Value |
|--------|-------|
| Category | {data['category']} |
| Language | {data['language']} |
| Priority | {'🔴 High' if data['priority'] == 1 else '🟡 Medium'} |

## 🔗 Links

- [GitHub Repository]({url})
- [Report Issues]({url}/issues)
- [Contributing]({url}/blob/main/CONTRIBUTING.md)

## 📄 License

MIT License — use freely, contribute back.

---

*Part of the [0xvanguard Cybersecurity Arsenal](https://github.com/{GITHUB_USER})*
"""
    return readme


def cmd_generate_readme(args):
    """Generate README.md for repos."""
    target = args.get("target", "all")
    output_dir = args.get("output", ".")

    print_header("📝 Generating READMEs")

    targets = []
    if target == "all":
        targets = list(REPOS.keys())
    elif target in REPOS:
        targets = [target]
    elif target in CATEGORIES:
        targets = CATEGORIES[target]["repos"]
    else:
        print_error(f"Unknown target: {target}")
        return

    for i, repo_name in enumerate(targets):
        print_progress(i + 1, len(targets), f"Generating {repo_name}...")

        readme = generate_readme_for_repo(repo_name)
        if readme:
            readme_path = os.path.join(output_dir, f"{repo_name}-README.md")
            with open(readme_path, "w") as f:
                f.write(readme)
            print_success(f"{repo_name}-README.md")
        else:
            print_warning(f"Skipped {repo_name}")

    print(f"\n  {C.GREEN}✓ Generated {len(targets)} READMEs{C.RESET}")


def cmd_generate_report(args):
    """Generate an overall portfolio report."""
    output = args.get("output", "PORTFOLIO_REPORT.md")

    print_header("📊 Generating Portfolio Report")

    # Get stats
    print_subheader("Fetching GitHub stats...")
    stats = get_repo_stats()

    # Build report
    now = datetime.now().strftime("%Y-%m-%d %H:%M")

    report = f"""# 🛡️ 0xvanguard — Portfolio Report

> Generated on {now} by `0xvanguard-cli`

## 📊 Overview

| Metric | Value |
|--------|-------|
| Total Repos | {stats.get('total_repos', len(REPOS))} |
| Total Stars | ⭐ {stats.get('total_stars', 0)} |
| Total Forks | 🍴 {stats.get('total_forks', 0)} |
| Categories | {len(CATEGORIES)} |
| GitHub User | [@{GITHUB_USER}](https://github.com/{GITHUB_USER}) |

## 📂 Categories

"""

    for cat_key, cat_data in CATEGORIES.items():
        repos = [(name, REPOS[name]) for name in cat_data["repos"] if name in REPOS]
        report += f"### {cat_data['name']}\n\n"
        report += f"| Repo | Description | Language | Priority |\n"
        report += f"|------|-------------|----------|----------|\n"
        for name, data in repos:
            priority = "🔴" if data["priority"] == 1 else "🟡"
            report += f"| [{name}](https://github.com/{GITHUB_USER}/{name}) | {data['description'][:50]} | {data['language']} | {priority} |\n"
        report += "\n"

    # Language breakdown
    if stats.get("languages"):
        report += "## 🔧 Languages\n\n"
        report += "| Language | Repos |\n"
        report += "|----------|-------|\n"
        for lang, count in sorted(stats["languages"].items(), key=lambda x: -x[1]):
            report += f"| {lang} | {count} |\n"
        report += "\n"

    # Top topics
    if stats.get("top_topics"):
        report += "## 🏷️ Top Topics\n\n"
        report += ", ".join([f"`{t}`" for t in list(stats["top_topics"].keys())[:15]])
        report += "\n\n"

    report += f"""## 🚀 Quick Start

```bash
# Install the CLI
pip install 0xvanguard-cli

# List all repos
0xv list

# Search
0xv search "encryption"

# Audit all repos
0xv audit

# Generate this report
0xv report
```

## 📄 License

MIT License

---

*Protecting the world, one repo at a time.* 🛡️
"""

    with open(output, "w") as f:
        f.write(report)

    print_success(f"Report saved to {output}")
    print(f"  {C.DIM}{len(report)} characters, {report.count(chr(10))} lines{C.RESET}")
