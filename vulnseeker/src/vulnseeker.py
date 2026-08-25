"""
VulnSeeker — Smart CVE Search Engine with Risk Context

A Python library for searching, analyzing, and prioritizing CVE vulnerabilities.
Integrates with NVD API, ExploitDB, and EPSS for comprehensive risk analysis.

Usage:
    from vulnseeker import VulnSeeker

    vs = VulnSeeker()
    results = vs.search("apache log4j")
    for vuln in results:
        print(f"{vuln.id}: CVSS {vuln.cvss_score} — {vuln.severity}")
"""

import json
import re
import hashlib
import time
from pathlib import Path
from dataclasses import dataclass, field, asdict
from typing import Optional, List, Dict, Any, Tuple
from enum import Enum
from datetime import datetime, timedelta
from urllib.request import urlopen, Request
from urllib.parse import urlencode, quote
from urllib.error import HTTPError, URLError


class Severity(Enum):
    CRITICAL = "CRITICAL"
    HIGH = "HIGH"
    MEDIUM = "MEDIUM"
    LOW = "LOW"
    NONE = "NONE"


@dataclass
class CVE:
    """CVE vulnerability entry with full context."""
    id: str
    description: str
    cvss_score: float = 0.0
    cvss_vector: str = ""
    severity: str = "UNKNOWN"
    published: str = ""
    modified: str = ""
    cwe: List[str] = field(default_factory=list)
    affected_products: List[str] = field(default_factory=list)
    references: List[str] = field(default_factory=list)
    exploit_available: bool = False
    patch_available: bool = False
    in_kev: bool = False  # Known Exploited Vulnerabilities
    epss_score: float = 0.0  # Exploit Prediction Scoring System
    epss_percentile: float = 0.0
    source: str = "NVD"

    @property
    def is_critical(self) -> bool:
        return self.cvss_score >= 9.0

    @property
    def is_high(self) -> bool:
        return 7.0 <= self.cvss_score < 9.0

    @property
    def is_exploitable(self) -> bool:
        return self.exploit_available or self.in_kev

    @property
    def risk_level(self) -> str:
        if self.in_kev or self.exploit_available:
            return "CRITICAL"
        if self.cvss_score >= 9.0:
            return "CRITICAL"
        if self.cvss_score >= 7.0:
            return "HIGH"
        if self.cvss_score >= 4.0:
            return "MEDIUM"
        return "LOW"

    @property
    def age_days(self) -> int:
        if not self.published:
            return 0
        try:
            pub = datetime.strptime(self.published[:10], "%Y-%m-%d")
            return (datetime.now() - pub).days
        except ValueError:
            return 0

    def to_dict(self) -> Dict[str, Any]:
        d = asdict(self)
        d["is_critical"] = self.is_critical
        d["is_exploitable"] = self.is_exploitable
        d["risk_level"] = self.risk_level
        d["age_days"] = self.age_days
        return d

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), indent=2)


@dataclass
class RiskAnalysis:
    """Comprehensive risk analysis for a CVE."""
    cve_id: str
    cvss_score: float
    risk_level: str
    exploitability: str
    impact: str
    epss_risk: str
    recommendations: List[str]
    affected_versions: List[str] = field(default_factory=list)
    patch_versions: List[str] = field(default_factory=list)
    similar_cves: List[str] = field(default_factory=list)
    mitigation_steps: List[str] = field(default_factory=list)

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), indent=2)


@dataclass
class SearchResult:
    """Search results container."""
    query: str
    total_results: int
    cves: List[CVE]
    search_time: float = 0.0
    page: int = 1
    per_page: int = 20

    def to_dict(self) -> Dict[str, Any]:
        return {
            "query": self.query,
            "total_results": self.total_results,
            "returned": len(self.cves),
            "search_time": self.search_time,
            "cves": [c.to_dict() for c in self.cves],
        }


