#!/usr/bin/env python3
"""
ThreatMap CLI — Threat Intelligence from the command line.

Usage:
    python cli.py threats --hours 24
    python cli.py stats --hours 24
    python cli.py countries --top 10
    python cli.py export --format json
    python cli.py geojson
    python cli.py feeds
"""

import argparse
import json
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "src"))

from map import ThreatMap


def cmd_threats(args):
    """List recent threats."""
    tmap = ThreatMap()
    threats = tmap.get_threats(
        region=args.region,
        country=args.country,
        threat_type=args.type,
        severity=args.severity,
        hours=args.hours,
        limit=args.limit,
    )

    print(f"\n🚨 Threats ({len(threats)} found, last {args.hours}h)\n")

    if not threats:
        print("  No threats found.")
        return

    print(f"{'ID':<12} {'Type':<15} {'Severity':<10} {'Country':<8} {'Title'}")
    print("-" * 80)

    for t in threats:
        country = t.geo.country_code if t.geo else "N/A"
        sev_icon = {"critical": "🔴", "high": "🟠", "medium": "🟡", "low": "🟢", "info": "⚪"}.get(t.severity, "⚪")
        print(f"{t.id:<12} {t.threat_type:<15} {sev_icon} {t.severity:<8} {country:<8} {t.title[:40]}")


def cmd_stats(args):
    """Show threat statistics."""
    tmap = ThreatMap()
    stats = tmap.get_stats(hours=args.hours)

    print(f"\n📊 Threat Statistics (last {args.hours}h)\n{'='*50}")
    print(f"  Total Threats:    {stats.total_threats}")
    print(f"  Active:           {stats.active_threats}")
    print(f"  Critical:         {stats.critical_threats}")
    print(f"  Avg Confidence:   {stats.avg_confidence:.0%}")

    print(f"\n  By Type:")
    for t, count in sorted(stats.by_type.items(), key=lambda x: x[1], reverse=True):
        print(f"    {t:<20} {count}")

    print(f"\n  By Severity:")
    for s, count in sorted(stats.by_severity.items(), key=lambda x: x[1], reverse=True):
        icon = {"critical": "🔴", "high": "🟠", "medium": "🟡", "low": "🟢"}.get(s, "⚪")
        print(f"    {icon} {s:<18} {count}")

    print(f"\n  By Region:")
    for r, count in sorted(stats.by_region.items(), key=lambda x: x[1], reverse=True):
        print(f"    {r:<20} {count}")


def cmd_countries(args):
    """Show top countries by threat count."""
    tmap = ThreatMap()
    countries = tmap.get_top_countries(top=args.top, hours=args.hours)

    print(f"\n🌍 Top Countries (last {args.hours}h)\n")

    print(f"{'Rank':<6} {'Country':<8} {'Threats'}")
    print("-" * 30)

    for i, entry in enumerate(countries, 1):
        medal = {1: "🥇", 2: "🥈", 3: "🥉"}.get(i, f"#{i}")
        print(f"{medal:<6} {entry['country']:<8} {entry['count']}")


def cmd_export(args):
    """Export threats."""
    tmap = ThreatMap()
    count = tmap.export(output_file=args.output, format=args.format)
    print(f"\n✅ Exported {count} threats to {args.output} ({args.format} format)")


def cmd_geojson(args):
    """Export as GeoJSON."""
    tmap = ThreatMap()
    count = tmap.export_geojson(output_file=args.output)
    print(f"\n✅ Exported {count} threats to {args.output} (GeoJSON)")


def cmd_feeds(args):
    """List threat feeds."""
    tmap = ThreatMap()
    feeds = tmap.get_feeds()

    print(f"\n📡 Threat Feeds ({len(feeds)} configured)\n")

    print(f"{'Name':<25} {'Type':<15} {'Frequency':<15} {'Reliability'}")
    print("-" * 70)

    for feed in feeds:
        stars = "⭐" * feed.reliability
        print(f"{feed.name:<25} {feed.feed_type:<15} {feed.update_frequency:<15} {stars}")


def cmd_mitre(args):
    """Show MITRE ATT&CK coverage."""
    tmap = ThreatMap()
    coverage = tmap.get_mitre_coverage(hours=args.hours)

    print(f"\n🎯 MITRE ATT&CK Coverage (last {args.hours}h)\n")

    if not coverage:
        print("  No techniques found.")
        return

    print(f"{'Technique':<15} {'Count':<10} {'Bar'}")
    print("-" * 50)

    max_count = max(coverage.values()) if coverage else 1
    for tech, count in sorted(coverage.items(), key=lambda x: x[1], reverse=True)[:20]:
        bar = "█" * int(count / max_count * 20) if max_count > 0 else ""
        print(f"{tech:<15} {count:<10} {bar}")


def cmd_trends(args):
    """Show threat trends."""
    tmap = ThreatMap()
    trends = tmap.analyze_trends(days=args.days)

    print(f"\n📈 Threat Trends (last {args.days} days)\n")
    print(f"  Trend: {trends['trend'].upper()}")
    print(f"  Average: {trends['avg_daily']:.1f} threats/day")
    print(f"  Max: {trends['max_daily']}")
    print(f"  Min: {trends['min_daily']}")

    print(f"\n  Daily:")
    for date, count in sorted(trends['daily_counts'].items()):
        bar = "█" * count
        print(f"    {date}: {bar} ({count})")


def main():
    parser = argparse.ArgumentParser(description="🌍 ThreatMap — Threat Intelligence")
    sub = parser.add_subparsers(dest="command")

    # threats
    threats_p = sub.add_parser("threats", help="List threats")
    threats_p.add_argument("-r", "--region", help="Filter by region")
    threats_p.add_argument("-c", "--country", help="Filter by country code")
    threats_p.add_argument("-t", "--type", help="Filter by type")
    threats_p.add_argument("-s", "--severity", help="Filter by severity")
    threats_p.add_argument("--hours", type=int, default=24)
    threats_p.add_argument("-n", "--limit", type=int, default=50)

    # stats
    stats_p = sub.add_parser("stats", help="Show statistics")
    stats_p.add_argument("--hours", type=int, default=24)

    # countries
    countries_p = sub.add_parser("countries", help="Top countries")
    countries_p.add_argument("--hours", type=int, default=24)
    countries_p.add_argument("-n", "--top", type=int, default=10)

    # export
    export_p = sub.add_parser("export", help="Export threats")
    export_p.add_argument("-o", "--output", default="threats.json")
    export_p.add_argument("-f", "--format", default="json", choices=["json", "csv", "markdown", "stix"])

    # geojson
    geojson_p = sub.add_parser("geojson", help="Export as GeoJSON")
    geojson_p.add_argument("-o", "--output", default="threats.geojson")

    # feeds
    sub.add_parser("feeds", help="List feeds")

    # mitre
    mitre_p = sub.add_parser("mitre", help="MITRE ATT&CK coverage")
    mitre_p.add_argument("--hours", type=int, default=24)

    # trends
    trends_p = sub.add_parser("trends", help="Threat trends")
    trends_p.add_argument("-d", "--days", type=int, default=7)

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        return

    commands = {
        "threats": cmd_threats,
        "stats": cmd_stats,
        "countries": cmd_countries,
        "export": cmd_export,
        "geojson": cmd_geojson,
        "feeds": cmd_feeds,
        "mitre": cmd_mitre,
        "trends": cmd_trends,
    }

    commands[args.command](args)


if __name__ == "__main__":
    main()
