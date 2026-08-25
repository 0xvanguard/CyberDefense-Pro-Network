"""
Commands: sync — push, create repos, manage GitHub
"""

import os
import subprocess
from pathlib import Path

from src.repos import REPOS, CATEGORIES, GITHUB_USER
from utils.github import create_repo, get_repos_from_github
from utils.display import (
    C, print_header, print_subheader, print_success, print_error,
    print_warning, print_info, print_progress,
)


def cmd_sync(args):
    """Sync all local repos to GitHub (create missing + push updates)."""
    action = args.get("action", "status")
    dry_run = args.get("dry_run", False)

    print_header("🔄 Sync with GitHub")

    if action == "status":
        _sync_status()
    elif action == "create-missing":
        _sync_create_missing(dry_run)
    elif action == "push-all":
        _sync_push_all(dry_run)
    elif action == "full":
        _sync_full(dry_run)
    else:
        print_error(f"Unknown sync action: {action}")
        print_info("Available: status, create-missing, push-all, full")


def _sync_status():
    """Show sync status between local and GitHub."""
    print_subheader("Local Registry")
    local_repos = set(REPOS.keys())
    print_info(f"{len(local_repos)} repos in local registry")

    print_subheader("GitHub Repos")
    github_repos = set(get_repos_from_github())
    if github_repos:
        print_info(f"{len(github_repos)} repos on GitHub")
    else:
        print_warning("Could not fetch GitHub repos")
        return

    # Compare
    missing_on_gh = local_repos - github_repos
    missing_local = github_repos - local_repos
    in_sync = local_repos & github_repos

    if in_sync:
        print_success(f"{len(in_sync)} repos in sync")
        for name in sorted(in_sync):
            print(f"    ✓ {name}")

    if missing_on_gh:
        print_warning(f"{len(missing_on_gh)} repos NOT on GitHub:")
        for name in sorted(missing_on_gh):
            print(f"    ✗ {name}")

    if missing_local:
        print_info(f"{len(missing_local)} repos on GitHub but not in registry:")
        for name in sorted(missing_local):
            print(f"    ? {name}")


def _sync_create_missing(dry_run=False):
    """Create repos on GitHub that are missing."""
    local_repos = set(REPOS.keys())
    github_repos = set(get_repos_from_github())
    missing = local_repos - github_repos

    if not missing:
        print_success("All repos exist on GitHub!")
        return

    print_subheader(f"Creating {len(missing)} repos")

    for i, name in enumerate(sorted(missing)):
        data = REPOS[name]
        print_progress(i + 1, len(missing), f"Creating {name}...")

        if dry_run:
            print_info(f"Would create: {name}")
            continue

        result = create_repo(name, data["description"])
        if result["success"]:
            print_success(f"Created {name}")
        else:
            print_error(f"Failed {name}: {result['output']}")


def _sync_push_all(dry_run=False):
    """Push updates for all local repos."""
    base = os.getcwd()
    repos_to_push = []

    for name in REPOS:
        repo_dir = os.path.join(base, name)
        if os.path.isdir(os.path.join(repo_dir, ".git")):
            repos_to_push.append((name, repo_dir))

    if not repos_to_push:
        print_warning("No git repos found locally")
        return

    print_subheader(f"Pushing {len(repos_to_push)} repos")

    for i, (name, repo_dir) in enumerate(repos_to_push):
        print_progress(i + 1, len(repos_to_push), f"Pushing {name}...")

        if dry_run:
            print_info(f"Would push: {name}")
            continue

        try:
            # Check if there are changes
            result = subprocess.run(
                ["git", "-C", repo_dir, "status", "--porcelain"],
                capture_output=True, text=True
            )
            if result.stdout.strip():
                subprocess.run(["git", "-C", repo_dir, "add", "-A"], capture_output=True)
                subprocess.run(
                    ["git", "-C", repo_dir, "commit", "-m", "chore: sync updates"],
                    capture_output=True
                )
                subprocess.run(["git", "-C", repo_dir, "push"], capture_output=True)
                print_success(f"Pushed {name}")
            else:
                print_info(f"{name} — up to date")
        except Exception as e:
            print_error(f"Failed {name}: {e}")


def _sync_full(dry_run=False):
    """Full sync: create missing + push all."""
    _sync_create_missing(dry_run)
    _sync_push_all(dry_run)
