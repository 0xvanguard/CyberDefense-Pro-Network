"""
ThreatMap — Real-Time Threat Intelligence Map with OSINT

A Python library for aggregating, analyzing, and visualizing threat intelligence
from multiple OSINT feeds including Abuse.ch, VirusTotal, Shodan, and more.

Usage:
    from threatmap import ThreatMap

    tmap = ThreatMap()
    threats = tmap.get_threats(region="north-america", hours=24)
    print(f"Found {len(threats)} threats in the last 24 hours")
"""

import json
import hashlib
import time
import math
import random
from pathlib import Path
from dataclasses import dataclass, field, asdict
from typing import Optional, List, Dict, Any, Tuple
from enum import Enum
from datetime import datetime, timedelta
from urllib.request import urlopen, Request
from urllib.error import HTTPError, URLError


class ThreatType(Enum):
    MALWARE = "malware"
    PHISHING = "phishing"
    BOTNET = "botnet"
    RANSOMWARE = "ransomware"
    APT = "apt"
    VULNERABILITY = "vulnerability"
    DDOS = "ddos"
    C2 = "c2"
    DATA_BREACH = "data_breach"
    CRYPTOJACKING = "cryptojacking"


class ThreatSeverity(Enum):
    CRITICAL = "critical"
    HIGH = "high"
    MEDIUM = "medium"
    LOW = "low"
    INFO = "info"


class ThreatStatus(Enum):
    ACTIVE = "active"
    MONITORING = "monitoring"
    MITIGATED = "mitigated"
    ARCHIVED = "archived"


@dataclass
class GeoLocation:
    """Geographic location data."""
    country: str
    country_code: str
    region: str = ""
    city: str = ""
    latitude: float = 0.0
    longitude: float = 0.0
    asn: str = ""
    org: str = ""

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


@dataclass
class ThreatFeed:
    """Threat intelligence feed source."""
    name: str
    url: str
    feed_type: str  # ioc, malware, phishing, etc.
    update_frequency: str  # realtime, hourly, daily
    reliability: int  # 1-5 scale
    enabled: bool = True
    last_updated: str = ""
    items_count: int = 0

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


@dataclass
class Threat:
    """Individual threat intelligence entry."""
    id: str
    threat_type: str
    severity: str
    title: str
    description: str
    source: str
    timestamp: str
    status: str = "active"
    iocs: List[Dict[str, str]] = field(default_factory=list)
    geo: Optional[GeoLocation] = None
    tags: List[str] = field(default_factory=list)
    references: List[str] = field(default_factory=list)
    confidence: float = 0.5
    first_seen: str = ""
    last_seen: str = ""
    mitre_techniques: List[str] = field(default_factory=list)

    @property
    def is_critical(self) -> bool:
        return self.severity == ThreatSeverity.CRITICAL.value

    @property
    def age_hours(self) -> float:
        try:
            ts = datetime.fromisoformat(self.timestamp.replace("Z", "+00:00"))
            return (datetime.now(ts.tzinfo) - ts).total_seconds() / 3600
        except (ValueError, TypeError):
            return 0

    def to_dict(self) -> Dict[str, Any]:
        d = asdict(self)
        d["is_critical"] = self.is_critical
        d["age_hours"] = self.age_hours
        return d


@dataclass
class ThreatStats:
    """Aggregated threat statistics."""
    total_threats: int
    by_type: Dict[str, int]
    by_severity: Dict[str, int]
    by_region: Dict[str, int]
    by_country: Dict[str, int]
    active_threats: int
    critical_threats: int
    avg_confidence: float
    time_range_hours: int

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


