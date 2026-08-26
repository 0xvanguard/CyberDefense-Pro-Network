#!/usr/bin/env python3
"""
ThreatHunt CLI — Threat hunting from the command line.

Usage:
    python cli.py hunt --timeframe 24h
    python cli.py hunt --timeframe 7d --format stix
    python cli.py queries
    python cli.py tactics
    python cli.py techniques
    python cli.py iocs --file iocs.json
    python cli.py export --format markdown --output report.md
    python cli.py summary
"""

import argparse
import json
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "src"))

from hunter import ThreatHunter, ThreatLevel, MITRE_TACTICS, MITRE_TECHNIQUES


def cmd_hunt(args):
    """Run threat hunt."""
    hunter = ThreatHunter()

    if args.iocs:
        hunter.load_iocs(args.iocs)

    result = hunter.hunt(timeframe=args.timeframe)

    severity_icons = {
        "critical": "🔴", "high": "🟠", "medium": "🟡", "low": "🟢", "info": "⚪",
    }

    print(f"\n🔍 Threat Hunt Results\n{'='*60}")
    print(f"  Timeframe:   {result.timeframe}")
    print(f"  Queries Run: {result.total_queries}")
    print(f"  Findings:    {len(result.findings)}")
    print(f"  IoCs Found:  {result.iocs_found}")

    if result.findings:
        print(f"\n  ⚠️  Findings\n  {'-'*50}")
        for f in sorted(result.findings, key=lambda x: x.confidence, reverse=True):
            icon = severity_icons.get(f.severity.value, "⚪")
            print(f"\n  {icon} {f.hunt_name} — {f.technique}")
            print(f"     Confidence: {f.confidence:.0%}")
            print(f"     Description: {f.description}")
            if f.evidence:
                print(f"     Evidence:")
                for e in f.evidence[:3]:
                    print(f"       • {e}")
            if f.recommended_action:
                print(f"     Action: {f.recommended_action}")

    # Export if requested
    if args.format != "text":
        output = hunter.export(result.findings, format=args.format)
        if args.output:
            with open(args.output, "w") as f:
                f.write(output)
            print(f"\n💾 Exported to {args.output} ({args.format})")
        else:
            print(f"\n{output}")


def cmd_queries(args):
    """List hunt queries."""
    hunter = ThreatHunter()

    print(f"\n📋 Hunt Queries ({len(hunter.hunt_queries)})\n{'='*60}")
    print(f"{'Name':<25} {'Technique':<12} {'Severity':<10} {'Data Sources'}")
    print("-" * 70)

    severity_icons = {
        "critical": "🔴", "high": "🟠", "medium": "🟡", "low": "🟢", "info": "⚪",
    }

    for name, q in sorted(hunter.hunt_queries.items()):
        icon = severity_icons.get(q.severity.value, "⚪")
        sources = ", ".join(q.data_sources)
        print(f"{q.name:<25} {q.mitre_technique:<12} {icon} {q.severity.value:<8} {sources}")


def cmd_tactics(args):
    """List MITRE ATT&CK tactics."""
    print(f"\n🎯 MITRE ATT&CK Tactics\n{'='*60}")
    for tid, tactic in sorted(MITRE_TACTICS.items()):
        print(f"  {tid} — {tactic.name}")
        print(f"    {tactic.description}")


def cmd_techniques(args):
    """List MITRE ATT&CK techniques."""
    print(f"\n🔧 MITRE ATT&CK Techniques\n{'='*60}")
    for tid, tech in sorted(MITRE_TECHNIQUES.items()):
        print(f"  {tid} — {tech.name}")
        print(f"    Tactic: {tech.tactic.name}")
        print(f"    Detection: {tech.detection[:80]}")
        print(f"    Mitigation: {tech.mitigation[:80]}")
        print()


def cmd_iocs(args):
    """Load and display IoCs."""
    hunter = ThreatHunter()

    if args.file:
        count = hunter.load_iocs(args.file)
        print(f"\n📥 Loaded {count} IoCs from {args.file}")

    if args.add_type and args.add_value:
        from hunter import IoC
        ioc = IoC(
            type=args.add_type, value=args.add_value,
            confidence=args.confidence, source="manual",
        )
        hunter.add_ioc(ioc)
        print(f"  Added IoC: {args.add_type} = {args.add_value}")

    print(f"\n📡 IoC Feed ({len(hunter.ioc_feeds)} entries)\n{'='*60}")
    for ioc in hunter.ioc_feeds[:20]:
        print(f"  [{ioc.type}] {ioc.value} (confidence: {ioc.confidence:.0%})")


def cmd_export(args):
    """Export findings."""
    hunter = ThreatHunter()
    hunter.hunt()

    output = hunter.export(format=args.format)

    if args.output:
        with open(args.output, "w") as f:
            f.write(output)
        print(f"✅ Exported {len(hunter.findings)} findings to {args.output}")
    else:
        print(output)


def cmd_summary(args):
    """Show hunt summary."""
    hunter = ThreatHunter()
    hunter.hunt()
    summary = hunter.summary()

    severity_icons = {
        "critical": "🔴", "high": "🟠", "medium": "🟡", "low": "🟢", "info": "⚪",
    }

    print(f"\n📊 Hunt Summary\n{'='*40}")
    print(f"  Timeframe:    {summary['timeframe']}")
    print(f"  Findings:     {summary['total_findings']}")
    print(f"  Queries Run:  {summary['queries_run']}")
    print(f"  IoCs Found:   {summary['iocs_found']}")

    if summary["by_severity"]:
        print(f"\n  By Severity:")
        for sev, count in summary["by_severity"].items():
            icon = severity_icons.get(sev, "⚪")
            print(f"    {icon} {sev:<10} {count}")

    if summary["by_tactic"]:
        print(f"\n  By Tactic:")
        for tactic, count in summary["by_tactic"].items():
            print(f"    {tactic:<30} {count}")


def main():
    parser = argparse.ArgumentParser(
        description="🔍 ThreatHunt — Automated Threat Hunting"
    )
    sub = parser.add_subparsers(dest="command")

    # hunt
    hunt_p = sub.add_parser("hunt", help="Run threat hunt")
    hunt_p.add_argument("--timeframe", "-t", default="24h")
    hunt_p.add_argument("--iocs", default="", help="IoC feed JSON file")
    hunt_p.add_argument("--format", "-f", default="text",
                       choices=["text", "json", "stix", "csv", "markdown"])
    hunt_p.add_argument("--output", "-o", default="")

    # queries
    sub.add_parser("queries", help="List hunt queries")

    # tactics
    sub.add_parser("tactics", help="List MITRE tactics")

    # techniques
    sub.add_parser("techniques", help="List MITRE techniques")

    # iocs
    ioc_p = sub.add_parser("iocs", help="Manage IoCs")
    ioc_p.add_argument("--file", default="")
    ioc_p.add_argument("--add-type", default="")
    ioc_p.add_argument("--add-value", default="")
    ioc_p.add_argument("--confidence", type=float, default=0.7)

    # export
    export_p = sub.add_parser("export", help="Export findings")
    export_p.add_argument("--format", "-f", default="json",
                         choices=["json", "stix", "csv", "markdown"])
    export_p.add_argument("--output", "-o", default="")

    # summary
    sub.add_parser("summary", help="Hunt summary")

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        return

    commands = {
        "hunt": cmd_hunt, "queries": cmd_queries, "tactics": cmd_tactics,
        "techniques": cmd_techniques, "iocs": cmd_iocs, "export": cmd_export,
        "summary": cmd_summary,
    }
    commands[args.command](args)


if __name__ == "__main__":
    main()
