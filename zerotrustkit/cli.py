#!/usr/bin/env python3
"""
ZeroTrustKit CLI — Zero Trust security from the command line.

Usage:
    python cli.py verify --user john@example.com --device iPhone-14 --ip 10.0.1.5
    python cli.py register --device-id dev-001 --name "MacBook Pro"
    python cli.py revoke --device-id dev-001
    python cli.py session --user john@example.com --create
    python cli.py policies
    python cli.py segments
    python cli.py audit --limit 20
    python cli.py stats
    python cli.py export
"""

import argparse
import json
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "src"))

from kit import ZeroTrustKit, TrustLevel, DeviceStatus, Policy, Action


ztk = ZeroTrustKit()


def cmd_verify(args):
    """Verify a request."""
    result = ztk.verify(
        user=args.user, device=args.device, ip=args.ip,
        location=args.location, role=args.role, mfa=args.mfa,
    )

    icons = {
        "allow": "🟢", "monitor": "🟡", "step_up": "🟠",
        "block": "🔴", "quarantine": "🟠", "deny": "🔴",
    }
    icon = icons.get(result.action.value, "⚪")

    print(f"\n🔐 Zero Trust Verification\n{'='*50}")
    print(f"  User:    {args.user}")
    print(f"  Device:  {args.device or 'N/A'}")
    print(f"  IP:      {args.ip or 'N/A'}")
    print(f"  Location:{args.location or 'N/A'}")
    print(f"\n  {icon} Action:     {result.action.value.upper()}")
    print(f"  📊 Risk Score: {result.risk_score:.2f}")
    print(f"  🛡️  Trust:      {result.trust_level.value}")
    print(f"\n  Reasons:")
    for r in result.reasons:
        print(f"    • {r}")


def cmd_register(args):
    """Register a device."""
    tl = TrustLevel(args.trust)
    profile = ztk.register_device(
        device_id=args.device_id, name=args.name,
        os=args.os, browser=args.browser,
        trust_level=tl, mfa_enabled=args.mfa,
    )
    print(f"\n📱 Device Registered\n{'='*40}")
    print(f"  ID:      {profile.device_id}")
    print(f"  Name:    {profile.name}")
    print(f"  OS:      {profile.os or 'N/A'}")
    print(f"  Trust:   {profile.trust_level.value}")
    print(f"  MFA:     {'✅' if profile.mfa_enabled else '❌'}")
    print(f"  Status:  {profile.status.value}")


def cmd_revoke(args):
    """Revoke or compromise a device."""
    if args.compromised:
        ok = ztk.mark_compromised(args.device_id)
        action = "marked COMPROMISED"
    else:
        ok = ztk.revoke_device(args.device_id)
        action = "REVOKED"

    if ok:
        print(f"\n⚠️  Device {action}: {args.device_id}")
    else:
        print(f"\n❌ Device not found: {args.device_id}")


def cmd_devices(args):
    """List devices."""
    status_filter = None
    if args.status:
        status_filter = DeviceStatus(args.status)

    devices = ztk.list_devices(status=status_filter)

    print(f"\n📱 Devices ({len(devices)})\n{'='*60}")
    print(f"{'ID':<15} {'Name':<20} {'Trust':<10} {'Status':<15} {'MFA'}")
    print("-" * 65)

    for d in devices:
        mfa = "✅" if d.mfa_enabled else "❌"
        status_icon = {
            "registered": "🟢", "pending": "🟡",
            "revoked": "🔴", "compromised": "⚫",
        }.get(d.status.value, "⚪")
        print(f"{d.device_id:<15} {d.name:<20} {d.trust_level.value:<10} "
              f"{status_icon} {d.status.value:<12} {mfa}")


def cmd_session(args):
    """Manage sessions."""
    if args.create:
        session = ztk.create_session(
            user=args.user, device_id=args.device,
            ip=args.ip, location=args.location,
        )
        print(f"\n🔑 Session Created\n{'='*40}")
        print(f"  ID:     {session.session_id}")
        print(f"  User:   {session.user}")
        print(f"  Expires:{session.expires_at}")
    elif args.revoke:
        sessions = ztk.get_user_sessions(args.user)
        for s in sessions:
            if s.is_valid:
                ztk.revoke_session(s.session_id)
                print(f"  Revoked: {s.session_id}")
    elif args.validate:
        session = ztk.validate_session(args.validate)
        if session:
            print(f"\n✅ Session Valid: {session.session_id}")
            print(f"   User: {session.user}, Trust: {session.trust_level.value}")
        else:
            print(f"\n❌ Session Invalid or Expired: {args.validate}")
    else:
        sessions = ztk.get_user_sessions(args.user) if args.user else list(ztk.sessions.values())
        print(f"\n🔑 Sessions ({len(sessions)})\n{'='*60}")
        for s in sessions:
            status_icon = "🟢" if s.is_valid else "🔴"
            print(f"  {status_icon} {s.session_id[:20]}... | {s.user} | {s.status.value}")


def cmd_policies(args):
    """List policies."""
    policies = ztk.get_policies()

    print(f"\n📋 Policies ({len(policies)})\n{'='*60}")
    print(f"{'ID':<8} {'Priority':<10} {'Action':<12} {'Enabled':<10} {'Name'}")
    print("-" * 65)

    for p in policies:
        enabled = "✅" if p.enabled else "❌"
        print(f"{p.id:<8} {p.priority:<10} {p.action.value:<12} {enabled:<10} {p.name}")


