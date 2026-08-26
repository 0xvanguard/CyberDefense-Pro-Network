#!/usr/bin/env python3
"""
CyberGuard CLI — Security policy enforcement from the command line.

Usage:
    python cli.py scan --framework SOC2
    python cli.py scan --framework HIPAA --framework PCI-DSS
    python cli.py scan --custom policy.json
    python cli.py report
    python cli.py remediate
    python cli.py frameworks
    python cli.py rules --framework SOC2
"""

import argparse
import json
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "src"))

from enforcer import CyberGuard, ComplianceFramework, Severity


def cmd_scan(args):
    """Scan resources against policies."""
    frameworks = None
    if args.framework:
        frameworks = args.framework

    guard = CyberGuard(frameworks=frameworks, policy_file=args.custom)

    result = guard.scan()

    # Score color
    if result.score >= 80:
        score_icon = "🟢"
    elif result.score >= 60:
        score_icon = "🟡"
    else:
        score_icon = "🔴"

    print(f"\n🔍 CyberGuard Scan Results\n{'='*60}")
    print(f"  Resources:  {result.total_resources}")
    print(f"  Rules:      {result.total_rules}")
    print(f"  Score:      {score_icon} {result.score:.0f}/100")
    print(f"  Violations: {len(result.violations)}")

    if result.violations:
        severity_order = [Severity.CRITICAL, Severity.HIGH, Severity.MEDIUM, Severity.LOW, Severity.INFO]
        severity_icons = {
            "critical": "🔴", "high": "🟠", "medium": "🟡",
            "low": "🟢", "info": "⚪",
        }

        print(f"\n  ⚠️  Violations\n  {'-'*50}")
        for sev in severity_order:
            sev_violations = [v for v in result.violations if v.severity == sev]
            if sev_violations:
                icon = severity_icons.get(sev.value, "⚪")
                print(f"\n  {icon} {sev.value.upper()} ({len(sev_violations)})")
                for v in sev_violations:
                    print(f"    • {v.rule_name}")
                    print(f"      Resource: {v.resource}")
                    print(f"      Current:  {v.current_value} | Expected: {v.expected_value}")
                    print(f"      Action:   {v.action.value}")

    # Remediate if requested
    if args.auto_fix:
        count = guard.remediate(result)
        print(f"\n  🔧 Auto-remediated: {count}/{len(result.violations)} violations")


def cmd_report(args):
    """Generate compliance report."""
    frameworks = None
    if args.framework:
        frameworks = args.framework

    guard = CyberGuard(frameworks=frameworks)
    guard.scan()

    report_text = guard.report(output_file=args.output)

    if not args.output:
        print(report_text)


def cmd_remediate(args):
    """Auto-remediate violations."""
    frameworks = None
    if args.framework:
        frameworks = args.framework

    guard = CyberGuard(frameworks=frameworks)
    guard.scan()

    count = guard.remediate()
    summary = guard.summary()

    print(f"\n🔧 Auto-Remediation Results\n{'='*40}")
    print(f"  Total violations:  {summary['total_violations']}")
    print(f"  Remediated:        {count}")
    print(f"  Remaining:         {summary['total_violations'] - count}")
    print(f"  Score:             {summary['score']:.0f}/100")


def cmd_frameworks(args):
    """List available compliance frameworks."""
    print(f"\n📋 Compliance Frameworks\n{'='*40}")
    for fw in ComplianceFramework:
        rules = CyberGuard.FRAMEWORK_RULES.get(fw, [])
        print(f"  {fw.value:<12} — {len(rules)} rules")


def cmd_rules(args):
    """List rules for a framework."""
    fw = ComplianceFramework(args.framework)
    rules = CyberGuard.FRAMEWORK_RULES.get(fw, [])

    severity_icons = {
        "critical": "🔴", "high": "🟠", "medium": "🟡", "low": "🟢", "info": "⚪",
    }

    print(f"\n📋 {fw.value} Rules ({len(rules)})\n{'='*60}")
    for rule in rules:
        icon = severity_icons.get(rule.severity.value, "⚪")
        print(f"  {icon} {rule.name}")
        print(f"    Resource:   {rule.resource}")
        print(f"    Condition:  {rule.condition}")
        print(f"    Action:     {rule.action.value}")
        print(f"    Severity:   {rule.severity.value}")
        print(f"    {rule.description}")
        print()


def cmd_summary(args):
    """Show latest scan summary."""
    guard = CyberGuard(frameworks=args.framework)
    guard.scan()
    summary = guard.summary()

    print(f"\n📊 Scan Summary\n{'='*40}")
    print(f"  Score:          {summary['score']:.0f}/100")
    print(f"  Violations:     {summary['total_violations']}")
    print(f"  Remediated:     {summary['remediated']}")
    print(f"  Resources:      {summary['resources_scanned']}")
    print(f"  Rules:          {summary['rules_applied']}")

    if summary["by_severity"]:
        print(f"\n  By Severity:")
        severity_icons = {
            "critical": "🔴", "high": "🟠", "medium": "🟡", "low": "🟢", "info": "⚪",
        }
        for sev, count in summary["by_severity"].items():
            icon = severity_icons.get(sev, "⚪")
            print(f"    {icon} {sev:<10} {count}")


def main():
    parser = argparse.ArgumentParser(
        description="🛡️ CyberGuard — Security Policy Enforcement"
    )
    sub = parser.add_subparsers(dest="command")

    # scan
    scan_p = sub.add_parser("scan", help="Scan resources")
    scan_p.add_argument("--framework", "-f", action="append",
                       choices=[fw.value for fw in ComplianceFramework])
    scan_p.add_argument("--custom", "-c", help="Custom policy JSON file")
    scan_p.add_argument("--auto-fix", action="store_true", help="Auto-remediate")

    # report
    report_p = sub.add_parser("report", help="Generate report")
    report_p.add_argument("--framework", "-f", action="append",
                         choices=[fw.value for fw in ComplianceFramework])
    report_p.add_argument("--output", "-o", default="")

    # remediate
    rem_p = sub.add_parser("remediate", help="Auto-remediate")
    rem_p.add_argument("--framework", "-f", action="append",
                      choices=[fw.value for fw in ComplianceFramework])

    # frameworks
    sub.add_parser("frameworks", help="List frameworks")

    # rules
    rules_p = sub.add_parser("rules", help="List framework rules")
    rules_p.add_argument("--framework", "-f", required=True,
                        choices=[fw.value for fw in ComplianceFramework])

    # summary
    sum_p = sub.add_parser("summary", help="Scan summary")
    sum_p.add_argument("--framework", "-f", action="append",
                      choices=[fw.value for fw in ComplianceFramework])

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        return

    commands = {
        "scan": cmd_scan, "report": cmd_report, "remediate": cmd_remediate,
        "frameworks": cmd_frameworks, "rules": cmd_rules, "summary": cmd_summary,
    }
    commands[args.command](args)


if __name__ == "__main__":
    main()
