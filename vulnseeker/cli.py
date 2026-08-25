#!/usr/bin/env python3
"""
VulnSeeker CLI — Smart CVE Search from the command line.

Usage:
    python cli.py search "apache log4j"
    python cli.py get CVE-2021-44228
    python cli.py recent --days 7
    python cli.py analyze CVE-2021-44228
    python cli.py product nginx
    python cli.py critical
"""

import argparse
import json
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "src"))

from vulnseeker import VulnSeeker


def cmd_search(args):
    """Search CVEs by keyword."""
    vs = VulnSeeker()
    result = vs.search(
        query=args.query,
        max_results=args.limit,
        min_cvss=args.min_cvss,
        severity=args.severity,
        has_exploit=args.exploits,
    )

    print(f"\n🔍 Search: '{args.query}' ({result.total_results} total, {len(result.cves)} shown)")
    print(f"   Search time: {result.search_time:.2f}s\n")

    if not result.cves:
        print("   No results found.")
        return

    print(f"{'ID':<18} {'CVSS':<6} {'Severity':<10} {'Exploit':<8} {'Description'}")
    print("-" * 90)

    for cve in result.cves:
        exploit = "🔴" if cve.exploit_available else "🟢"
        desc = cve.description[:50] + "..." if len(cve.description) > 50 else cve.description
        print(f"{cve.id:<18} {cve.cvss_score:<6.1f} {cve.severity:<10} {exploit:<8} {desc}")

    if args.output:
        count = vs.export(result.cves, args.output, args.format)
        print(f"\n✅ Exported {count} CVEs to {args.output}")


def cmd_get(args):
    """Get details for a specific CVE."""
    vs = VulnSeeker()
    cve = vs.get_cve(args.cve_id.upper())

    if not cve:
        print(f"\n❌ CVE not found: {args.cve_id}")
        return

    print(f"\n🛡️  {cve.id}")
    print(f"{'='*60}")
    print(f"  CVSS Score:  {cve.cvss_score}/10 ({cve.severity})")
    print(f"  Published:  {cve.published[:10] if cve.published else 'N/A'}")
    print(f"  Modified:   {cve.modified[:10] if cve.modified else 'N/A'}")
    print(f"  Age:        {cve.age_days} days")
    print(f"  KEV:        {'🔴 YES' if cve.in_kev else '🟢 NO'}")
    print(f"  Exploit:    {'🔴 Available' if cve.exploit_available else '🟢 None known'}")
    print(f"\n  Description:")
    print(f"  {cve.description[:200]}...")

    if cve.cwe:
        print(f"\n  CWEs: {', '.join(cve.cwe)}")

    if cve.cvss_vector:
        print(f"  CVSS Vector: {cve.cvss_vector}")

    if cve.references:
        print(f"\n  References ({len(cve.references)}):")
        for ref in cve.references[:5]:
            print(f"    - {ref[:80]}")

    if args.output:
        vs.export([cve], args.output, args.format)
        print(f"\n✅ Exported to {args.output}")


def cmd_recent(args):
    """Search recent CVEs."""
    vs = VulnSeeker()
    cves = vs.search_recent(days=args.days, max_results=args.limit)

    print(f"\n📅 Recent CVEs (last {args.days} days) — {len(cves)} found\n")

    if not cves:
        print("   No recent CVEs found.")
        return

    print(f"{'ID':<18} {'CVSS':<6} {'Severity':<10} {'Published':<12} {'Description'}")
    print("-" * 90)

    for cve in cves:
        desc = cve.description[:45] + "..." if len(cve.description) > 45 else cve.description
        print(f"{cve.id:<18} {cve.cvss_score:<6.1f} {cve.severity:<10} {cve.published[:10]:<12} {desc}")

    if args.output:
        count = vs.export(cves, args.output, args.format)
        print(f"\n✅ Exported {count} CVEs to {args.output}")


def cmd_analyze(args):
    """Analyze risk for a CVE."""
    vs = VulnSeeker()
    analysis = vs.analyze_risk(args.cve_id.upper())

    if not analysis:
        print(f"\n❌ Could not analyze: {args.cve_id}")
        return

    print(f"\n📊 Risk Analysis: {analysis.cve_id}")
    print(f"{'='*60}")
    print(f"  CVSS Score:     {analysis.cvss_score}/10")
    print(f"  Risk Level:     {analysis.risk_level}")
    print(f"\n  Exploitability:")
    print(f"    {analysis.exploitability}")
    print(f"\n  Impact:")
    print(f"    {analysis.impact}")
    print(f"\n  EPSS Risk:")
    print(f"    {analysis.epss_risk}")

    if analysis.recommendations:
        print(f"\n  Recommendations:")
        for i, rec in enumerate(analysis.recommendations, 1):
            print(f"    {i}. {rec}")

    if analysis.mitigation_steps:
        print(f"\n  Mitigation Steps:")
        for i, step in enumerate(analysis.mitigation_steps, 1):
            print(f"    {i}. {step}")

    if analysis.similar_cves:
        print(f"\n  Similar CVEs:")
        for sim in analysis.similar_cves:
            print(f"    - {sim}")


