"""VulnSeeker - Smart CVE Search with Risk Context"""
import json
from dataclasses import dataclass, field
from typing import List, Dict, Optional
from pathlib import Path


@dataclass
class CVE:
    """CVE vulnerability entry."""
    id: str
    description: str
    cvss_score: float
    severity: str
    published: str
    modified: str
    cwe: List[str] = field(default_factory=list)
    affected_products: List[str] = field(default_factory=list)
    references: List[str] = field(default_factory=list)
    exploit_available: bool = False
    patch_available: bool = False
    in_kev: bool = False
    epss_score: float = 0.0
    
    @property
    def is_critical(self) -> bool:
        return self.cvss_score >= 9.0
    
    @property
    def is_exploitable(self) -> bool:
        return self.exploit_available or self.in_kev


@dataclass
class RiskAnalysis:
    """Risk analysis for a CVE."""
    cve_id: str
    risk_level: str
    risk_score: float
    exploitability: str
    impact: str
    recommendations: List[str]
    affected_versions: List[str] = field(default_factory=list)
    patch_versions: List[str] = field(default_factory=list)


class VulnSeeker:
    """
    Smart CVE search with exploitability context.
    
    Usage:
        vs = VulnSeeker()
        results = vs.search("log4j")
        cve = vs.get("CVE-2021-44228")
    """
    
    def __init__(self, data_dir: Optional[str] = None):
        self.data_dir = data_dir or str(Path(__file__).parent.parent / "data")
        self.cves: Dict[str, CVE] = {}
        self._load_sample_data()
    
    def _load_sample_data(self):
        """Load sample CVE data."""
        self.cves = {
            "CVE-2021-44228": CVE(
                id="CVE-2021-44228",
                description="Apache Log4j2 JNDI features do not protect against attacker controlled LDAP and other JNDI related endpoints.",
                cvss_score=10.0,
                severity="CRITICAL",
                published="2021-12-10",
                modified="2024-01-01",
                cwe=["CWE-502", "CWE-400"],
                affected_products=["Apache Log4j 2.0-beta9 to 2.14.1"],
                exploit_available=True,
                patch_available=True,
                in_kev=True,
                epss_score=0.97
            ),
            "CVE-2023-44228": CVE(
                id="CVE-2023-44228",
                description="Spring4Shell - Remote Code Execution via data binding.",
                cvss_score=9.8,
                severity="CRITICAL",
                published="2022-03-31",
                modified="2024-01-01",
                cwe=["CWE-94"],
                affected_products=["Spring Framework 5.3.0 to 5.3.17"],
                exploit_available=True,
                patch_available=True,
                in_kev=True,
                epss_score=0.85
            ),
            "CVE-2024-3094": CVE(
                id="CVE-2024-3094",
                description="XZ Utils backdoor - Malicious code in liblzma.",
                cvss_score=10.0,
                severity="CRITICAL",
                published="2024-03-29",
                modified="2024-04-01",
                cwe=["CWE-506"],
                affected_products=["XZ Utils 5.6.0 to 5.6.1"],
                exploit_available=True,
                patch_available=True,
                in_kev=True,
                epss_score=0.92
            )
        }
    
    def search(self, query: str, limit: int = 10) -> List[CVE]:
        """Search CVEs by keyword."""
        query_lower = query.lower()
        results = []
        for cve in self.cves.values():
            if (query_lower in cve.id.lower() or 
                query_lower in cve.description.lower() or
                any(query_lower in p.lower() for p in cve.affected_products)):
                results.append(cve)
        return results[:limit]
    
    def get(self, cve_id: str) -> Optional[CVE]:
        """Get specific CVE by ID."""
        return self.cves.get(cve_id)
    
    def get_critical(self, limit: int = 10) -> List[CVE]:
        """Get critical CVEs."""
        return sorted(
            [c for c in self.cves.values() if c.is_critical],
            key=lambda x: x.epss_score,
            reverse=True
        )[:limit]
    
    def get_exploitable(self, limit: int = 10) -> List[CVE]:
        """Get actively exploited CVEs."""
        return sorted(
            [c for c in self.cves.values() if c.is_exploitable],
            key=lambda x: x.epss_score,
            reverse=True
        )[:limit]
    
    def risk_analysis(self, cve_id: str) -> Optional[RiskAnalysis]:
        """Generate risk analysis for a CVE."""
        cve = self.get(cve_id)
        if not cve:
            return None
        
        risk_score = cve.cvss_score * cve.epss_score
        risk_level = "CRITICAL" if risk_score > 8 else "HIGH" if risk_score > 6 else "MEDIUM"
        
        return RiskAnalysis(
            cve_id=cve_id,
            risk_level=risk_level,
            risk_score=risk_score,
            exploitability="HIGH" if cve.exploit_available else "LOW",
            impact=cve.severity,
            recommendations=[
                f"Apply patch immediately" if cve.patch_available else "Monitor for patch",
                f"Check for exploit indicators" if cve.exploit_available else "No known exploits",
                f"Included in CISA KEV" if cve.in_kev else "Not in KEV"
            ]
        )
    
    def __len__(self) -> int:
        return len(self.cves)
    
    def __repr__(self) -> str:
        return f"VulnSeeker(cves={len(self.cves)})"