class VulnSeeker:
    """
    Smart CVE Search Engine.

    Searches NVD database, analyzes risk, and provides actionable intelligence.
    """

    NVD_API_BASE = "https://services.nvd.nist.gov/rest/json/cves/2.0"
    KEV_URL = "https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json"
    EPSS_URL = "https://api.first.org/data/v1/epss"

    def __init__(self, api_key: Optional[str] = None, cache_dir: Optional[str] = None,
                 use_cache: bool = True):
        """
        Initialize VulnSeeker.

        Args:
            api_key: NVD API key for higher rate limits (optional).
            cache_dir: Directory for caching API responses.
            use_cache: Whether to use caching.
        """
        self.api_key = api_key
        self.cache_dir = Path(cache_dir or "/tmp/vulnseeker_cache")
        self.use_cache = use_cache
        self.kev_data: Dict[str, bool] = {}
        self._loaded_kev = False

        if use_cache:
            self.cache_dir.mkdir(parents=True, exist_ok=True)

    # ─── Search API ──────────────────────────────────────────────────────

    def search(self, query: str, max_results: int = 20, min_cvss: float = 0.0,
               severity: Optional[str] = None, year: Optional[int] = None,
               has_exploit: bool = False) -> SearchResult:
        """
        Search CVEs by keyword.

        Args:
            query: Search query (product name, CVE ID, keyword).
            max_results: Maximum results to return.
            min_cvss: Minimum CVSS score filter.
            severity: Filter by severity (CRITICAL, HIGH, MEDIUM, LOW).
            year: Filter by publication year.
            has_exploit: Only show CVEs with known exploits.

        Returns:
            SearchResult with matching CVEs.
        """
        start_time = time.time()

        # Check if query is a CVE ID
        if re.match(r"CVE-\d{4}-\d{4,}", query, re.IGNORECASE):
            cve = self.get_cve(query.upper())
            if cve:
                return SearchResult(
                    query=query,
                    total_results=1,
                    cves=[cve],
                    search_time=time.time() - start_time,
                )

        # Build NVD API query
        params = {
            "keywordSearch": query,
            "resultsPerPage": min(max_results, 2000),
        }

        if min_cvss > 0:
            params["cvssV3Severity"] = severity or "HIGH"

        if year:
            start_date = f"{year}-01-01T00:00:00.000"
            end_date = f"{year}-12-31T23:59:59.999"
            params["pubStartDate"] = start_date
            params["pubEndDate"] = end_date

        # Make API request
        raw_results = self._nvd_request(params)

        # Parse results
        cves = []
        for item in raw_results.get("vulnerabilities", []):
            cve_data = item.get("cve", {})
            cve = self._parse_cve(cve_data)
            if cve:
                # Apply filters
                if min_cvss > 0 and cve.cvss_score < min_cvss:
                    continue
                if severity and cve.severity.upper() != severity.upper():
                    continue
                if has_exploit and not cve.exploit_available:
                    continue
                cves.append(cve)

        # Sort by CVSS score (highest first)
        cves.sort(key=lambda x: x.cvss_score, reverse=True)

        return SearchResult(
            query=query,
            total_results=raw_results.get("totalResults", len(cves)),
            cves=cves[:max_results],
            search_time=time.time() - start_time,
        )

    def get_cve(self, cve_id: str) -> Optional[CVE]:
        """
        Get detailed information for a specific CVE.

        Args:
            cve_id: CVE ID (e.g., "CVE-2021-44228").

        Returns:
            CVE object or None if not found.
        """
        params = {"cveId": cve_id}
        raw = self._nvd_request(params)
        vulns = raw.get("vulnerabilities", [])
        if vulns:
            return self._parse_cve(vulns[0].get("cve", {}))
        return None

    def search_by_product(self, product: str, version: Optional[str] = None,
                          max_results: int = 50) -> List[CVE]:
        """
        Search CVEs affecting a specific product.

        Args:
            product: Product name (e.g., "nginx", "apache").
            version: Specific version (optional).
            max_results: Maximum results.

        Returns:
            List of CVEs affecting the product.
        """
        query = product
        if version:
            query = f"{product} {version}"

        result = self.search(query, max_results=max_results)
        return result.cves

    def search_critical(self, max_results: int = 20) -> List[CVE]:
        """Search for critical CVEs (CVSS >= 9.0)."""
        result = self.search("*", max_results=max_results, min_cvss=9.0)
        return result.cves

    def search_recent(self, days: int = 30, max_results: int = 50) -> List[CVE]:
        """Search for recently published CVEs."""
        cutoff = datetime.now() - timedelta(days=days)
        params = {
            "pubStartDate": cutoff.strftime("%Y-%m-%dT00:00:00.000"),
            "pubEndDate": datetime.now().strftime("%Y-%m-%dT23:59:59.999"),
            "resultsPerPage": min(max_results, 2000),
        }
        raw = self._nvd_request(params)
        cves = []
        for item in raw.get("vulnerabilities", []):
            cve = self._parse_cve(item.get("cve", {}))
            if cve:
                cves.append(cve)
        cves.sort(key=lambda x: x.cvss_score, reverse=True)
        return cves[:max_results]

    def search_by_cwe(self, cwe_id: str, max_results: int = 50) -> List[CVE]:
        """Search CVEs by CWE ID (e.g., CWE-79)."""
        params = {
            "keywordSearch": cwe_id,
            "resultsPerPage": min(max_results, 2000),
        }
        raw = self._nvd_request(params)
        cves = []
        for item in raw.get("vulnerabilities", []):
            cve = self._parse_cve(item.get("cve", {}))
            if cve and cwe_id.upper() in [c.upper() for c in cve.cwe]:
                cves.append(cve)
        return cves[:max_results]

    # ─── Risk Analysis ───────────────────────────────────────────────────

    def analyze_risk(self, cve_id: str) -> Optional[RiskAnalysis]:
        """
        Perform comprehensive risk analysis for a CVE.

        Args:
            cve_id: CVE ID to analyze.

        Returns:
            RiskAnalysis with detailed risk assessment.
        """
        cve = self.get_cve(cve_id)
        if not cve:
            return None

        # Determine exploitability
        if cve.in_kev:
            exploitability = "ACTIVE EXPLOITATION — Patch immediately"
        elif cve.exploit_available:
            exploitability = "Public exploit available — High risk"
        elif cve.epss_score > 0.5:
            exploitability = f"High exploit probability (EPSS: {cve.epss_score:.0%})"
        elif cve.epss_score > 0.1:
            exploitability = f"Moderate exploit probability (EPSS: {cve.epss_score:.0%})"
        else:
            exploitability = "Low exploit probability"

        # Determine impact
        if cve.cvss_score >= 9.0:
            impact = "CRITICAL — Complete system compromise possible"
        elif cve.cvss_score >= 7.0:
            impact = "HIGH — Significant data loss or system damage"
        elif cve.cvss_score >= 4.0:
            impact = "MEDIUM — Limited impact, local access required"
        else:
            impact = "LOW — Minimal impact"

        # EPSS risk
        if cve.epss_score > 0.7:
            epss_risk = "VERY HIGH — Likely to be exploited in next 30 days"
        elif cve.epss_score > 0.3:
            epss_risk = "HIGH — Significant chance of exploitation"
        elif cve.epss_score > 0.1:
            epss_risk = "MODERATE — Possible exploitation"
        else:
            epss_risk = "LOW — Unlikely to be exploited soon"

        # Generate recommendations
        recommendations = self._generate_recommendations(cve)

        # Find similar CVEs
        similar = self._find_similar(cve)

        return RiskAnalysis(
            cve_id=cve.id,
            cvss_score=cve.cvss_score,
            risk_level=cve.risk_level,
            exploitability=exploitability,
            impact=impact,
            epss_risk=epss_risk,
            recommendations=recommendations,
            affected_versions=cve.affected_products[:5],
            similar_cves=[s.id for s in similar[:5]],
            mitigation_steps=self._generate_mitigations(cve),
        )

    # ─── Export ──────────────────────────────────────────────────────────

    def export(self, cves: List[CVE], output_file: str, format: str = "json") -> int:
        """
        Export CVEs to file.

        Args:
            cves: List of CVEs to export.
            output_file: Output file path.
            format: Export format (json, csv, markdown).

        Returns:
            Number of CVEs exported.
        """
        with open(output_file, "w") as f:
            if format == "json":
                data = {
                    "exported_at": datetime.now().isoformat(),
                    "count": len(cves),
                    "cves": [c.to_dict() for c in cves],
                }
                json.dump(data, f, indent=2)

            elif format == "csv":
                import csv
                writer = csv.writer(f)
                writer.writerow(["ID", "CVSS", "Severity", "Description", "Published", "Exploit", "KEV"])
                for c in cves:
                    writer.writerow([
                        c.id, c.cvss_score, c.severity,
                        c.description[:100], c.published,
                        c.exploit_available, c.in_kev
                    ])

            elif format == "markdown":
                f.write("# CVE Report\n\n")
                f.write(f"Generated: {datetime.now().isoformat()}\n\n")
                f.write(f"Total: {len(cves)} vulnerabilities\n\n")
                f.write("| ID | CVSS | Severity | Description | Exploit |\n")
                f.write("|-----|------|----------|-------------|--------|\n")
                for c in cves:
                    desc = c.description[:60] + "..." if len(c.description) > 60 else c.description
                    exploit = "🔴 YES" if c.exploit_available else "🟢 NO"
                    f.write(f"| {c.id} | {c.cvss_score} | {c.severity} | {desc} | {exploit} |\n")

        return len(cves)

    # ─── Statistics ──────────────────────────────────────────────────────

    def stats(self, cves: List[CVE]) -> Dict[str, Any]:
        """Get statistics for a list of CVEs."""
        if not cves:
            return {"total": 0}

        severities = {}
        for c in cves:
            sev = c.severity or "UNKNOWN"
            severities[sev] = severities.get(sev, 0) + 1

        return {
            "total": len(cves),
            "severities": severities,
            "avg_cvss": sum(c.cvss_score for c in cves) / len(cves),
            "max_cvss": max(c.cvss_score for c in cves),
            "with_exploits": sum(1 for c in cves if c.exploit_available),
            "in_kev": sum(1 for c in cves if c.in_kev),
            "avg_age_days": sum(c.age_days for c in cves) / len(cves),
        }

    # ─── Internal Methods ────────────────────────────────────────────────

    def _nvd_request(self, params: Dict[str, Any]) -> Dict[str, Any]:
        """Make request to NVD API."""
        cache_key = hashlib.md5(json.dumps(params, sort_keys=True).encode()).hexdigest()
        cache_file = self.cache_dir / f"{cache_key}.json"

        # Check cache
        if self.use_cache and cache_file.exists():
            age = time.time() - cache_file.stat().st_mtime
            if age < 3600:  # Cache for 1 hour
                with open(cache_file) as f:
                    return json.load(f)

        # Make API request
        url = f"{self.NVD_API_BASE}?{urlencode(params)}"
        headers = {"User-Agent": "VulnSeeker/2.0"}
        if self.api_key:
            headers["apiKey"] = self.api_key

        try:
            req = Request(url, headers=headers)
            with urlopen(req, timeout=30) as response:
                data = json.loads(response.read().decode())

            # Cache response
            if self.use_cache:
                with open(cache_file, "w") as f:
                    json.dump(data, f)

            return data

        except HTTPError as e:
            if e.code == 403:
                return {"vulnerabilities": [], "totalResults": 0}
            raise
        except URLError:
            return {"vulnerabilities": [], "totalResults": 0}

    def _parse_cve(self, cve_data: Dict[str, Any]) -> Optional[CVE]:
        """Parse NVD CVE data into CVE object."""
        try:
            cve_id = cve_data.get("id", "")

            # Get description
            descriptions = cve_data.get("descriptions", [])
            description = ""
            for desc in descriptions:
                if desc.get("lang") == "en":
                    description = desc.get("value", "")
                    break
            if not description and descriptions:
                description = descriptions[0].get("value", "")

            # Get CVSS score
            cvss_score = 0.0
            cvss_vector = ""
            severity = "UNKNOWN"

            metrics = cve_data.get("metrics", {})
            # Try CVSS v3.1 first
            for metric in metrics.get("cvssMetricV31", []):
                cvss_data = metric.get("cvssData", {})
                cvss_score = cvss_data.get("baseScore", 0.0)
                cvss_vector = cvss_data.get("vectorString", "")
                severity = cvss_data.get("baseSeverity", "UNKNOWN")
                break

            # Fallback to CVSS v3.0
            if cvss_score == 0:
                for metric in metrics.get("cvssMetricV30", []):
                    cvss_data = metric.get("cvssData", {})
                    cvss_score = cvss_data.get("baseScore", 0.0)
                    cvss_vector = cvss_data.get("vectorString", "")
                    severity = cvss_data.get("baseSeverity", "UNKNOWN")
                    break

            # Fallback to CVSS v2
            if cvss_score == 0:
                for metric in metrics.get("cvssMetricV2", []):
                    cvss_data = metric.get("cvssData", {})
                    cvss_score = cvss_data.get("baseScore", 0.0)
                    cvss_vector = cvss_data.get("vectorString", "")
                    severity = "HIGH" if cvss_score >= 7 else "MEDIUM" if cvss_score >= 4 else "LOW"
                    break

            # Get CWEs
            cwe_list = []
            weaknesses = cve_data.get("weaknesses", [])
            for weakness in weaknesses:
                for desc in weakness.get("description", []):
                    cwe_id = desc.get("value", "")
                    if cwe_id.startswith("CWE-"):
                        cwe_list.append(cwe_id)

            # Get references
            references = []
            for ref in cve_data.get("references", []):
                references.append(ref.get("url", ""))

            # Get published/modified dates
            published = cve_data.get("published", "")
            modified = cve_data.get("lastModified", "")

            # Check for exploits in references
            exploit_available = any(
                "exploit" in ref.get("tags", []) or "Exploit" in ref.get("url", "")
                for ref in cve_data.get("references", [])
            )

            return CVE(
                id=cve_id,
                description=description,
                cvss_score=cvss_score,
                cvss_vector=cvss_vector,
                severity=severity.upper() if severity else "UNKNOWN",
                published=published,
                modified=modified,
                cwe=cwe_list,
                references=references,
                exploit_available=exploit_available,
                in_kev=self._check_kev(cve_id),
            )

        except Exception:
            return None

    def _check_kev(self, cve_id: str) -> bool:
        """Check if CVE is in CISA KEV."""
        if not self._loaded_kev:
            self._load_kev()
        return self.kev_data.get(cve_id, False)

    def _load_kev(self):
        """Load CISA Known Exploited Vulnerabilities."""
        cache_file = self.cache_dir / "kev.json"

        if self.use_cache and cache_file.exists():
            age = time.time() - cache_file.stat().st_mtime
            if age < 86400:  # Cache for 24 hours
                with open(cache_file) as f:
                    self.kev_data = json.load(f)
                self._loaded_kev = True
                return

        try:
            req = Request(self.KEV_URL, headers={"User-Agent": "VulnSeeker/2.0"})
            with urlopen(req, timeout=30) as response:
                data = json.loads(response.read().decode())

            for vuln in data.get("vulnerabilities", []):
                self.kev_data[vuln.get("cveID", "")] = True

            if self.use_cache:
                with open(cache_file, "w") as f:
                    json.dump(self.kev_data, f)

        except Exception:
            pass

        self._loaded_kev = True

    def _generate_recommendations(self, cve: CVE) -> List[str]:
        """Generate security recommendations for a CVE."""
        recs = []

        if cve.in_kev:
            recs.append("🚨 CRITICAL: This CVE is actively exploited in the wild")
            recs.append("Apply vendor patches immediately")
            recs.append("Consider isolating affected systems")

        if cve.exploit_available:
            recs.append("⚠️ Public exploit exists — prioritize patching")
            recs.append("Deploy WAF rules if applicable")

        if cve.cvss_score >= 9.0:
            recs.append("Critical CVSS score — emergency patching recommended")
            recs.append("Enable enhanced monitoring for affected systems")

        if cve.epss_score > 0.5:
            recs.append(f"High exploit probability ({cve.epss_score:.0%}) — act quickly")

        if not cve.patch_available:
            recs.append("No official patch available — apply mitigations")
            recs.append("Monitor vendor advisories for updates")

        if "CWE-79" in cve.cwe:
            recs.append("XSS vulnerability — validate and sanitize all user input")
        elif "CWE-89" in cve.cwe:
            recs.append("SQL injection — use parameterized queries")
        elif "CWE-22" in cve.cwe:
            recs.append("Path traversal — validate file paths")
        elif "CWE-416" in cve.cwe:
            recs.append("Use-after-free — update affected software")

        if not recs:
            recs.append("Monitor for updates and apply patches when available")

        return recs

    def _generate_mitigations(self, cve: CVE) -> List[str]:
        """Generate mitigation steps."""
        mitigations = []

        if cve.in_kev:
            mitigations.append("Block known IOCs at network perimeter")
            mitigations.append("Enable threat hunting for related indicators")

        if cve.cvss_score >= 7.0:
            mitigations.append("Implement network segmentation")
            mitigations.append("Enable intrusion detection/prevention")

        if "network" in cve.cvss_vector.lower():
            mitigations.append("Restrict network access to affected services")

        if "local" in cve.cvss_vector.lower():
            mitigations.append("Limit local user privileges")

        mitigations.append("Monitor logs for exploitation attempts")
        mitigations.append("Keep software updated")

        return mitigations

    def _find_similar(self, cve: CVE, max_results: int = 5) -> List[CVE]:
        """Find similar CVEs based on CWE and product."""
        if not cve.cwe:
            return []

        similar = []
        for cwe in cve.cwe[:2]:
            results = self.search(cwe, max_results=3)
            for r in results.cves:
                if r.id != cve.id and r.id not in [s.id for s in similar]:
                    similar.append(r)

        return similar[:max_results]


# Alias for backward compatibility
VulnSearch = VulnSeeker