def cmd_product(args):
    """Search CVEs by product."""
    vs = VulnSeeker()
    cves = vs.search_by_product(args.product, args.version, max_results=args.limit)

    print(f"\n🔍 Product: {args.product} {args.version or ''} — {len(cves)} CVEs found\n")

    if not cves:
        print("   No CVEs found for this product.")
        return

    stats = vs.stats(cves)
    print(f"  Avg CVSS: {stats['avg_cvss']:.1f} | Max: {stats['max_cvss']:.1f}")
    print(f"  With Exploits: {stats['with_exploits']} | In KEV: {stats['in_kev']}\n")

    print(f"{'ID':<18} {'CVSS':<6} {'Severity':<10} {'Description'}")
    print("-" * 80)

    for cve in cves[:args.limit]:
        desc = cve.description[:45] + "..." if len(cve.description) > 45 else cve.description
        print(f"{cve.id:<18} {cve.cvss_score:<6.1f} {cve.severity:<10} {desc}")


def cmd_critical(args):
    """Search critical CVEs."""
    vs = VulnSeeker()
    cves = vs.search_critical(max_results=args.limit)

    print(f"\n🚨 Critical CVEs (CVSS >= 9.0) — {len(cves)} found\n")

    if not cves:
        print("   No critical CVEs found.")
        return

    print(f"{'ID':<18} {'CVSS':<6} {'KEV':<5} {'Exploit':<8} {'Description'}")
    print("-" * 85)

    for cve in cves:
        kev = "🔴" if cve.in_kev else "  "
        exploit = "🔴" if cve.exploit_available else "🟢"
        desc = cve.description[:45] + "..." if len(cve.description) > 45 else cve.description
        print(f"{cve.id:<18} {cve.cvss_score:<6.1f} {kev:<5} {exploit:<8} {desc}")


def main():
    parser = argparse.ArgumentParser(
        description="🔍 VulnSeeker — Smart CVE Search Engine",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    sub = parser.add_subparsers(dest="command", help="Command")

    # search
    search_p = sub.add_parser("search", help="Search CVEs by keyword")
    search_p.add_argument("query", help="Search query")
    search_p.add_argument("-n", "--limit", type=int, default=20)
    search_p.add_argument("--min-cvss", type=float, default=0)
    search_p.add_argument("--severity", choices=["CRITICAL", "HIGH", "MEDIUM", "LOW"])
    search_p.add_argument("--exploits", action="store_true", help="Only CVEs with exploits")
    search_p.add_argument("-o", "--output", help="Export to file")
    search_p.add_argument("-f", "--format", default="json", choices=["json", "csv", "markdown"])

    # get
    get_p = sub.add_parser("get", help="Get CVE details")
    get_p.add_argument("cve_id", help="CVE ID (e.g., CVE-2021-44228)")
    get_p.add_argument("-o", "--output", help="Export to file")
    get_p.add_argument("-f", "--format", default="json")

    # recent
    recent_p = sub.add_parser("recent", help="Search recent CVEs")
    recent_p.add_argument("-d", "--days", type=int, default=30)
    recent_p.add_argument("-n", "--limit", type=int, default=50)
    recent_p.add_argument("-o", "--output", help="Export to file")
    recent_p.add_argument("-f", "--format", default="json")

    # analyze
    analyze_p = sub.add_parser("analyze", help="Analyze CVE risk")
    analyze_p.add_argument("cve_id", help="CVE ID")

    # product
    product_p = sub.add_parser("product", help="Search by product")
    product_p.add_argument("product", help="Product name")
    product_p.add_argument("-v", "--version", help="Version")
    product_p.add_argument("-n", "--limit", type=int, default=20)

    # critical
    critical_p = sub.add_parser("critical", help="Search critical CVEs")
    critical_p.add_argument("-n", "--limit", type=int, default=20)

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        return

    commands = {
        "search": cmd_search,
        "get": cmd_get,
        "recent": cmd_recent,
        "analyze": cmd_analyze,
        "product": cmd_product,
        "critical": cmd_critical,
    }

    commands[args.command](args)


if __name__ == "__main__":
    main()
