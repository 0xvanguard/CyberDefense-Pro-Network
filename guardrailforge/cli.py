#!/usr/bin/env python3
"""
GuardRailForge CLI — LLM Guardrail Testing Toolkit

Usage:
    python cli.py test --library owasp_top10 --model gpt-4
    python cli.py test --library all --model gpt-4 -o results.json
    python cli.py libraries
    python cli.py vectors --library jailbreak
    python cli.py report --results results.json
"""

import argparse
import json
import sys
import os
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from src.tester import GuardrailTester, AttackLibrary, Severity


def cmd_test(args):
    """Run guardrail tests."""
    lib = AttackLibrary.load(args.library)
    vectors = lib.vectors

    if args.category:
        vectors = [v for v in vectors if v.category == args.category]
    if args.severity:
        vectors = [v for v in vectors if v.severity.value == args.severity]

    tester = GuardrailTester(
        model=args.model,
        guardrail=args.guardrail,
        delay_ms=args.delay,
    )

    print(f"🛡️  GuardRailForge — LLM Guardrail Testing")
    print(f"   Library: {args.library} ({len(vectors)} vectors)")
    print(f"   Model: {args.model}")
    print(f"   Guardrail: {args.guardrail}")
    print()

    start = time.time()
    results = tester.run(vectors)
    elapsed = time.time() - start

    summary = results.summary()
    print(f"{'='*60}")
    print(f"📊 RESULTS")
    print(f"{'='*60}")
    print(f"   Total tests:   {summary['total_tests']}")
    print(f"   Blocked:       {summary['blocked']} ✅")
    print(f"   Bypassed:      {summary['bypassed']} 🚨")
    print(f"   Partial:       {summary['partial']} ⚠️")
    print(f"   Bypass Rate:   {summary['bypass_rate']}")
    print(f"   Time:          {elapsed:.2f}s")
    print()

    # Severity breakdown
    print(f"📋 SEVERITY BREAKDOWN:")
    for sev, data in summary.get("severity_breakdown", {}).items():
        bar = "█" * data["bypassed"]
        print(f"   {sev:10s} {data['bypassed']}/{data['total']} bypassed {bar}")
    print()

    # Show bypassed vectors
    bypassed = [r for r in results.results if r.verdict.value == "bypassed"]
    if bypassed:
        print(f"🚨 BYPASSED VECTORS ({len(bypassed)}):")
        for r in bypassed[:10]:
            print(f"   [{r.vector.id}] {r.vector.name}")
            print(f"     Category: {r.vector.category} | Severity: {r.vector.severity.value}")
            print(f"     Payload: {r.vector.payload[:80]}")
            print()

    if args.output:
        results.to_json(args.output)
        print(f"📁 Results exported to {args.output}")


def cmd_libraries(args):
    """List all available attack libraries."""
    print(f"📚 GuardRailForge — Attack Libraries")
    print(f"{'='*60}")

    for lib_name in AttackLibrary.LIBRARIES:
        lib = AttackLibrary.load(lib_name)
        cats = {}
        for v in lib.vectors:
            cats[v.category] = cats.get(v.category, 0) + 1
        cat_str = ", ".join(f"{c}:{n}" for c, n in sorted(cats.items()))
        print(f"  📦 {lib_name:20s} {lib.count:3d} vectors  [{cat_str}]")

    # Total
    all_lib = AttackLibrary.load("all")
    print(f"\n  {'='*50}")
    print(f"  📊 Total: {all_lib.count} attack vectors")


def cmd_vectors(args):
    """Show vectors from a library."""
    lib = AttackLibrary.load(args.library)
    vectors = lib.vectors

    if args.category:
        vectors = [v for v in vectors if v.category == args.category]

    print(f"🎯 Attack Vectors — {args.library} ({len(vectors)} vectors)")
    print(f"{'='*60}")

    for v in vectors:
        sev_icon = {"critical": "🔴", "high": "🟠", "medium": "🟡", "low": "🟢", "info": "ℹ️"}
        icon = sev_icon.get(v.severity.value, "❓")
        print(f"  {icon} [{v.id}] {v.name}")
        print(f"     Category: {v.category} | Severity: {v.severity.value}")
        print(f"     Payload: {v.payload[:70]}...")
        print()


def cmd_report(args):
    """Generate report from results."""
    if not os.path.exists(args.results):
        print(f"❌ Results file not found: {args.results}")
        return

    with open(args.results) as f:
        data = json.load(f)

    summary = data.get("summary", {})
    results = data.get("results", [])

    print(f"{'='*60}")
    print(f"📋 GUARDRAIL TEST REPORT")
    print(f"{'='*60}")
    print(f"  Model:     {summary.get('model', 'N/A')}")
    print(f"  Guardrail: {summary.get('guardrail', 'N/A')}")
    print(f"  Tests:     {summary.get('total_tests', 0)}")
    print(f"  Blocked:   {summary.get('blocked', 0)}")
    print(f"  Bypassed:  {summary.get('bypassed', 0)}")
    print(f"  Rate:      {summary.get('bypass_rate', '0%')}")
    print()

    sev_data = summary.get("severity_breakdown", {})
    if sev_data:
        print(f"  SEVERITY BREAKDOWN:")
        for sev, data in sev_data.items():
            pct = (data["bypassed"] / data["total"] * 100) if data["total"] > 0 else 0
            bar = "█" * int(pct / 5)
            print(f"   {sev:10s} {bar} {pct:.0f}% ({data['bypassed']}/{data['total']})")


def main():
    parser = argparse.ArgumentParser(
        description="GuardRailForge — LLM Guardrail Testing Toolkit",
    )
    sub = parser.add_subparsers(dest="command")

    # test
    p_test = sub.add_parser("test", help="Run guardrail tests")
    p_test.add_argument("--library", "-l", default="owasp_top10",
                        choices=AttackLibrary.LIBRARIES + ["all"],
                        help="Attack library to use")
    p_test.add_argument("--model", "-m", default="unknown", help="Model name")
    p_test.add_argument("--guardrail", "-g", default="default", help="Guardrail name")
    p_test.add_argument("--category", "-c", help="Filter by category")
    p_test.add_argument("--severity", "-s", help="Filter by severity")
    p_test.add_argument("--delay", type=int, default=0, help="Delay between tests (ms)")
    p_test.add_argument("--output", "-o", help="Export results to JSON")

    # libraries
    sub.add_parser("libraries", help="List all attack libraries")

    # vectors
    p_vec = sub.add_parser("vectors", help="Show attack vectors")
    p_vec.add_argument("--library", "-l", default="all",
                       choices=AttackLibrary.LIBRARIES + ["all"])
    p_vec.add_argument("--category", "-c", help="Filter by category")

    # report
    p_rep = sub.add_parser("report", help="Generate report from results")
    p_rep.add_argument("--results", "-r", required=True, help="Results JSON file")

    args = parser.parse_args()

    if args.command == "test":
        cmd_test(args)
    elif args.command == "libraries":
        cmd_libraries(args)
    elif args.command == "vectors":
        cmd_vectors(args)
    elif args.command == "report":
        cmd_report(args)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
