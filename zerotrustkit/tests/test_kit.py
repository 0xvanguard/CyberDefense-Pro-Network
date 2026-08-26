"""Tests for ZeroTrustKit"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.kit import (
    TrustLevel, Action, DeviceStatus, SessionStatus,
    VerificationResult, Policy, DeviceProfile, Session,
    AuditLog, NetworkSegment, ZeroTrustKit
)


ztk = ZeroTrustKit()


def test_trust_level_enum():
    assert TrustLevel.FULL.value == "full"
    assert TrustLevel.NONE.value == "none"
    print("✅ TrustLevel enum OK")


def test_action_enum():
    assert Action.ALLOW.value == "allow"
    assert Action.BLOCK.value == "block"
    assert Action.QUARANTINE.value == "quarantine"
    print("✅ Action enum OK")


def test_verify_trusted():
    result = ztk.verify(user="john@example.com", device="dev-001",
                        ip="10.0.1.5", location="US")
    assert isinstance(result, VerificationResult)
    assert result.identity_verified is True
    print(f"✅ Verify trusted: {result.action.value}, risk={result.risk_score:.2f}")


def test_verify_blocked_ip():
    ztk.block_ip("192.168.1.100")
    result = ztk.verify(user="hacker", ip="192.168.1.100")
    assert result.action == Action.BLOCK
    assert result.risk_score == 1.0
    print("✅ Verify blocked IP: BLOCKED")


def test_verify_untrusted_location():
    result = ztk.verify(user="john", location="XX")
    assert result.location_trusted is False
    assert result.risk_score > 0.1
    print(f"✅ Verify untrusted location: risk={result.risk_score:.2f}")


def test_verify_admin_without_mfa():
    result = ztk.verify(user="admin", role="admin", mfa=False)
    assert any("MFA" in r or "mfa" in r.lower() for r in result.reasons)
    print("✅ Verify admin no MFA: step_up required")


def test_register_device():
    profile = ztk.register_device(
        device_id="dev-mac-001", name="MacBook Pro",
        os="macOS 14", browser="Safari",
        trust_level=TrustLevel.HIGH, mfa_enabled=True,
    )
    assert profile.device_id == "dev-mac-001"
    assert profile.is_trusted is True
    assert profile.mfa_enabled is True
    print(f"✅ Register device: {profile.name} (trusted={profile.is_trusted})")


def test_revoke_device():
    ztk.register_device("dev-test-001", "Test Device")
    ok = ztk.revoke_device("dev-test-001")
    assert ok is True
    device = ztk.get_device("dev-test-001")
    assert device.status == DeviceStatus.REVOKED
    assert device.is_trusted is False
    print("✅ Revoke device: REVOKED")


def test_mark_compromised():
    ztk.register_device("dev-comp-001", "Compromised Device")
    ok = ztk.mark_compromised("dev-comp-001")
    assert ok is True
    device = ztk.get_device("dev-comp-001")
    assert device.status == DeviceStatus.COMPROMISED
    print("✅ Mark compromised: COMPROMISED")


def test_verify_compromised_device():
    ztk.register_device("dev-bad-001", "Bad Device")
    ztk.mark_compromised("dev-bad-001")
    result = ztk.verify(user="john", device="dev-bad-001")
    assert result.action == Action.QUARANTINE
    print("✅ Verify compromised device: QUARANTINE")


def test_create_session():
    session = ztk.create_session(user="john@example.com", ip="10.0.1.5")
    assert session.session_id.startswith("sess_")
    assert session.is_valid is True
    assert session.user == "john@example.com"
    print(f"✅ Create session: {session.session_id[:20]}...")


def test_validate_session():
    session = ztk.create_session(user="jane@example.com")
    valid = ztk.validate_session(session.session_id)
    assert valid is not None
    assert valid.user == "jane@example.com"
    print("✅ Validate session: VALID")


def test_revoke_session():
    session = ztk.create_session(user="bob@example.com")
    ok = ztk.revoke_session(session.session_id)
    assert ok is True
    valid = ztk.validate_session(session.session_id)
    assert valid is None
    print("✅ Revoke session: REVOKED")


def test_network_segment():
    seg = NetworkSegment(
        name="corporate", cidr="10.0.0.0/8", zone="trusted",
        trust_level=TrustLevel.HIGH, allowed_services=["ssh", "https"],
    )
    assert seg.contains_ip("10.0.1.5") is True
    assert seg.contains_ip("192.168.1.1") is False
    assert seg.allows_service("ssh") is True
    assert seg.allows_service("ftp") is False
    print("✅ Network segment: corporate trust zone")


def test_check_network_access():
    result = ztk.check_network_access("10.0.1.5", "https")
    assert result["allowed"] is True
    assert result["zone"] == "trusted"
    print(f"✅ Network access: {result['reason']}")


def test_check_network_blocked():
    result = ztk.check_network_access("10.0.1.5", "ftp")
    assert result["allowed"] is False
    print(f"✅ Network blocked: {result['reason']}")


def test_add_policy():
    custom = Policy("P100", "Custom Rule", {"role": "guest"}, Action.DENY, 99)
    ztk.add_policy(custom)
    policies = ztk.get_policies()
    assert any(p.id == "P100" for p in policies)
    print("✅ Add custom policy")


def test_remove_policy():
    ztk.add_policy(Policy("P-temp", "Temp Rule", {}, Action.ALLOW, 0))
    ok = ztk.remove_policy("P-temp")
    assert ok is True
    assert not any(p.id == "P-temp" for p in ztk.policies)
    print("✅ Remove policy")


def test_audit_log():
    ztk.verify(user="audit-test", ip="10.0.0.1")
    logs = ztk.get_audit_log(user="audit-test")
    assert len(logs) > 0
    assert logs[-1].user == "audit-test"
    print(f"✅ Audit log: {len(logs)} entries")


def test_get_stats():
    stats = ztk.get_stats()
    assert "policies" in stats
    assert "devices" in stats
    assert "sessions" in stats
    assert stats["policies"] > 0
    print(f"✅ Stats: {stats['policies']} policies, {stats['devices']} devices")


def test_export_config():
    config = ztk.export_config()
    assert "policies" in config
    assert "devices" in config
    assert "segments" in config
    print("✅ Export config OK")


def test_device_profile_to_dict():
    profile = ztk.register_device("dev-dict", "Dict Device")
    d = profile.to_dict()
    assert d["device_id"] == "dev-dict"
    assert "is_trusted" in d
    print("✅ DeviceProfile to_dict OK")


def test_session_to_dict():
    session = ztk.create_session(user="dict-test")
    d = session.to_dict()
    assert d["user"] == "dict-test"
    assert "is_valid" in d
    print("✅ Session to_dict OK")


if __name__ == "__main__":
    test_trust_level_enum()
    test_action_enum()
    test_verify_trusted()
    test_verify_blocked_ip()
    test_verify_untrusted_location()
    test_verify_admin_without_mfa()
    test_register_device()
    test_revoke_device()
    test_mark_compromised()
    test_verify_compromised_device()
    test_create_session()
    test_validate_session()
    test_revoke_session()
    test_network_segment()
    test_check_network_access()
    test_check_network_blocked()
    test_add_policy()
    test_remove_policy()
    test_audit_log()
    test_get_stats()
    test_export_config()
    test_device_profile_to_dict()
    test_session_to_dict()
    print("\n🎉 All 22 tests passed!")