def cmd_segments(args):
    """List network segments."""
    segments = ztk.network_segments

    print(f"\n🌐 Network Segments ({len(segments)})\n{'='*60}")
    for seg in segments:
        icon = {"trusted": "🟢", "dmz": "🟡", "untrusted": "🔴"}.get(seg.zone, "⚪")
        print(f"\n  {icon} {seg.name} ({seg.cidr})")
        print(f"     Zone: {seg.zone} | Trust: {seg.trust_level.value}")
        if seg.allowed_services:
            print(f"     Services: {', '.join(seg.allowed_services)}")
        if seg.blocked_services:
            print(f"     Blocked:  {', '.join(seg.blocked_services)}")


def cmd_audit(args):
    """Show audit log."""
    logs = ztk.get_audit_log(user=args.user, event=args.event, limit=args.limit)

    print(f"\n📝 Audit Log ({len(logs)} entries)\n{'='*70}")
    print(f"{'Time':<22} {'Event':<20} {'User':<20} {'Action'}")
    print("-" * 70)

    for log in logs[-args.limit:]:
        ts = log.timestamp[:19]
        print(f"{ts:<22} {log.event:<20} {log.user:<20} {log.action}")


def cmd_block(args):
    """Block/unblock IPs."""
    if args.unblock:
        ok = ztk.unblock_ip(args.ip)
        print(f"{'✅' if ok else '❌'} IP {args.ip} {'unblocked' if ok else 'not found'}")
    else:
        ztk.block_ip(args.ip)
        print(f"🚫 IP blocked: {args.ip}")


def cmd_stats(args):
    """Show statistics."""
    stats = ztk.get_stats()

    print(f"\n📊 ZeroTrustKit Statistics\n{'='*40}")
    print(f"  Policies:        {stats['active_policies']}/{stats['policies']} active")
    print(f"  Devices:         {stats['active_devices']}/{stats['devices']} registered")
    print(f"  Sessions:        {stats['active_sessions']}/{stats['sessions']} active")
    print(f"  Blocked IPs:     {stats['blocked_ips']}")
    print(f"  Segments:        {stats['segments']}")
    print(f"  Audit Entries:   {stats['audit_entries']}")


def cmd_export(args):
    """Export configuration."""
    config = ztk.export_config()
    with open(args.output, "w") as f:
        json.dump(config, f, indent=2)
    print(f"\n✅ Config exported to {args.output}")


def main():
    parser = argparse.ArgumentParser(
        description="🛡️ ZeroTrustKit — Zero Trust Security"
    )
    sub = parser.add_subparsers(dest="command")

    # verify
    verify_p = sub.add_parser("verify", help="Verify request")
    verify_p.add_argument("--user", required=True)
    verify_p.add_argument("--device", default="")
    verify_p.add_argument("--ip", default="")
    verify_p.add_argument("--location", default="")
    verify_p.add_argument("--role", default="user")
    verify_p.add_argument("--mfa", action="store_true")

    # register
    reg_p = sub.add_parser("register", help="Register device")
    reg_p.add_argument("--device-id", required=True)
    reg_p.add_argument("--name", required=True)
    reg_p.add_argument("--os", default="")
    reg_p.add_argument("--browser", default="")
    reg_p.add_argument("--trust", default="medium",
                       choices=["none", "low", "medium", "high", "full"])
    reg_p.add_argument("--mfa", action="store_true")

    # revoke
    rev_p = sub.add_parser("revoke", help="Revoke device")
    rev_p.add_argument("--device-id", required=True)
    rev_p.add_argument("--compromised", action="store_true")

    # devices
    dev_p = sub.add_parser("devices", help="List devices")
    dev_p.add_argument("--status", choices=["registered", "pending", "revoked", "compromised"])

    # session
    sess_p = sub.add_parser("session", help="Manage sessions")
    sess_p.add_argument("--user", default="")
    sess_p.add_argument("--device", default="")
    sess_p.add_argument("--ip", default="")
    sess_p.add_argument("--location", default="")
    sess_p.add_argument("--create", action="store_true")
    sess_p.add_argument("--validate", default="")
    sess_p.add_argument("--revoke", action="store_true")

    # policies
    sub.add_parser("policies", help="List policies")

    # segments
    sub.add_parser("segments", help="List segments")

    # audit
    audit_p = sub.add_parser("audit", help="Audit log")
    audit_p.add_argument("--user", default="")
    audit_p.add_argument("--event", default="")
    audit_p.add_argument("--limit", type=int, default=20)

    # block
    block_p = sub.add_parser("block", help="Block/unblock IPs")
    block_p.add_argument("--ip", required=True)
    block_p.add_argument("--unblock", action="store_true")

    # stats
    sub.add_parser("stats", help="Statistics")

    # export
    export_p = sub.add_parser("export", help="Export config")
    export_p.add_argument("--output", default="zerotrust-config.json")

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        return

    commands = {
        "verify": cmd_verify, "register": cmd_register, "revoke": cmd_revoke,
        "devices": cmd_devices, "session": cmd_session, "policies": cmd_policies,
        "segments": cmd_segments, "audit": cmd_audit, "block": cmd_block,
        "stats": cmd_stats, "export": cmd_export,
    }
    commands[args.command](args)


if __name__ == "__main__":
    main()
