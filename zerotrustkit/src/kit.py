"""ZeroTrustKit — Zero Trust Security Implementation Toolkit

Implement zero trust architecture with identity verification, device profiling,
network segmentation, session management, and audit logging.
"""

import hashlib
import secrets
import json
from dataclasses import dataclass, field, asdict
from typing import List, Dict, Optional, Any
from datetime import datetime, timedelta
from enum import Enum


# ─── Enums ───────────────────────────────────────────────────────────

class TrustLevel(Enum):
    NONE = "none"
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    FULL = "full"


class Action(Enum):
    ALLOW = "allow"
    DENY = "deny"
    STEP_UP = "step_up"
    MONITOR = "monitor"
    BLOCK = "block"
    QUARANTINE = "quarantine"


class DeviceStatus(Enum):
    REGISTERED = "registered"
    PENDING = "pending"
    REVOKED = "revoked"
    COMPROMISED = "compromised"


class SessionStatus(Enum):
    ACTIVE = "active"
    EXPIRED = "expired"
    REVOKED = "revoked"
    SUSPICIOUS = "suspicious"


# ─── Data Models ─────────────────────────────────────────────────────

@dataclass
class VerificationResult:
    """Result of identity verification."""
    trusted: bool
    trust_level: TrustLevel
    risk_score: float
    action: Action
    reasons: List[str]
    device_trusted: bool = False
    location_trusted: bool = False
    identity_verified: bool = False

    def to_dict(self) -> Dict[str, Any]:
        d = asdict(self)
        d["trust_level"] = self.trust_level.value
        d["action"] = self.action.value
        return d


@dataclass
class Policy:
    """Access policy rule."""
    id: str
    name: str
    conditions: Dict[str, Any]
    action: Action
    priority: int = 0
    enabled: bool = True
    description: str = ""

    def to_dict(self) -> Dict[str, Any]:
        d = asdict(self)
        d["action"] = self.action.value
        return d


@dataclass
class DeviceProfile:
    """Trusted device profile."""
    device_id: str
    name: str
    os: str = ""
    browser: str = ""
    trust_level: TrustLevel = TrustLevel.MEDIUM
    status: DeviceStatus = DeviceStatus.REGISTERED
    registered_at: str = ""
    last_seen: str = ""
    mfa_enabled: bool = False
    certificates: List[str] = field(default_factory=list)
    tags: List[str] = field(default_factory=list)

    def __post_init__(self):
        if not self.registered_at:
            self.registered_at = datetime.now().isoformat()
        if not self.last_seen:
            self.last_seen = self.registered_at

    @property
    def is_trusted(self) -> bool:
        return self.status == DeviceStatus.REGISTERED and self.trust_level.value in ("high", "full")

    def to_dict(self) -> Dict[str, Any]:
        d = asdict(self)
        d["trust_level"] = self.trust_level.value
        d["status"] = self.status.value
        d["is_trusted"] = self.is_trusted
        return d


@dataclass
class Session:
    """User session with risk tracking."""
    session_id: str
    user: str
    device_id: str = ""
    ip: str = ""
    location: str = ""
    status: SessionStatus = SessionStatus.ACTIVE
    trust_level: TrustLevel = TrustLevel.LOW
    risk_score: float = 0.0
    created_at: str = ""
    expires_at: str = ""
    last_activity: str = ""
    activities: List[Dict[str, str]] = field(default_factory=list)

    def __post_init__(self):
        if not self.created_at:
            self.created_at = datetime.now().isoformat()
        if not self.last_activity:
            self.last_activity = self.created_at
        if not self.expires_at:
            dt = datetime.now() + timedelta(hours=8)
            self.expires_at = dt.isoformat()

    @property
    def is_expired(self) -> bool:
        try:
            exp = datetime.fromisoformat(self.expires_at)
            return datetime.now() > exp
        except (ValueError, TypeError):
            return True

    @property
    def is_valid(self) -> bool:
        return self.status == SessionStatus.ACTIVE and not self.is_expired

    def to_dict(self) -> Dict[str, Any]:
        d = asdict(self)
        d["status"] = self.status.value
        d["trust_level"] = self.trust_level.value
        d["is_expired"] = self.is_expired
        d["is_valid"] = self.is_valid
        return d


@dataclass
class AuditLog:
    """Audit log entry."""
    timestamp: str
    event: str
    user: str
    source_ip: str = ""
    action: str = ""
    result: str = ""
    details: Dict[str, Any] = field(default_factory=dict)

    def __post_init__(self):
        if not self.timestamp:
            self.timestamp = datetime.now().isoformat()

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


