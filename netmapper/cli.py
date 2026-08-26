#!/usr/bin/env python3
"""
NetMapper CLI — Network scanning from the command line.

Usage:
    python cli.py scan 192.168.1.0/24
    python cli.py scan 10.0.0.1 --ports 22,80,443
    python cli.py host 192.168.1.1
    python cli.py export --output topology.json
    python cli.py stats
    python cli.py vulns
"""

import argparse
import json
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "src"))

from scanner import NetworkMapper, HostStatus, PortState


def cmd_scan(args):
    """Scan a network range."""
    ports = None
    if args.ports:
        ports = [int(p.strip()) for p in args.ports.split(",")]

    mapper = NetworkMapper(
        target=args.target, ports=ports,
        timeout=args.timeout,
    )

    print(f"\n🔍 Scanning {args.target}...")
    print(f"   Ports: {len(mapper.ports)} | Timeout: {args.timeout}s\n")

    topology = mapper.scan()

    # Summary
    summary = topology.get_summary()
    print(f"📊 Scan Results\n{'='*60}")
    print(f"  Network:       {topology.network_range}")
    print(f"  Hosts:         {topology.active_hosts}/{topology.total_hosts} active")
    print(f"  Open Ports:    {topology.total_open_ports}")
    print(f"  Vulnerabilities: {topology.total_vulnerabilities}")
    print(f"  Duration:      {topology.scan_duration:.2f}s")

    # Active hosts
    active = [h for h in topology.hosts if h.status == HostStatus.UP]
    if active:
        print(f"\n🖥️  Active Hosts ({len(active)})\n{'-'*60}")
        print(f"{'IP':<18} {'Hostname':<25} {'OS':<22} {'Ports'}")
        print("-" * 70)
        for h in active:
            hostname = h.hostname[:22] if h.hostname else "N/A"
            os_guess = h.os_guess[:20] if h.os_guess else "N/A"
            print(f"{h.ip:<18} {hostname:<25} {os_guess:<22} {h.open_ports}")

    # Top services
    if summary["top_services"]:
        print(f"\n📡 Top Services")
        for svc, count in summary["top_services"][:5]:
            bar = "█" * count
            print(f"  {svc:<15} {bar} ({count})")

    # Vulnerabilities
    all_vulns = []
    for h in topology.hosts:
        for v in h.vulnerabilities:
            all_vulns.append({"host": h.ip, **v})

    if all_vulns:
        risk_icons = {"critical": "🔴", "high": "🟠", "medium": "🟡", "low": "🟢"}
        print(f"\n⚠️  Vulnerabilities ({len(all_vulns)})\n{'-'*60}")
        for v in all_vulns:
            icon = risk_icons.get(v["risk"], "⚪")
            print(f"  {icon} {v['host']}:{v['port']} — {v['service']}")
            print(f"     {v['issue']}")

    # Export
    if args.output:
        topology.to_json(args.output)
        print(f"\n💾 Exported to {args.output}")


def cmd_host(args):
    """Scan a single host."""
    mapper = NetworkMapper(target=args.ip, timeout=args.timeout)
    host = mapper.scan_single(args.ip)

    status_icon = "🟢" if host.status == HostStatus.UP else "🔴"

    print(f"\n🖥️  Host: {args.ip}\n{'='*50}")
    print(f"  Status:   {status_icon} {host.status.value}")
    print(f"  Hostname: {host.hostname or 'N/A'}")
    print(f"  OS:       {host.os_guess or 'Unknown'}")
    print(f"  Latency:  {host.latency_ms:.1f}ms")

    if host.ports:
        open_ports = [p for p in host.ports if p.state == PortState.OPEN]
        if open_ports:
            print(f"\n  📡 Open Ports ({len(open_ports)})\n  {'-'*45}")
            risk_icons = {"critical": "🔴", "high": "🟠", "medium": "🟡", "low": "🟢"}
            for p in open_ports:
                icon = risk_icons.get(p.risk, "⚪")
                print(f"  {icon} {p.port:<8} {p.service:<15} {p.risk}")

    if host.vulnerabilities:
        print(f"\n  ⚠️  Vulnerabilities ({len(host.vulnerabilities)})")
        for v in host.vulnerabilities:
            print(f"     🔴 {v['service']}: {v['issue']}")


def cmd_export(args):
    """Export last scan."""
    print(f"💡 Use 'scan --output {args.output}' to export during scan")


def cmd_vulns(args):
    """Show known vulnerable services."""
    from scanner import VULNERABLE_SERVICES

    print(f"\n⚠️  Known Vulnerable Services\n{'='*60}")
    risk_icons = {"critical": "🔴", "high": "🟠", "medium": "🟡", "low": "🟢"}

    for svc, info in sorted(VULNERABLE_SERVICES.items(), key=lambda x: x[1]["risk"]):
        icon = risk_icons.get(info["risk"], "⚪")
        print(f"  {icon} {svc:<20} [{info['risk'].upper()}]")
        print(f"     {info['issue']}")


def cmd_stats(args):
    """Show mapper statistics."""
    print(f"\n📊 NetMapper Statistics\n{'='*40}")
    print(f"  Target:         192.168.1.0/24 (default)")
    print(f"  Ports:          {len([21,22,23,25,53,80,110,135,139,143,443,445,993,995,1433,1521,3306,3389,5432,5900,6379,8080,8443,27017])}")
    print(f"  Timeout:        1.0s")
    print(f"  Max Hosts:      256")


def main():
    parser = argparse.ArgumentParser(
        description="🔍 NetMapper — Network Scanner & Topology Mapper"
    )
    sub = parser.add_subparsers(dest="command")

    # scan
    scan_p = sub.add_parser("scan", help="Scan network")
    scan_p.add_argument("target", help="Target IP or CIDR (e.g., 192.168.1.0/24)")
    scan_p.add_argument("--ports", default="", help="Comma-separated ports")
    scan_p.add_argument("--timeout", type=float, default=1.0)
    scan_p.add_argument("--output", "-o", default="")

    # host
    host_p = sub.add_parser("host", help="Scan single host")
    host_p.add_argument("ip", help="Target IP")
    host_p.add_argument("--timeout", type=float, default=1.0)

    # export
    export_p = sub.add_parser("export", help="Export topology")
    export_p.add_argument("--output", "-o", default="topology.json")

    # vulns
    sub.add_parser("vulns", help="Known vulnerable services")

    # stats
    sub.add_parser("stats", help="Mapper statistics")

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        return

    commands = {
        "scan": cmd_scan, "host": cmd_host, "export": cmd_export,
        "vulns": cmd_vulns, "stats": cmd_stats,
    }
    commands[args.command](args)


if __name__ == "__main__":
    main()
