"""ThreatMap - Real-time Threat Intelligence Map"""
from dataclasses import dataclass, field
from typing import List, Dict, Optional
from datetime import datetime
from enum import Enum


class ThreatType(Enum):
    MALWARE = "malware"
    RANSOMWARE = "ransomware"
    PHISHING = "phishing"
    DDoS = "ddos"
    DATA_BREACH = "data_breach"
    VULNERABILITY = "vulnerability"


@dataclass
class Threat:
    """Single threat entry."""
    id: str
    type: ThreatType
    name: str
    source_country: str
    target_country: str
    severity: str
    timestamp: str
    description: str
    iocs: List[str] = field(default_factory=list)
    mitigations: List[str] = field(default_factory=list)


@dataclass
class ThreatStats:
    """Threat statistics."""
    total_threats: int
    active_threats: int
    by_type: Dict[str, int]
    by_country: Dict[str, int]
    top_malware: List[str]
    top_targets: List[str]


class ThreatMap:
    """
    Real-time threat intelligence map.
    
    Usage:
        tm = ThreatMap()
        threats = tm.get_threats(region="latam")
        stats = tm.get_statistics()
    """
    
    def __init__(self):
        self.threats: List[Threat] = []
        self._load_sample_data()
    
    def _load_sample_data(self):
        """Load sample threat data."""
        self.threats = [
            Threat(
                id="THR-001", type=ThreatType.RANSOMWARE,
                name="LockBit 3.0", source_country="RU",
                target_country="US", severity="critical",
                timestamp="2024-01-15T10:30:00Z",
                description="Active ransomware campaign targeting healthcare",
                iocs=["lockbit3.onion", "185.100.87.20"],
                mitigations=["Patch SMB vulnerabilities", "Backup data offline"]
            ),
            Threat(
                id="THR-002", type=ThreatType.PHISHING,
                name="Microsoft 365 Phishing", source_country="CN",
                target_country="BR", severity="high",
                timestamp="2024-01-15T11:45:00Z",
                description="Credential harvesting campaign targeting LATAM",
                iocs=["micros0ft-login.com", "login-m365.xyz"],
                mitigations=["Enable MFA", "Train users on phishing"]
            ),
            Threat(
                id="THR-003", type=ThreatType.MALWARE,
                name="Emotet Botnet", source_country="RU",
                target_country="MX", severity="high",
                timestamp="2024-01-15T09:15:00Z",
                description="Banking trojan distributed via email",
                iocs=["emotet感染.com", "45.77.65.211"],
                mitigations=["Block known C2 IPs", "Update email filters"]
            ),
            Threat(
                id="THR-004", type=ThreatType.DDoS,
                name="Mirai Variant", source_country="KR",
                target_country="CL", severity="medium",
                timestamp="2024-01-15T08:00:00Z",
                description="IoT botnet DDoS attack on financial sector",
                iocs=["mirai-cnc.top", "192.168.1.100"],
                mitigations=["Secure IoT devices", "Implement rate limiting"]
            ),
            Threat(
                id="THR-005", type=ThreatType.VULNERABILITY,
                name="Citrix Bleed", source_country="US",
                target_country="AR", severity="critical",
                timestamp="2024-01-15T12:00:00Z",
                description="Critical vulnerability in Citrix NetScaler",
                iocs=["CVE-2023-4966"],
                mitigations=["Patch immediately", "Reset session tokens"]
            )
        ]
    
    def get_threats(self, region: str = None, 
                    threat_type: str = None,
                    severity: str = None) -> List[Threat]:
        """Get filtered threats."""
        threats = self.threats.copy()
        
        if region:
            region_map = {
                "latam": ["BR", "MX", "AR", "CL", "CO", "PE"],
                "north_america": ["US", "CA"],
                "europe": ["UK", "DE", "FR"],
                "asia": ["CN", "JP", "KR"]
            }
            countries = region_map.get(region.lower(), [region.upper()])
            threats = [t for t in threats if t.target_country in countries]
        
        if threat_type:
            threats = [t for t in threats if t.type.value == threat_type]
        
        if severity:
            threats = [t for t in threats if t.severity == severity]
        
        return threats
    
    def get_statistics(self) -> ThreatStats:
        """Get threat statistics."""
        by_type = {}
        by_country = {}
        
        for t in self.threats:
            by_type[t.type.value] = by_type.get(t.type.value, 0) + 1
            by_country[t.target_country] = by_country.get(t.target_country, 0) + 1
        
        return ThreatStats(
            total_threats=len(self.threats),
            active_threats=len([t for t in self.threats if t.severity in ["high", "critical"]]),
            by_type=by_type,
            by_country=by_country,
            top_malware=["LockBit 3.0", "Emotet", "Mirai"],
            top_targets=["US", "BR", "MX"]
        )
    
    def generate_report(self, output_file: str):
        """Generate HTML threat report."""
        stats = self.get_statistics()
        
        html = f"""<!DOCTYPE html>
<html><head><title>Threat Map Report</title>
<style>
body {{ font-family: sans-serif; max-width: 800px; margin: 40px auto; }}
h1 {{ color: #ef4444; }}
.stat {{ display: inline-block; margin: 10px; padding: 20px; background: #f5f5f5; border-radius: 8px; }}
.threat {{ border-left: 4px solid #ef4444; padding: 10px; margin: 10px 0; }}
</style></head><body>
<h1>🗺️ Threat Map Report</h1>
<div class="stat"><h3>{stats.total_threats}</h3><p>Total Threats</p></div>
<div class="stat"><h3>{stats.active_threats}</h3><p>Active (High/Critical)</p></div>
<h2>By Type</h2>
{''.join(f"<p>{k}: {v}</p>" for k,v in stats.by_type.items())}
<h2>Recent Threats</h2>
{''.join(f"<div class='threat'><b>{t.name}</b> ({t.severity})<br>{t.description}</div>" for t in self.threats)}
</body></html>"""
        
        with open(output_file, 'w') as f:
            f.write(html)
    
    def __len__(self) -> int:
        return len(self.threats)
    
    def __repr__(self) -> str:
        return f"ThreatMap(threats={len(self.threats)})"