@dataclass
class NetworkSegment:
    """Network microsegment definition."""
    name: str
    cidr: str
    zone: str  # "trusted", "dmz", "untrusted"
    trust_level: TrustLevel = TrustLevel.MEDIUM
    allowed_services: List[str] = field(default_factory=list)
    blocked_services: List[str] = field(default_factory=list)
    description: str = ""

    def contains_ip(self, ip: str) -> bool:
        """Check if IP is in this segment (simplified CIDR match)."""
        parts = self.cidr.split("/")
        net_ip = parts[0]
        prefix_len = int(parts[1]) if len(parts) > 1 else 32

        def to_int(addr: str) -> int:
            octets = addr.split(".")
            return (int(octets[0]) << 24) | (int(octets[1]) << 16) | (int(octets[2]) << 8) | int(octets[3])

        mask = (0xFFFFFFFF << (32 - prefix_len)) & 0xFFFFFFFF
        try:
            return (to_int(ip) & mask) == (to_int(net_ip) & mask)
        except (ValueError, IndexError):
            return False

    def allows_service(self, service: str) -> bool:
        if self.blocked_services:
            return service not in self.blocked_services
        if self.allowed_services:
            return service in self.allowed_services
        return True

    def to_dict(self) -> Dict[str, Any]:
        d = asdict(self)
        d["trust_level"] = self.trust_level.value
        return d


# ─── Engine ──────────────────────────────────────────────────────────

