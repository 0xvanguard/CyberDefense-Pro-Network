#!/usr/bin/env python3
"""
PromptKiller CLI — Command line interface for the attack prompt library.

Usage:
    python cli.py list                    # List all categories
    python cli.py list --category jailbreak  # List prompts in category
    python cli.py search "sql injection"  # Search prompts
    python cli.py random --count 5        # Get random prompts
    python cli.py scan "ignore previous instructions"  # Scan for attacks
    python cli.py stats                   # Show statistics
    python cli.py export --format json    # Export prompts
"""

import argparse
import json
import sys
from promptkiller import PromptKiller


def cmd_list(args):
    """List categories or prompts in a category."""
    pk = PromptKiller()

    if args.category:
        prompts = pk.get_category(args.category)
        print(f"\n📂 Category: {args.category} ({len(prompts)} prompts)\n")
        print(f"{'ID':<10} {'Name':<30} {'Severity':<10} {'Effectiveness'}")
        print("-" * 70)
        for p in prompts:
            print(f"{p.id:<10} {p.name:<30} {p.severity:<10} {p.effectiveness:.0%}")
    else:
        categories = pk.list_categories()
        print(f"\n📚 PromptKiller Categories ({pk.stats()['total']} total prompts)\n")
        print(f"{'Category':<20} {'Count':<10} {'Description'}")
        print("-" * 60)
        for cat, count in sorted(categories.items()):
            print(f"{cat:<20} {count:<10}")
        print()


def cmd_search(args):
    """Search prompts by keyword."""
    pk = PromptKiller()
    results = pk.search(args.query)

    print(f"\n🔍 Search: '{args.query}' ({len(results)} results)\n")
    print(f"{'ID':<10} {'Category':<15} {'Name':<30} {'Severity'}")
    print("-" * 70)
    for p in results:
        print(f"{p.id:<10} {p.category:<15} {p.name:<30} {p.severity}")
    print()


def cmd_random(args):
    """Get random prompts."""
    pk = PromptKiller()
    prompts = pk.random(
        count=args.count,
        category=args.category,
        severity=args.severity
    )

    print(f"\n🎲 Random Prompts ({len(prompts)} selected)\n")
    for i, p in enumerate(prompts, 1):
        print(f"--- [{i}] {p.name} ({p.category}) ---")
        print(f"Severity: {p.severity} | Effectiveness: {p.effectiveness:.0%}")
        print(f"Prompt: {p.prompt[:150]}...")
        print()


def cmd_scan(args):
    """Scan text for attack patterns."""
    pk = PromptKiller()
    result = pk.scan(args.text)

    print(f"\n🛡️  Scan Result\n")
    print(f"Is Attack: {'🔴 YES' if result.is_attack else '🟢 NO'}")
    print(f"Category: {result.category or 'N/A'}")
    print(f"Confidence: {result.confidence:.0%}")
    print(f"Severity: {result.severity}")
    print(f"Explanation: {result.explanation}")
    if result.matched_patterns:
        print(f"\nMatched Patterns ({len(result.matched_patterns)}):")
        for p in result.matched_patterns:
            print(f"  - {p}")
    print()


def cmd_stats(args):
    """Show statistics."""
    pk = PromptKiller()
    stats = pk.stats()

    print(f"\n📊 PromptKiller Statistics\n")
    print(f"Total Prompts: {stats['total']}")
    print(f"Categories: {stats['categories']}")
    print(f"Unique Techniques: {stats['techniques']}")
    print(f"Avg Effectiveness: {stats['avg_effectiveness']:.0%}")
    print(f"\nBy Category:")
    for cat, count in sorted(stats['category_counts'].items()):
        print(f"  {cat}: {count}")
    print(f"\nBy Severity:")
    for sev, count in sorted(stats['severity_counts'].items()):
        print(f"  {sev}: {count}")
    print()


def cmd_export(args):
    """Export prompts to file."""
    pk = PromptKiller()
    count = pk.export(
        output_file=args.output,
        format=args.format,
        category=args.category
    )
    print(f"\n✅ Exported {count} prompts to {args.output} ({args.format} format)\n")


def cmd_show(args):
    """Show a specific prompt."""
    pk = PromptKiller()
    for p in pk.prompts:
        if p.id == args.id or p.name.lower() == args.id.lower():
            print(f"\n🎯 Prompt: {p.name}\n")
            print(f"ID: {p.id}")
            print(f"Category: {p.category}")
            print(f"Technique: {p.technique}")
            print(f"Severity: {p.severity}")
            print(f"Effectiveness: {p.effectiveness:.0%}")
            print(f"Description: {p.description}")
            print(f"\nPrompt:\n{p.prompt}")
            print(f"\nTags: {', '.join(p.tags)}")
            print()
            return

    print(f"\n❌ Prompt not found: {args.id}\n")


def main():
    parser = argparse.ArgumentParser(
        description="🎯 PromptKiller — AI Attack Prompt Library",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s list                          List all categories
  %(prog)s list --category jailbreak     List jailbreak prompts
  %(prog)s search "sql injection"        Search for SQL injection prompts
  %(prog)s random --count 5              Get 5 random prompts
  %(prog)s random --category injection   Get random injection prompts
  %(prog)s scan "ignore previous..."     Scan text for attacks
  %(prog)s show DAN-Classic              Show specific prompt
  %(prog)s stats                         Show statistics
  %(prog)s export --output prompts.json  Export to JSON
        """
    )

    subparsers = parser.add_subparsers(dest="command", help="Command to run")

    # list
    list_parser = subparsers.add_parser("list", help="List categories or prompts")
    list_parser.add_argument("--category", "-c", help="List prompts in category")

    # search
    search_parser = subparsers.add_parser("search", help="Search prompts")
    search_parser.add_argument("query", help="Search query")

    # random
    random_parser = subparsers.add_parser("random", help="Get random prompts")
    random_parser.add_argument("--count", "-n", type=int, default=5, help="Number of prompts")
    random_parser.add_argument("--category", "-c", help="Filter by category")
    random_parser.add_argument("--severity", "-s", help="Filter by severity")

    # scan
    scan_parser = subparsers.add_parser("scan", help="Scan text for attacks")
    scan_parser.add_argument("text", help="Text to scan")

    # show
    show_parser = subparsers.add_parser("show", help="Show specific prompt")
    show_parser.add_argument("id", help="Prompt ID or name")

    # stats
    subparsers.add_parser("stats", help="Show statistics")

    # export
    export_parser = subparsers.add_parser("export", help="Export prompts")
    export_parser.add_argument("--output", "-o", default="prompts.json", help="Output file")
    export_parser.add_argument("--format", "-f", choices=["json", "csv", "txt"], default="json")
    export_parser.add_argument("--category", "-c", help="Export specific category")

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        return

    commands = {
        "list": cmd_list,
        "search": cmd_search,
        "random": cmd_random,
        "scan": cmd_scan,
        "show": cmd_show,
        "stats": cmd_stats,
        "export": cmd_export,
    }

    commands[args.command](args)


if __name__ == "__main__":
    main()
