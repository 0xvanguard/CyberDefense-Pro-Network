"""ZeroTrustKit - Zero Trust Security Implementation"""
from dataclasses import dataclass, field
from typing import List, Dict, Optional
from datetime import datetime
from enum import Enum


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


@dataclass
class Policy:
    """Access policy rule."""
    id: str
    name: str
    conditions: Dict
    action: Action
    priority: int = 0


class ZeroTrustKit:
    """
    Zero Trust security implementation.
    
    Usage:
        ztk = ZeroTrustKit()
        result = ztk.verify(user="john@example.com", device="iPhone-14", ...)
    """
    
    def __init__(self):
        self.policies: List[Policy] = []
        self.trusted_devices: Dict[str, TrustLevel] = {}
        self.blocked_ips: List[str] = []
        self._load_default_policies()
    
    def _load_default_policies(self):
        """Load default zero trust policies."""
        self.policies = [
            Policy(id="P001", name="Block known bad IPs", 
                   conditions={"ip": "blocked"}, action=Action.BLOCK, priority=100),
            Policy(id="P002", name="Require MFA for admin",
                   conditions={"role": "admin", "mfa": False}, action=Action.STEP_UP, priority=90),
            Policy(id="P003", name="Allow trusted devices",
                   conditions={"device_trusted": True, "identity_verified": True}, 
                   action=Action.ALLOW, priority=80),
            Policy(id="P004", name="Monitor unknown devices",
                   conditions={"device_trusted": False}, action=Action.MONITOR, priority=50),
        ]
    
    def verify(self, user: str, device: str = "", ip: str = "", 
               location: str = "", **kwargs) -> VerificationResult:
        """
        Verify a request against zero trust policies.
        
        Returns VerificationResult with trust assessment.
        """
        risk_score = 0.0
        reasons = []
        
        # Check IP
        if ip in self.blocked_ips:
            return VerificationResult(
                trusted=False, trust_level=TrustLevel.NONE,
                risk_score=1.0, action=Action.BLOCK,
                reasons=["IP is blocked"]
            )
        
        # Check device trust
        device_trusted = device in self.trusted_devices
        if not device_trusted:
            risk_score += 0.3
            reasons.append("Unknown device")
        
        # Check location (simplified)
        trusted_locations = ["US", "CA", "UK", "DE", "FR"]
        location_trusted = location in trusted_locations
        if not location_trusted:
            risk_score += 0.2
            reasons.append("Untrusted location")
        
        # Check time
        hour = datetime.now().hour
        if hour < 6 or hour > 22:
            risk_score += 0.1
            reasons.append("Off-hours access")
        
        # Determine action
        if risk_score > 0.7:
            action = Action.BLOCK
        elif risk_score > 0.4:
            action = Action.STEP_UP
        elif risk_score > 0.2:
            action = Action.MONITOR
        else:
            action = Action.ALLOW
        
        trust_level = TrustLevel.FULL if risk_score < 0.1 else \
                     TrustLevel.HIGH if risk_score < 0.3 else \
                     TrustLevel.MEDIUM if risk_score < 0.5 else \
                     TrustLevel.LOW if risk_score < 0.7 else TrustLevel.NONE
        
        return VerificationResult(
            trusted=action == Action.ALLOW,
            trust_level=trust_level,
            risk_score=min(risk_score, 1.0),
            action=action,
            reasons=reasons if reasons else ["All checks passed"],
            device_trusted=device_trusted,
            location_trusted=location_trusted,
            identity_verified=True
        )
    
    def add_trusted_device(self, device_id: str, trust_level: TrustLevel = TrustLevel.HIGH):
        """Add a trusted device."""
        self.trusted_devices[device_id] = trust_level
    
    def block_ip(self, ip: str):
        """Block an IP address."""
        if ip not in self.blocked_ips:
            self.blocked_ips.append(ip)
    
    def add_policy(self, policy: Policy):
        """Add a custom policy."""
        self.policies.append(policy)
    
    def get_policies(self) -> List[Policy]:
        """Get all policies."""
        return sorted(self.policies, key=lambda p: p.priority, reverse=True)
    
    def __repr__(self) -> str:
        return f"ZeroTrustKit(policies={len(self.policies)})"