class ZeroTrustKit:
    """
    Zero Trust security implementation.

    Usage:
        ztk = ZeroTrustKit()
        result = ztk.verify(user="john@example.com", device="iPhone-14", ...)
        session = ztk.create_session(user="john@example.com")
    """

    def __init__(self):
        self.policies: List[Policy] = []
        self.devices: Dict[str, DeviceProfile] = {}
        self.sessions: Dict[str, Session] = {}
        self.audit_log: List[AuditLog] = []
        self.blocked_ips: List[str] = []
        self.network_segments: List[NetworkSegment] = []
        self._load_default_policies()
        self._load_default_segments()

    def _load_default_policies(self):
        """Load default zero trust policies."""
        self.policies = [
            Policy("P001", "Block known bad IPs",
                   {"ip": "blocked"}, Action.BLOCK, 100, True, "Block known malicious IPs"),
            Policy("P002", "Require MFA for admin",
                   {"role": "admin", "mfa": False}, Action.STEP_UP, 90, True, "Admins need MFA"),
            Policy("P003", "Allow trusted devices",
                   {"device_trusted": True, "identity_verified": True},
                   Action.ALLOW, 80, True, "Trusted verified devices get access"),
            Policy("P004", "Monitor unknown devices",
                   {"device_trusted": False}, Action.MONITOR, 50, True, "Watch unknown devices"),
            Policy("P005", "Block off-hours admin",
                   {"role": "admin", "off_hours": True}, Action.DENY, 95, True, "No admin at 3am"),
            Policy("P006", "Quarantine compromised devices",
                   {"device_status": "compromised"}, Action.QUARANTINE, 100, True, "Isolate compromised devices"),
        ]

    def _load_default_segments(self):
        """Load default network segments."""
        self.network_segments = [
            NetworkSegment("corporate", "10.0.0.0/8", "trusted",
                          TrustLevel.HIGH, ["ssh", "https", "ldap"]),
            NetworkSegment("dmz", "172.16.0.0/12", "dmz",
                          TrustLevel.MEDIUM, ["https", "smtp"]),
            NetworkSegment("guest", "192.168.0.0/16", "untrusted",
                          TrustLevel.LOW, ["https"]),
        ]

    # ─── Identity Verification ───────────────────────────────────────

    def verify(self, user: str, device: str = "", ip: str = "",
               location: str = "", role: str = "user",
               mfa: bool = False, **kwargs) -> VerificationResult:
        """
        Verify a request against zero trust policies.
        """
        risk_score = 0.0
        reasons = []

        # 1. Check IP blocklist
        if ip in self.blocked_ips:
            self._audit("verify", user, "BLOCK", "IP blocked", {"ip": ip})
            return VerificationResult(
                trusted=False, trust_level=TrustLevel.NONE,
                risk_score=1.0, action=Action.BLOCK,
                reasons=["IP is blocked"]
            )

        # 2. Check device
        device_trusted = False
        if device and device in self.devices:
            profile = self.devices[device]
            if profile.status == DeviceStatus.COMPROMISED:
                self._audit("verify", user, "QUARANTINE", "Compromised device", {"device": device})
                return VerificationResult(
                    trusted=False, trust_level=TrustLevel.NONE,
                    risk_score=1.0, action=Action.QUARANTINE,
                    reasons=["Device is compromised"], device_trusted=False
                )
            device_trusted = profile.is_trusted
            if not device_trusted:
                risk_score += 0.2
                reasons.append("Device not fully trusted")
        elif device:
            risk_score += 0.3
            reasons.append("Unknown device")

        # 3. Check location
        trusted_locations = ["US", "CA", "UK", "DE", "FR", "JP", "AU", "NL"]
        location_trusted = location in trusted_locations
        if not location_trusted and location:
            risk_score += 0.2
            reasons.append("Untrusted location")

        # 4. Check time
        hour = datetime.now().hour
        off_hours = hour < 6 or hour > 22
        if off_hours:
            risk_score += 0.1
            reasons.append("Off-hours access")

        # 5. Check role
        if role == "admin":
            risk_score += 0.1
            reasons.append("Admin role detected")
            if not mfa:
                risk_score += 0.2
                reasons.append("Admin without MFA")

        # 6. Check network segment
        if ip:
            segment = self._get_segment(ip)
            if segment and segment.zone == "untrusted":
                risk_score += 0.2
                reasons.append(f"Request from untrusted segment ({segment.name})")

        # Determine action
        risk_score = min(risk_score, 1.0)
        if risk_score > 0.7:
            action = Action.BLOCK
        elif risk_score > 0.5:
            action = Action.QUARANTINE
        elif risk_score > 0.3:
            action = Action.STEP_UP
        elif risk_score > 0.15:
            action = Action.MONITOR
        else:
            action = Action.ALLOW

        trust_level = (
            TrustLevel.FULL if risk_score < 0.05 else
            TrustLevel.HIGH if risk_score < 0.2 else
            TrustLevel.MEDIUM if risk_score < 0.4 else
            TrustLevel.LOW if risk_score < 0.7 else
            TrustLevel.NONE
        )

        if not reasons:
            reasons.append("All checks passed")

        self._audit("verify", user, action.value,
                     f"Risk: {risk_score:.2f}", {"reasons": reasons})

        return VerificationResult(
            trusted=action == Action.ALLOW,
            trust_level=trust_level,
            risk_score=risk_score,
            action=action,
            reasons=reasons,
            device_trusted=device_trusted,
            location_trusted=location_trusted,
            identity_verified=True,
        )

    # ─── Device Management ───────────────────────────────────────────

    def register_device(self, device_id: str, name: str, os: str = "",
                       browser: str = "", trust_level: TrustLevel = TrustLevel.MEDIUM,
                       mfa_enabled: bool = False) -> DeviceProfile:
        """Register a new device."""
        profile = DeviceProfile(
            device_id=device_id, name=name, os=os, browser=browser,
            trust_level=trust_level, mfa_enabled=mfa_enabled,
            status=DeviceStatus.REGISTERED,
        )
        self.devices[device_id] = profile
        self._audit("device_register", name, "register", f"Device {device_id}")
        return profile

    def revoke_device(self, device_id: str) -> bool:
        """Revoke device trust."""
        if device_id in self.devices:
            self.devices[device_id].status = DeviceStatus.REVOKED
            self._audit("device_revoke", device_id, "revoke", "Device revoked")
            return True
        return False

    def mark_compromised(self, device_id: str) -> bool:
        """Mark device as compromised."""
        if device_id in self.devices:
            self.devices[device_id].status = DeviceStatus.COMPROMISED
            self._audit("device_compromised", device_id, "quarantine", "Device compromised")
            return True
        return False

    def get_device(self, device_id: str) -> Optional[DeviceProfile]:
        return self.devices.get(device_id)

    def list_devices(self, status: Optional[DeviceStatus] = None) -> List[DeviceProfile]:
        devices = list(self.devices.values())
        if status:
            devices = [d for d in devices if d.status == status]
        return devices

    # ─── Session Management ──────────────────────────────────────────

    def create_session(self, user: str, device_id: str = "",
                      ip: str = "", location: str = "",
                      ttl_hours: int = 8) -> Session:
        """Create a new session."""
        session_id = f"sess_{secrets.token_hex(16)}"
        session = Session(
            session_id=session_id, user=user, device_id=device_id,
            ip=ip, location=location, status=SessionStatus.ACTIVE,
        )
        self.sessions[session_id] = session
        self._audit("session_create", user, "create", f"Session {session_id}")
        return session

    def validate_session(self, session_id: str) -> Optional[Session]:
        """Validate and return session if active."""
        session = self.sessions.get(session_id)
        if not session:
            return None
        if session.is_expired:
            session.status = SessionStatus.EXPIRED
            return None
        if session.status != SessionStatus.ACTIVE:
            return None
        return session

    def revoke_session(self, session_id: str) -> bool:
        """Revoke a session."""
        if session_id in self.sessions:
            self.sessions[session_id].status = SessionStatus.REVOKED
            self._audit("session_revoke", self.sessions[session_id].user,
                        "revoke", f"Session {session_id}")
            return True
        return False

    def get_user_sessions(self, user: str) -> List[Session]:
        return [s for s in self.sessions.values() if s.user == user]

    # ─── Network Segmentation ────────────────────────────────────────

    def add_segment(self, segment: NetworkSegment):
        self.network_segments.append(segment)

    def _get_segment(self, ip: str) -> Optional[NetworkSegment]:
        for seg in self.network_segments:
            if seg.contains_ip(ip):
                return seg
        return None

    def check_network_access(self, ip: str, service: str) -> Dict[str, Any]:
        """Check if an IP can access a service."""
        segment = self._get_segment(ip)
        if not segment:
            return {"allowed": False, "reason": "No segment found", "segment": None}

        allowed = segment.allows_service(service)
        return {
            "allowed": allowed,
            "reason": f"Service {'allowed' if allowed else 'blocked'} in {segment.zone}",
            "segment": segment.name,
            "zone": segment.zone,
        }

    # ─── Policy Engine ───────────────────────────────────────────────

    def add_policy(self, policy: Policy):
        self.policies.append(policy)

    def remove_policy(self, policy_id: str) -> bool:
        before = len(self.policies)
        self.policies = [p for p in self.policies if p.id != policy_id]
        return len(self.policies) < before

    def get_policies(self) -> List[Policy]:
        return sorted(self.policies, key=lambda p: p.priority, reverse=True)

    def block_ip(self, ip: str):
        if ip not in self.blocked_ips:
            self.blocked_ips.append(ip)
            self._audit("ip_block", "system", "block", f"IP {ip}")

    def unblock_ip(self, ip: str) -> bool:
        if ip in self.blocked_ips:
            self.blocked_ips.remove(ip)
            self._audit("ip_unblock", "system", "unblock", f"IP {ip}")
            return True
        return False

    # ─── Audit ───────────────────────────────────────────────────────

    def _audit(self, event: str, user: str, action: str, details_str: str,
               details: Optional[Dict] = None):
        """Log an audit entry."""
        entry = AuditLog(
            timestamp=datetime.now().isoformat(),
            event=event, user=user, action=action,
            result=action, details=details or {},
        )
        self.audit_log.append(entry)

    def get_audit_log(self, user: Optional[str] = None,
                     event: Optional[str] = None,
                     limit: int = 50) -> List[AuditLog]:
        """Query audit log."""
        logs = self.audit_log
        if user:
            logs = [l for l in logs if l.user == user]
        if event:
            logs = [l for l in logs if l.event == event]
        return logs[-limit:]

    # ─── Stats ───────────────────────────────────────────────────────

    def get_stats(self) -> Dict[str, Any]:
        """Get kit statistics."""
        active_sessions = sum(1 for s in self.sessions.values() if s.is_valid)
        active_devices = sum(1 for d in self.devices.values()
                            if d.status == DeviceStatus.REGISTERED)
        return {
            "policies": len(self.policies),
            "active_policies": sum(1 for p in self.policies if p.enabled),
            "devices": len(self.devices),
            "active_devices": active_devices,
            "sessions": len(self.sessions),
            "active_sessions": active_sessions,
            "blocked_ips": len(self.blocked_ips),
            "segments": len(self.network_segments),
            "audit_entries": len(self.audit_log),
        }

    def export_config(self) -> Dict[str, Any]:
        """Export full configuration."""
        return {
            "policies": [p.to_dict() for p in self.policies],
            "devices": [d.to_dict() for d in self.devices.values()],
            "segments": [s.to_dict() for s in self.network_segments],
            "blocked_ips": self.blocked_ips,
        }

    def __repr__(self) -> str:
        return (f"ZeroTrustKit(policies={len(self.policies)}, "
                f"devices={len(self.devices)}, sessions={len(self.sessions)})")
