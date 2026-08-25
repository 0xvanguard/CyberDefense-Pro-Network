"""
GitHub API wrapper for managing 0xvanguard repos.
Uses the gh CLI for all operations.
"""

import json
import subprocess
from typing import Optional


GITHUB_API = "https://api.github.com"
GITHUB_USER = "0xvanguard"


def _gh_cmd(args: list, capture: bool = True) -> subprocess.CompletedProcess:
    """Run a gh CLI command."""
    cmd = ["gh"] + args
    return subprocess.run(cmd, capture_output=capture, text=True)


def _get_token() -> Optional[str]:
    """Get the current GitHub token from gh auth."""
    result = _gh_cmd(["auth", "token"])
    if result.returncode == 0 and result.stdout.strip():
        return result.stdout.strip()
    return None


def get_repos_from_github() -> list:
    """Fetch all repo names from GitHub for the user."""
    result = _gh_cmd([
        "api", f"users/{GITHUB_USER}/repos",
        "--paginate",
        "--jq", ".[].name"
    ])
    if result.returncode == 0:
        return [r.strip() for r in result.stdout.strip().split("\n") if r.strip()]
    return []


def get_repo_info(repo_name: str) -> dict:
    """Get detailed info about a specific repo."""
    result = _gh_cmd([
        "api", f"repos/{GITHUB_USER}/{repo_name}"
    ])
    if result.returncode == 0:
        try:
            data = json.loads(result.stdout)
            return {
                "name": data.get("name", ""),
                "description": data.get("description", ""),
                "stars": data.get("stargazers_count", 0),
                "forks": data.get("forks_count", 0),
                "language": data.get("language", ""),
                "url": data.get("html_url", ""),
                "created": data.get("created_at", ""),
                "updated": data.get("pushed_at", ""),
                "topics": data.get("topics", []),
            }
        except json.JSONDecodeError:
            return {}
    return {}


def create_repo(name: str, description: str, private: bool = False) -> dict:
    """Create a new GitHub repo."""
    cmd = [
        "repo", "create", f"{GITHUB_USER}/{name}",
        "--description", description,
    ]
    if private:
        cmd.append("--private")
    else:
        cmd.append("--public")

    result = _gh_cmd(cmd, capture=True)
    return {
        "success": result.returncode == 0,
        "output": result.stdout.strip() if result.stdout else result.stderr.strip(),
    }


def get_repo_stats() -> dict:
    """Get aggregate stats for all repos."""
    repos = get_repos_from_github()
    total_stars = 0
    total_forks = 0
    languages = {}
    topics = {}

    for repo in repos:
        info = get_repo_info(repo)
        if info:
            total_stars += info.get("stars", 0)
            total_forks += info.get("forks", 0)
            lang = info.get("language")
            if lang:
                languages[lang] = languages.get(lang, 0) + 1
            for topic in info.get("topics", []):
                topics[topic] = topics.get(topic, 0) + 1

    return {
        "total_repos": len(repos),
        "total_stars": total_stars,
        "total_forks": total_forks,
        "languages": languages,
        "top_topics": dict(sorted(topics.items(), key=lambda x: -x[1])[:20]),
    }
