"""
Commands: list, search, info, status
"""

from src.repos import REPOS, CATEGORIES, list_repos, search_repos, get_repo, GITHUB_USER
from utils.github import get_repos_from_github, get_repo_info, get_repo_stats
from utils.display import (
    C, print_header, print_subheader, print_success, print_error,
    print_warning, print_info, print_table, print_repo_card,
    print_category_card, print_progress,
)


def cmd_list(args):
    """List all repos, optionally filtered by category."""
    category = args.get("category")
    show_all = args.get("all", False)
    verbose = args.get("verbose", False)

    if category:
        cats = [category]
    else:
        cats = list(CATEGORIES.keys())

    total = 0
    for cat_key in cats:
        cat = CATEGORIES.get(cat_key)
        if not cat:
            print_error(f"Unknown category: {cat_key}")
            continue

        print_category_card(cat["name"], cat)

        repos_in_cat = [
            (name, REPOS[name]) for name in cat["repos"] if name in REPOS
        ]

        rows = []
        for name, data in repos_in_cat:
            total += 1
            url = f"https://github.com/{GITHUB_USER}/{name}"
            rows.append([
                f"{C.CYAN}{name}{C.RESET}",
                data["description"][:50],
                data["language"],
            ])

        if rows:
            print_table(
                ["Repo", "Description", "Lang"],
                rows,
                [22, 52, 12]
            )
        print()

    print(f"  {C.DIM}Total: {total} repos{C.RESET}")


def cmd_search(args):
    """Search repos by query."""
    query = args.get("query", "")
    if not query:
        print_error("Provide a search query: 0xv search <query>")
        return

    results = search_repos(query)
    if not results:
        print_warning(f"No repos found for '{query}'")
        return

    print_header(f"Search Results: '{query}'")
    for i, (name, data) in enumerate(results, 1):
        print_repo_card(name, data, index=i)

    print(f"  {C.DIM}Found {len(results)} repos{C.RESET}")


def cmd_info(args):
    """Show detailed info about a repo."""
    repo_name = args.get("repo", "")
    if not repo_name:
        print_error("Provide a repo name: 0xv info <repo>")
        return

    local_data = get_repo(repo_name)
    if not local_data:
        print_error(f"Unknown repo: {repo_name}")
        print_info(f"Available: {', '.join(sorted(REPOS.keys()))}")
        return

    print_header(f"📦 {local_data['name']}")
    print(f"  {C.DIM}Description:{C.RESET}  {local_data['description']}")
    print(f"  {C.DIM}Category:{C.RESET}    {local_data['category']}")
    print(f"  {C.DIM}Language:{C.RESET}    {local_data['language']}")
    print(f"  {C.DIM}Priority:{C.RESET}    {'🔴 High' if local_data['priority'] == 1 else '🟡 Medium'}")
    print(f"  {C.DIM}URL:{C.RESET}         https://github.com/{GITHUB_USER}/{repo_name}")

    tags = "  ".join([f"{C.CYAN}#{t}{C.RESET}" for t in local_data["tags"]])
    print(f"  {C.DIM}Tags:{C.RESET}       {tags}")

    # Try to get live stats from GitHub
    print_subheader("GitHub Stats")
    info = get_repo_info(repo_name)
    if info:
        print(f"  ⭐ Stars: {info.get('stars', 0)}")
        print(f"  🍴 Forks: {info.get('forks', 0)}")
        print(f"  📅 Created: {info.get('created', 'N/A')[:10]}")
        print(f"  🔄 Updated: {info.get('updated', 'N/A')[:10]}")
    else:
        print_warning("Could not fetch live GitHub stats")


def cmd_status(args):
    """Show overall status of all repos."""
    print_header("📊 Portfolio Status")

    # Local repos (from registry)
    local_count = len(REPOS)

    # GitHub repos
    print_subheader("GitHub Repositories")
    github_repos = get_repos_from_github()
    if github_repos:
        print_success(f"Found {len(github_repos)} repos on GitHub")
        for repo in sorted(github_repos):
            marker = "✓" if repo in REPOS else "?"
            print(f"    {C.DIM}{marker}{C.RESET} {repo}")
    else:
        print_warning("Could not fetch GitHub repos (check auth)")

    # Summary
    print_subheader("Summary by Category")
    for cat_key, cat_data in CATEGORIES.items():
        count = len([r for r in cat_data["repos"] if r in REPOS])
        print(f"  {cat_data['name']}: {count} repos")

    print(f"\n  {C.BOLD}Total in registry: {local_count}{C.RESET}")
    print(f"  {C.DIM}GitHub user: {GITHUB_USER}{C.RESET}")