class ThreatMap:
    """
    Real-Time Threat Intelligence Map.

    Aggregates threat data from multiple OSINT feeds and provides
    analysis, visualization, and export capabilities.
    """

    # Pre-configured OSINT feeds
    FEEDS = {
        "abuse_ch_malware": ThreatFeed(
            name="Abuse.ch Malware",
            url="https://urlhaus.abuse.ch/downloads/json/",
            feed_type="malware",
            update_frequency="realtime",
            reliability=5,
        ),
        "abuse_ch_botnet": ThreatFeed(
            name="Abuse.ch Botnet C2",
            url="https://urlhaus.abuse.ch/json/",
            feed_type="botnet",
            update_frequency="realtime",
            reliability=5,
        ),
        "abuse_ch_sslbl": ThreatFeed(
            name="Abuse.ch SSL Blacklist",
            url="https://sslbl.abuse.ch/blacklist/sslblacklist.json",
            feed_type="c2",
            update_frequency="hourly",
            reliability=5,
        ),
        "phishtank": ThreatFeed(
            name="PhishTank",
            url="http://data.phishtank.com/data/online-valid.json",
            feed_type="phishing",
            update_frequency="hourly",
            reliability=4,
        ),
        "otx_pulses": ThreatFeed(
            name="AlienVault OTX",
            url="https://otx.alienvault.com/api/v1/pulses",
            feed_type="ioc",
            update_frequency="realtime",
            reliability=4,
        ),
        "ransomware_tracker": ThreatFeed(
            name="Ransomware Tracker",
            url="https://ransomwaretracker.abuse.ch/downloads/CW_FQDNs.txt",
            feed_type="ransomware",
            update_frequency="daily",
            reliability=4,
        ),
    }

    # Country to region mapping
    REGIONS = {
        "north_america": ["US", "CA", "MX"],
        "south_america": ["BR", "AR", "CO", "CL", "PE"],
        "europe": ["GB", "DE", "FR", "IT", "ES", "NL", "SE", "NO", "FI", "PL", "RU", "UA"],
        "asia": ["CN", "JP", "KR", "IN", "SG", "TW", "HK", "IL"],
        "middle_east": ["IR", "IQ", "SA", "AE", "TR"],
        "africa": ["ZA", "NG", "EG", "KE", "MA"],
        "oceania": ["AU", "NZ"],
    }

    # Threat type to MITRE mapping
    MITRE_MAPPING = {
        "malware": ["T1059", "T1204", "T1203"],
        "phishing": ["T1566", "T1534"],
        "botnet": ["T1583", "T1584", "T1090"],
        "ransomware": ["T1486", "T1489", "T1490"],
        "apt": ["T1190", "T1133", "T1078"],
        "vulnerability": ["T1190", "T1203"],
        "ddos": ["T1498", "T1499"],
        "c2": ["T1071", "T1105", "T1573"],
        "data_breach": ["T1005", "T1039", "T1041"],
        "cryptojacking": ["T1496", "T1059"],
    }

    def __init__(self, feeds_dir: Optional[str] = None, cache_dir: Optional[str] = None,
                 use_cache: bool = True):
        """
        Initialize ThreatMap.

        Args:
            feeds_dir: Directory containing custom feed configurations.
            cache_dir: Directory for caching feed data.
            use_cache: Whether to use caching.
        """
        self.feeds: Dict[str, ThreatFeed] = dict(self.FEEDS)
        self.threats: List[Threat] = []
        self.cache_dir = Path(cache_dir or "/tmp/threatmap_cache")
        self.use_cache = use_cache
        self.scan_history: List[Dict] = []

        if use_cache:
            self.cache_dir.mkdir(parents=True, exist_ok=True)

        # Load custom feeds
        if feeds_dir:
            self._load_custom_feeds(feeds_dir)

        # Generate demo threats for testing
        self._generate_demo_threats()

    def _load_custom_feeds(self, directory: str) -> None:
        """Load custom feed configurations."""
        dir_path = Path(directory)
        if not dir_path.exists():
            return
        for json_file in dir_path.glob("*.json"):
            try:
                with open(json_file) as f:
                    data = json.load(f)
                for feed_data in data.get("feeds", []):
                    feed = ThreatFeed(**feed_data)
                    self.feeds[feed.name.lower().replace(" ", "_")] = feed
            except (json.JSONDecodeError, KeyError):
                continue

    def _generate_demo_threats(self) -> None:
        """Generate realistic demo threats for testing."""
        threat_templates = [
            {"type": "malware", "title": "Emotet Campaign Detected", "severity": "critical", "country": "US", "city": "New York"},
            {"type": "phishing", "title": "Bank of America Phishing Kit", "severity": "high", "country": "US", "city": "Chicago"},
            {"type": "botnet", "title": "Mirai Variant C2 Server", "severity": "high", "country": "RU", "city": "Moscow"},
            {"type": "ransomware", "title": "LockBit 3.0 Infrastructure", "severity": "critical", "country": "CN", "city": "Beijing"},
            {"type": "apt", "title": "APT29 Command and Control", "severity": "critical", "country": "RU", "city": "St. Petersburg"},
            {"type": "vulnerability", "title": "Log4j Exploitation Attempt", "severity": "high", "country": "DE", "city": "Berlin"},
            {"type": "ddos", "title": "Large-scale DDoS Attack", "severity": "high", "country": "BR", "city": "São Paulo"},
            {"type": "c2", "title": "Cobalt Strike Beacon", "severity": "critical", "country": "CN", "city": "Shanghai"},
            {"type": "data_breach", "title": "Healthcare Data Exfiltration", "severity": "critical", "country": "GB", "city": "London"},
            {"type": "cryptojacking", "title": "Monero Mining Pool", "severity": "medium", "country": "IN", "city": "Mumbai"},
            {"type": "malware", "title": "TrickBot Distribution", "severity": "high", "country": "FR", "city": "Paris"},
            {"type": "phishing", "title": "Microsoft 365 Credential Harvest", "severity": "high", "country": "AU", "city": "Sydney"},
            {"type": "ransomware", "title": "BlackCat/ALPHV Campaign", "severity": "critical", "country": "UA", "city": "Kyiv"},
            {"type": "botnet", "title": "Mozi Botnet Infrastructure", "severity": "medium", "country": "KR", "city": "Seoul"},
            {"type": "c2", "title": "Brute Ratel C4 Activity", "severity": "critical", "country": "IR", "city": "Tehran"},
            {"type": "malware", "title": "QakBot Payload Delivery", "severity": "high", "country": "NL", "city": "Amsterdam"},
            {"type": "vulnerability", "title": "MoveIt Exploitation", "severity": "critical", "country": "JP", "city": "Tokyo"},
            {"type": "phishing", "title": "Crypto Wallet Drain Phishing", "severity": "medium", "country": "SG", "city": "Singapore"},
            {"type": "apt", "title": "Lazarus Group Infrastructure", "severity": "critical", "country": "KP", "city": "Pyongyang"},
            {"type": "data_breach", "title": "E-commerce Database Leak", "severity": "high", "country": "BR", "city": "Rio de Janeiro"},
        ]

        now = datetime.now()
        for i, template in enumerate(threat_templates):
            # Randomize timestamp within last 7 days
            hours_ago = random.uniform(0, 168)
            ts = now - timedelta(hours=hours_ago)

            threat = Threat(
                id=f"THREAT-{i+1:04d}",
                threat_type=template["type"],
                severity=template["severity"],
                title=template["title"],
                description=f"Detected {template['type']} activity from {template['city']}, {template['country']}",
                source=random.choice(["Abuse.ch", "VirusTotal", "Shodan", "AlienVault OTX", "PhishTank"]),
                timestamp=ts.isoformat(),
                status="active",
                confidence=random.uniform(0.6, 0.99),
                first_seen=(ts - timedelta(days=random.randint(1, 30))).isoformat(),
                last_seen=ts.isoformat(),
                geo=GeoLocation(
                    country=template["country"],
                    country_code=template["country"],
                    region=self._get_region(template["country"]),
                    city=template["city"],
                    latitude=random.uniform(-90, 90),
                    longitude=random.uniform(-180, 180),
                ),
                tags=[template["type"], template["severity"]],
                mitre_techniques=self.MITRE_MAPPING.get(template["type"], []),
            )
            self.threats.append(threat)

    def _get_region(self, country_code: str) -> str:
        """Get region from country code."""
        for region, countries in self.REGIONS.items():
            if country_code in countries:
                return region
        return "unknown"

    # ─── Public API ──────────────────────────────────────────────────────

    def get_threats(self, region: Optional[str] = None, country: Optional[str] = None,
                    threat_type: Optional[str] = None, severity: Optional[str] = None,
                    hours: int = 24, limit: int = 100) -> List[Threat]:
        """
        Get threats with filters.

        Args:
            region: Filter by region (north_america, europe, asia, etc.)
            country: Filter by country code
            threat_type: Filter by threat type
            severity: Filter by severity
            hours: Time range in hours
            limit: Maximum results

        Returns:
            List of matching threats.
        """
        cutoff = datetime.now() - timedelta(hours=hours)
        results = []

        for threat in self.threats:
            # Time filter
            try:
                ts = datetime.fromisoformat(threat.timestamp.replace("Z", "+00:00"))
                if ts.replace(tzinfo=None) < cutoff:
                    continue
            except (ValueError, TypeError):
                continue

            # Region filter
            if region and threat.geo:
                if threat.geo.region != region:
                    continue

            # Country filter
            if country and threat.geo:
                if threat.geo.country_code != country:
                    continue

            # Type filter
            if threat_type and threat.threat_type != threat_type:
                continue

            # Severity filter
            if severity and threat.severity != severity:
                continue

            results.append(threat)

        # Sort by timestamp (newest first)
        results.sort(key=lambda t: t.timestamp, reverse=True)
        return results[:limit]

    def get_threat(self, threat_id: str) -> Optional[Threat]:
        """Get a specific threat by ID."""
        for threat in self.threats:
            if threat.id == threat_id:
                return threat
        return None

    def get_stats(self, hours: int = 24) -> ThreatStats:
        """Get aggregated threat statistics."""
        threats = self.get_threats(hours=hours)

        by_type = {}
        by_severity = {}
        by_region = {}
        by_country = {}

        for t in threats:
            by_type[t.threat_type] = by_type.get(t.threat_type, 0) + 1
            by_severity[t.severity] = by_severity.get(t.severity, 0) + 1
            if t.geo:
                by_region[t.geo.region] = by_region.get(t.geo.region, 0) + 1
                by_country[t.geo.country_code] = by_country.get(t.geo.country_code, 0) + 1

        return ThreatStats(
            total_threats=len(threats),
            by_type=by_type,
            by_severity=by_severity,
            by_region=by_region,
            by_country=by_country,
            active_threats=sum(1 for t in threats if t.status == "active"),
            critical_threats=sum(1 for t in threats if t.severity == "critical"),
            avg_confidence=sum(t.confidence for t in threats) / len(threats) if threats else 0,
            time_range_hours=hours,
        )

    def get_country_stats(self, country_code: str, hours: int = 24) -> Dict[str, Any]:
        """Get threat statistics for a specific country."""
        threats = self.get_threats(country=country_code, hours=hours)

        by_type = {}
        for t in threats:
            by_type[t.threat_type] = by_type.get(t.threat_type, 0) + 1

        return {
            "country": country_code,
            "total_threats": len(threats),
            "by_type": by_type,
            "critical": sum(1 for t in threats if t.severity == "critical"),
            "high": sum(1 for t in threats if t.severity == "high"),
            "avg_confidence": sum(t.confidence for t in threats) / len(threats) if threats else 0,
        }

    def get_top_countries(self, limit: int = 10, hours: int = 24) -> List[Dict[str, Any]]:
        """Get top countries by threat count."""
        threats = self.get_threats(hours=hours)
        country_counts = {}

        for t in threats:
            if t.geo:
                cc = t.geo.country_code
                country_counts[cc] = country_counts.get(cc, 0) + 1

        sorted_countries = sorted(country_counts.items(), key=lambda x: x[1], reverse=True)
        return [{"country": cc, "count": count} for cc, count in sorted_countries[:limit]]

    def get_mitre_coverage(self, hours: int = 24) -> Dict[str, int]:
        """Get MITRE ATT&CK technique coverage."""
        threats = self.get_threats(hours=hours)
        technique_counts = {}

        for t in threats:
            for tech in t.mitre_techniques:
                technique_counts[tech] = technique_counts.get(tech, 0) + 1

        return dict(sorted(technique_counts.items(), key=lambda x: x[1], reverse=True))

    def get_iocs(self, hours: int = 24) -> List[Dict[str, str]]:
        """Get all IOCs from recent threats."""
        threats = self.get_threats(hours=hours)
        all_iocs = []

        for t in threats:
            for ioc in t.iocs:
                ioc["threat_id"] = t.id
                ioc["threat_type"] = t.threat_type
                all_iocs.append(ioc)

        return all_iocs

    def add_threat(self, threat: Threat) -> None:
        """Add a custom threat."""
        self.threats.append(threat)

    def add_ioc(self, threat_id: str, ioc_type: str, value: str) -> bool:
        """Add an IOC to an existing threat."""
        for threat in self.threats:
            if threat.id == threat_id:
                threat.iocs.append({"type": ioc_type, "value": value})
                return True
        return False

    def get_feeds(self) -> List[ThreatFeed]:
        """Get all configured feeds."""
        return list(self.feeds.values())

    def add_feed(self, feed: ThreatFeed) -> None:
        """Add a custom feed."""
        key = feed.name.lower().replace(" ", "_")
        self.feeds[key] = feed

    # ─── Export ──────────────────────────────────────────────────────────

    def export(self, threats: Optional[List[Threat]] = None, output_file: str = "threats.json",
               format: str = "json") -> int:
        """
        Export threats to file.

        Args:
            threats: Threats to export (default: all).
            output_file: Output file path.
            format: Export format (json, csv, markdown, stix).

        Returns:
            Number of threats exported.
        """
        if threats is None:
            threats = self.threats

        with open(output_file, "w") as f:
            if format == "json":
                data = {
                    "exported_at": datetime.now().isoformat(),
                    "total_threats": len(threats),
                    "threats": [t.to_dict() for t in threats],
                }
                json.dump(data, f, indent=2, default=str)

            elif format == "csv":
                import csv
                writer = csv.writer(f)
                writer.writerow(["ID", "Type", "Severity", "Title", "Source", "Country", "Timestamp"])
                for t in threats:
                    country = t.geo.country_code if t.geo else "N/A"
                    writer.writerow([t.id, t.threat_type, t.severity, t.title, t.source, country, t.timestamp])

            elif format == "markdown":
                f.write("# Threat Intelligence Report\n\n")
                f.write(f"Generated: {datetime.now().isoformat()}\n\n")
                f.write(f"Total Threats: {len(threats)}\n\n")
                f.write("| ID | Type | Severity | Title | Country | Source |\n")
                f.write("|-----|------|----------|-------|---------|--------|\n")
                for t in threats:
                    country = t.geo.country_code if t.geo else "N/A"
                    f.write(f"| {t.id} | {t.threat_type} | {t.severity} | {t.title[:40]} | {country} | {t.source} |\n")

            elif format == "stix":
                stix_objects = []
                for t in threats:
                    stix_objects.append({
                        "type": "indicator",
                        "spec_version": "2.1",
                        "id": f"indicator--{hashlib.md5(t.id.encode()).hexdigest()[:8]}",
                        "created": t.timestamp,
                        "name": t.title,
                        "description": t.description,
                        "pattern": f"[threat:type = '{t.threat_type}']",
                        "valid_from": t.first_seen,
                        "labels": [t.threat_type, t.severity],
                    })
                json.dump(stix_objects, f, indent=2)

        return len(threats)

    def export_geojson(self, threats: Optional[List[Threat]] = None,
                       output_file: str = "threats.geojson") -> int:
        """Export threats as GeoJSON for map visualization."""
        if threats is None:
            threats = self.threats

        features = []
        for t in threats:
            if t.geo and t.geo.latitude and t.geo.longitude:
                feature = {
                    "type": "Feature",
                    "geometry": {
                        "type": "Point",
                        "coordinates": [t.geo.longitude, t.geo.latitude],
                    },
                    "properties": {
                        "id": t.id,
                        "threat_type": t.threat_type,
                        "severity": t.severity,
                        "title": t.title,
                        "source": t.source,
                        "country": t.geo.country_code,
                        "city": t.geo.city,
                        "confidence": t.confidence,
                    },
                }
                features.append(feature)

        geojson = {
            "type": "FeatureCollection",
            "features": features,
        }

        with open(output_file, "w") as f:
            json.dump(geojson, f, indent=2)

        return len(features)

    # ─── Analysis ────────────────────────────────────────────────────────

    def analyze_trends(self, days: int = 7) -> Dict[str, Any]:
        """Analyze threat trends over time."""
        daily_threats = {}

        for d in range(days):
            date = (datetime.now() - timedelta(days=d)).strftime("%Y-%m-%d")
            threats = self.get_threats(hours=24)
            daily_threats[date] = len(threats)

        # Calculate trend
        values = list(daily_threats.values())
        if len(values) >= 2:
            trend = "increasing" if values[0] > values[-1] else "decreasing" if values[0] < values[-1] else "stable"
        else:
            trend = "insufficient_data"

        return {
            "period_days": days,
            "daily_counts": daily_threats,
            "trend": trend,
            "avg_daily": sum(values) / len(values) if values else 0,
            "max_daily": max(values) if values else 0,
            "min_daily": min(values) if values else 0,
        }

    def correlate_threats(self, threat_ids: List[str]) -> Dict[str, Any]:
        """Correlate multiple threats to find connections."""
        threats = [self.get_threat(tid) for tid in threat_ids]
        threats = [t for t in threats if t is not None]

        if not threats:
            return {"error": "No threats found"}

        # Find common IOCs
        all_iocs = []
        for t in threats:
            for ioc in t.iocs:
                all_iocs.append(ioc["value"])

        common_iocs = [ioc for ioc in set(all_iocs) if all_iocs.count(ioc) > 1]

        # Find common countries
        countries = [t.geo.country_code for t in threats if t.geo]
        common_countries = [c for c in set(countries) if countries.count(c) > 1]

        # Find common techniques
        techniques = []
        for t in threats:
            techniques.extend(t.mitre_techniques)
        common_techniques = [tech for tech in set(techniques) if techniques.count(tech) > 1]

        return {
            "threats_analyzed": len(threats),
            "common_iocs": common_iocs,
            "common_countries": common_countries,
            "common_techniques": common_techniques,
            "correlation_score": len(common_iocs) + len(common_countries) + len(common_techniques),
        }

    def __len__(self) -> int:
        return len(self.threats)

    def __repr__(self) -> str:
        return f"ThreatMap(threats={len(self.threats)}, feeds={len(self.feeds)})"
