"""Tests for ThreatMap"""

import os
import sys
import tempfile
import json

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.map import (
    ThreatType, ThreatSeverity, ThreatStatus, GeoLocation,
    ThreatFeed, Threat, ThreatStats, ThreatMap
)


def test_threat_type_enum():
    assert ThreatType.MALWARE.value == "malware"
    assert ThreatType.PHISHING.value == "phishing"
    assert ThreatType.RANSOMWARE.value == "ransomware"
    assert ThreatType.APT.value == "apt"
    print("✅ ThreatType enum OK")


def test_threat_severity_enum():
    assert ThreatSeverity.CRITICAL.value == "critical"
    assert ThreatSeverity.HIGH.value == "high"
    assert ThreatSeverity.MEDIUM.value == "medium"
    print("✅ ThreatSeverity enum OK")


def test_geolocation_creation():
    geo = GeoLocation(
        country="United States",
        country_code="US",
        region="north_america",
        city="New York",
        latitude=40.7128,
        longitude=-74.0060,
        asn="AS15169",
        org="Google LLC"
    )
    assert geo.country_code == "US"
    assert geo.org == "Google LLC"
    assert geo.region == "north_america"
    print("✅ GeoLocation creation OK")


def test_geolocation_to_dict():
    geo = GeoLocation(
        country="Australia",
        country_code="AU",
        region="oceania",
        city="Sydney",
        latitude=-33.8688,
        longitude=151.2093,
    )
    d = geo.to_dict()
    assert d["country_code"] == "AU"
    assert d["region"] == "oceania"
    print("✅ GeoLocation to_dict OK")


def test_threat_feed_creation():
    feed = ThreatFeed(
        name="Abuse.ch Malware",
        url="https://urlhaus.abuse.ch/downloads/json/",
        feed_type="malware",
        update_frequency="realtime",
        reliability=5
    )
    assert feed.name == "Abuse.ch Malware"
    assert feed.reliability == 5
    assert feed.enabled is True
    print("✅ ThreatFeed creation OK")


def test_threat_feed_to_dict():
    feed = ThreatFeed(
        name="PhishTank",
        url="http://data.phishtank.com/data/online-valid.json",
        feed_type="phishing",
        update_frequency="hourly",
        reliability=4
    )
    d = feed.to_dict()
    assert d["feed_type"] == "phishing"
    print("✅ ThreatFeed to_dict OK")


def test_threat_creation():
    threat = Threat(
        id="THREAT-0001",
        threat_type="malware",
        severity="critical",
        title="Emotet Campaign",
        description="Emotet malware detected in US",
        source="Abuse.ch",
        timestamp="2024-12-15T10:30:00",
        confidence=0.92
    )
    assert threat.id == "THREAT-0001"
    assert threat.threat_type == "malware"
    assert threat.is_critical is True
    print("✅ Threat creation OK")


def test_threat_is_critical():
    t_crit = Threat(id="1", threat_type="c2", severity="critical",
                    title="C2", description="", source="", timestamp="2024-12-15T10:00:00")
    t_high = Threat(id="2", threat_type="phishing", severity="high",
                    title="Phish", description="", source="", timestamp="2024-12-15T10:00:00")
    assert t_crit.is_critical is True
    assert t_high.is_critical is False
    print("✅ Threat is_critical OK")


def test_threat_to_dict():
    threat = Threat(
        id="THREAT-0002",
        threat_type="ransomware",
        severity="high",
        title="LockBit Activity",
        description="Ransomware detected",
        source="VirusTotal",
        timestamp="2024-12-15T10:00:00",
        tags=["ransomware", "lockbit"]
    )
    d = threat.to_dict()
    assert d["id"] == "THREAT-0002"
    assert "ransomware" in d["tags"]
    assert "is_critical" in d
    print("✅ Threat to_dict OK")


def test_threat_map_init():
    tmap = ThreatMap(use_cache=False)
    assert len(tmap.threats) == 20
    assert len(tmap.FEEDS) > 0
    print("✅ ThreatMap init OK")


def test_threat_map_get_threats():
    tmap = ThreatMap(use_cache=False)
    threats = tmap.get_threats(hours=168)
    assert len(threats) == 20
    print("✅ ThreatMap get_threats OK")


def test_threat_map_filter_by_type():
    tmap = ThreatMap(use_cache=False)
    malware = tmap.get_threats(threat_type="malware", hours=168)
    phishing = tmap.get_threats(threat_type="phishing", hours=168)
    assert len(malware) > 0
    assert len(phishing) > 0
    assert all(t.threat_type == "malware" for t in malware)
    print("✅ ThreatMap filter by type OK")


def test_threat_map_filter_by_severity():
    tmap = ThreatMap(use_cache=False)
    critical = tmap.get_threats(severity="critical", hours=168)
    assert len(critical) > 0
    assert all(t.severity == "critical" for t in critical)
    print("✅ ThreatMap filter by severity OK")


def test_threat_map_get_stats():
    tmap = ThreatMap(use_cache=False)
    stats = tmap.get_stats(hours=168)
    assert stats.total_threats == 20
    assert "by_type" in stats.to_dict()
    assert "by_severity" in stats.to_dict()
    print("✅ ThreatMap get_stats OK")


def test_threat_map_get_threat_by_id():
    tmap = ThreatMap(use_cache=False)
    threat = tmap.get_threat("THREAT-0001")
    assert threat is not None
    assert threat.id == "THREAT-0001"
    none_threat = tmap.get_threat("NONEXISTENT")
    assert none_threat is None
    print("✅ ThreatMap get_threat OK")


def test_threat_map_export():
    tmap = ThreatMap(use_cache=False)
    with tempfile.NamedTemporaryFile(suffix=".json", delete=False) as f:
        path = f.name
    try:
        count = tmap.export(output_file=path, format="json")
        with open(path) as f:
            data = json.load(f)
        assert "threats" in data
        assert len(data["threats"]) == 20
    finally:
        os.unlink(path)
    print("✅ ThreatMap export OK")


if __name__ == "__main__":
    test_threat_type_enum()
    test_threat_severity_enum()
    test_geolocation_creation()
    test_geolocation_to_dict()
    test_threat_feed_creation()
    test_threat_feed_to_dict()
    test_threat_creation()
    test_threat_is_critical()
    test_threat_to_dict()
    test_threat_map_init()
    test_threat_map_get_threats()
    test_threat_map_filter_by_type()
    test_threat_map_filter_by_severity()
    test_threat_map_get_stats()
    test_threat_map_get_threat_by_id()
    test_threat_map_export()
    print("\n🎉 All 16 tests passed!")
