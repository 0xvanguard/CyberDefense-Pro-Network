#!/usr/bin/env python3
"""
GuardDog CLI — Prompt Injection Scanner from the command line.

Usage:
    python cli.py scan "ignore all previous instructions"
    python cli.py scan-file input.txt
    python cli.py rules --category injection
    python cli.py stats
"""

import argparse
import json
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "src"))

from scanner import GuardDog


def cmd_scan(args):
    """Scan text for attacks."""
    scanner = GuardDog()
    result = scanner.scan(args.text)

    color = {
        "critical": "\033[91m", "high": "\033[93m", "medium": "\033[93m",
        "low": "\033[92m", "info": "\033[94m", "safe": "\033[92m"
    }
    reset = "\033[0m"

    threat_color = color.get(result.threat_level, "")

    print(f"\n🛡️  GuardDog Scan Result\n{'='*50}")
    print(f"  Threat Level: {threat_color}{result.threat_level.upper()}{reset}")
    print(f"  Confidence:   {result.confidence:.0%}")
    print(f"  Is Attack:    {'🔴 YES' if result.is_attack else '🟢 NO'}")
    print(f"  Scan Time:    {result.scan_time*1000:.1f}ms")
    print(f"  Categories:   {', '.join(result.categories_found) if result.categories_found else 'None'}")

    if result.detections:
        print(f"\n  Detections ({len(result.detections)}):")
        for d in result.detections:
            sev_color = color.get(d.severity, "")
            print(f"    [{sev_color}{d.severity.upper():8}{reset}] {d.rule_name}")
            print(f"             Matched: \"{d.matched_text[:60]}...\"")

    print(f"\n  📋 {result.recommendation}")

    if args.output:
        with open(args.output, "w") as f:
            json.dump(result.to_dict(), f, indent=2)
        print(f"\n  ✅ Exported to {args.output}")


def cmd_scan_file(args):
    """Scan a file for attacks."""
    with open(args.file) as f:
        text = f.read()

    scanner = GuardDog()
    result = scanner.scan(text)

    print(f"\n🛡️  GuardDog File Scan: {args.file}")
    print(f"  Threat: {result.threat_level.upper()} | Confidence: {result.confidence:.0%}")
    print(f"  Detections: {len(result.detections)}")
    print(f"  {result.recommendation}")


def cmd_rules(args):
    """List detection rules."""
    scanner = GuardDog()
    rules = scanner.get_rules(category=args.category, severity=args.severity)

    print(f"\n📋 GuardDog Rules ({len(rules)} rules)\n")

    if not args.category:
        categories = scanner.list_categories()
        print("Categories:")
        for cat, count in sorted(categories.items()):
            print(f"  {cat:<20} {count} rules")
        print()

    print(f"{'ID':<10} {'Name':<30} {'Severity':<10} {'Confidence'}")
    print("-" * 65)

    for rule in rules:
        print(f"{rule.id:<10} {rule.name:<30} {rule.severity:<10} {rule.confidence:.0%}")


def cmd_stats(args):
    """Show scanner statistics."""
    scanner = GuardDog()
    stats = scanner.stats()

    print(f"\n📊 GuardDog Statistics\n{'='*40}")
    print(f"  Total Rules:    {stats['total_rules']}")
    print(f"  Categories:     {stats['categories']}")
    print(f"  Total Scans:    {stats['total_scans']}")
    print(f"  Threats Found:  {stats['threats_detected']}")

    print(f"\n  By Category:")
    for cat, count in sorted(stats['category_counts'].items()):
        print(f"    {cat:<20} {count}")

    print(f"\n  By Severity:")
    for sev, count in sorted(stats['severity_counts'].items()):
        print(f"    {sev:<20} {count}")


def main():
    parser = argparse.ArgumentParser(description="🛡️ GuardDog — Prompt Injection Scanner")
    sub = parser.add_subparsers(dest="command")

    # scan
    scan_p = sub.add_parser("scan", help="Scan text")
    scan_p.add_argument("text", help="Text to scan")
    scan_p.add_argument("-o", "--output", help="Export result")

    # scan-file
    file_p = sub.add_parser("scan-file", help="Scan file")
    file_p.add_argument("file", help="File to scan")

    # rules
    rules_p = sub.add_parser("rules", help="List rules")
    rules_p.add_argument("-c", "--category", help="Filter by category")
    rules_p.add_argument("-s", "--severity", help="Filter by severity")

    # stats
    sub.add_parser("stats", help="Show statistics")

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        return

    commands = {
        "scan": cmd_scan,
        "scan-file": cmd_scan_file,
        "rules": cmd_rules,
        "stats": cmd_stats,
    }

    commands[args.command](args)


if __name__ == "__main__":
    main()
