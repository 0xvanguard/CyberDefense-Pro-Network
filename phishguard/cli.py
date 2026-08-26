#!/usr/bin/env python3
"""
PhishGuard CLI — Phishing detection from the command line.

Usage:
    python cli.py url "https://suspicious-site.xyz"
    python cli.py email --from "bad@phish.com" --body "Verify your password"
    python cli.py text "You have won a prize!"
    python cli.py batch --file urls.txt
    python cli.py stats
"""

import argparse
import json
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "src"))

from detector import PhishDetector, Verdict


detector = PhishDetector()


def cmd_url(args):
    """Analyze a URL."""
    result = detector.analyze_url(args.url)

    verdict_icons = {
        "legitimate": "🟢", "suspicious": "🟡",
        "phishing": "🔴", "unknown": "⚪",
    }
    icon = verdict_icons.get(result.verdict.value, "⚪")

    print(f"\n🔗 URL Analysis\n{'='*60}")
    print(f"  URL:       {result.target}")
    print(f"  Verdict:   {icon} {result.verdict.value.upper()}")
    print(f"  Confidence:{result.confidence:.0%}")
    print(f"  Risk:      {'█' * int(result.risk_score * 10)}{'░' * (10 - int(result.risk_score * 10))} {result.risk_score:.2f}")

    if result.signals:
        print(f"\n  📡 Signals ({len(result.signals)}):")
        for s in result.signals:
            print(f"    ⚠️  {s.name}: {s.description}")
            if s.evidence:
                print(f"       Evidence: {s.evidence}")

    print(f"\n  📌 Recommendations:")
    for rec in result.recommendations:
        print(f"    {rec}")

    print(f"\n  ⏱️  Analysis time: {result.analysis_time_ms:.1f}ms")


def cmd_email(args):
    """Analyze an email."""
    headers = {
        "from": args.from_addr,
        "reply-to": args.reply_to or "",
        "authentication-results": args.auth or "",
    }

    result = detector.analyze_email(headers, args.body)

    verdict_icons = {
        "legitimate": "🟢", "suspicious": "🟡",
        "phishing": "🔴", "unknown": "⚪",
    }
    icon = verdict_icons.get(result.verdict.value, "⚪")

    print(f"\n📧 Email Analysis\n{'='*60}")
    print(f"  From:      {result.target}")
    print(f"  Verdict:   {icon} {result.verdict.value.upper()}")
    print(f"  Confidence:{result.confidence:.0%}")
    print(f"  Risk:      {'█' * int(result.risk_score * 10)}{'░' * (10 - int(result.risk_score * 10))} {result.risk_score:.2f}")

    if result.signals:
        print(f"\n  📡 Signals ({len(result.signals)}):")
        for s in result.signals:
            print(f"    ⚠️  {s.name}: {s.description}")

    print(f"\n  📌 Recommendations:")
    for rec in result.recommendations:
        print(f"    {rec}")


def cmd_text(args):
    """Analyze text for social engineering."""
    result = detector.analyze_text(args.text)

    verdict_icons = {
        "legitimate": "🟢", "suspicious": "🟡",
        "phishing": "🔴", "unknown": "⚪",
    }
    icon = verdict_icons.get(result.verdict.value, "⚪")

    print(f"\n💬 Text Analysis\n{'='*60}")
    print(f"  Text:      {result.target}")
    print(f"  Verdict:   {icon} {result.verdict.value.upper()}")
    print(f"  Confidence:{result.confidence:.0%}")
    print(f"  Risk:      {'█' * int(result.risk_score * 10)}{'░' * (10 - int(result.risk_score * 10))} {result.risk_score:.2f}")

    if result.signals:
        print(f"\n  📡 Signals ({len(result.signals)}):")
        for s in result.signals:
            print(f"    ⚠️  {s.name}: {s.description}")

    print(f"\n  📌 Recommendations:")
    for rec in result.recommendations:
        print(f"    {rec}")


def cmd_batch(args):
    """Batch scan URLs from file."""
    with open(args.file) as f:
        urls = [line.strip() for line in f if line.strip()]

    results = detector.batch_scan_urls(urls)

    print(f"\n📊 Batch Scan — {len(results)} URLs\n{'='*70}")
    print(f"{'URL':<45} {'Verdict':<12} {'Risk':<8} {'Signals'}")
    print("-" * 75)

    phishing = 0
    suspicious = 0
    clean = 0

    for r in results:
        icon = {"legitimate": "🟢", "suspicious": "🟡", "phishing": "🔴"}.get(r.verdict.value, "⚪")
        url_short = r.target[:42] + "..." if len(r.target) > 45 else r.target
        print(f"{url_short:<45} {icon} {r.verdict.value:<10} {r.risk_score:<8.2f} {len(r.signals)}")

        if r.verdict == Verdict.PHISHING:
            phishing += 1
        elif r.verdict == Verdict.SUSPICIOUS:
            suspicious += 1
        else:
            clean += 1

    print(f"\n  Summary:")
    print(f"    🔴 Phishing:    {phishing}")
    print(f"    🟡 Suspicious:  {suspicious}")
    print(f"    🟢 Clean:       {clean}")


def cmd_stats(args):
    """Show scan statistics."""
    stats = detector.get_stats()

    print(f"\n📊 PhishGuard Statistics\n{'='*40}")
    print(f"  Total Scans:      {stats['total_scans']}")
    print(f"  Phishing Found:   {stats['phishing_found']}")
    print(f"  Detection Rate:   {stats['detection_rate']:.1f}%")


def main():
    parser = argparse.ArgumentParser(
        description="🛡️ PhishGuard — Phishing Detection Engine"
    )
    sub = parser.add_subparsers(dest="command")

    # url
    url_p = sub.add_parser("url", help="Analyze URL")
    url_p.add_argument("url", help="URL to analyze")

    # email
    email_p = sub.add_parser("email", help="Analyze email")
    email_p.add_argument("--from", dest="from_addr", required=True)
    email_p.add_argument("--reply-to", default="")
    email_p.add_argument("--auth", default="", help="Authentication-Results header")
    email_p.add_argument("--body", required=True)

    # text
    text_p = sub.add_parser("text", help="Analyze text")
    text_p.add_argument("text", help="Text to analyze")

    # batch
    batch_p = sub.add_parser("batch", help="Batch scan URLs")
    batch_p.add_argument("--file", required=True)

    # stats
    sub.add_parser("stats", help="Scan statistics")

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        return

    commands = {
        "url": cmd_url, "email": cmd_email, "text": cmd_text,
        "batch": cmd_batch, "stats": cmd_stats,
    }
    commands[args.command](args)


if __name__ == "__main__":
    main()
