"""Tests for VulnSeeker."""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from vulnseeker import VulnSeeker, CVE, RiskAnalysis


def test_cve_creation():
    """Test CVE dataclass creation."""
    cve = CVE(
        id="CVE-2021-44228",
        description="Apache Log4j2 Remote Code Execution",
        cvss_score=10.0,
        severity="CRITICAL",
        published="2021-12-10T00:00:00",
    )
    assert cve.id == "CVE-2021-44228"
    assert cve.cvss_score == 10.0
    assert cve.is_critical is True
    assert cve.risk_level == "CRITICAL"


def test_cve_properties():
    """Test CVE computed properties."""
    cve = CVE(id="CVE-2021-44228", description="Test", cvss_score=10.0, severity="CRITICAL")
    assert cve.is_critical is True
    assert cve.is_high is False

    cve2 = CVE(id="CVE-2021-99999", description="Test", cvss_score=7.5, severity="HIGH")
    assert cve2.is_critical is False
    assert cve2.is_high is True


def test_cve_exploitable():
    """Test CVE exploitability check."""
    cve1 = CVE(id="CVE-001", description="Test", exploit_available=True)
    assert cve1.is_exploitable is True

    cve2 = CVE(id="CVE-002", description="Test", in_kev=True)
    assert cve2.is_exploitable is True

    cve3 = CVE(id="CVE-003", description="Test")
    assert cve3.is_exploitable is False


def test_cve_to_dict():
    """Test CVE to_dict conversion."""
    cve = CVE(id="CVE-2021-44228", description="Test", cvss_score=10.0)
    d = cve.to_dict()
    assert isinstance(d, dict)
    assert d["id"] == "CVE-2021-44228"
    assert "is_critical" in d
    assert "risk_level" in d


def test_vulnseeker_init():
    """Test VulnSeeker initialization."""
    vs = VulnSeeker(use_cache=False)
    assert vs is not None
    assert vs.use_cache is False


def test_vulnseeker_search_mock():
    """Test search with mock data."""
    vs = VulnSeeker(use_cache=False)
    # Search should work even with API errors (returns empty)
    result = vs.search("nonexistent_product_xyz123", max_results=5)
    assert result is not None
    assert result.query == "nonexistent_product_xyz123"
    assert isinstance(result.cves, list)


def test_risk_analysis_generation():
    """Test risk analysis generation."""
    vs = VulnSeeker(use_cache=False)
    cve = CVE(
        id="CVE-2021-44228",
        description="Test RCE",
        cvss_score=10.0,
        severity="CRITICAL",
        in_kev=True,
        exploit_available=True,
        cwe=["CWE-502"],
    )
    recs = vs._generate_recommendations(cve)
    assert len(recs) > 0
    assert any("CRITICAL" in r for r in recs)

    mitigations = vs._generate_mitigations(cve)
    assert len(mitigations) > 0


def test_stats():
    """Test statistics calculation."""
    vs = VulnSeeker(use_cache=False)
    cves = [
        CVE(id="CVE-001", description="Test", cvss_score=10.0, severity="CRITICAL"),
        CVE(id="CVE-002", description="Test", cvss_score=7.5, severity="HIGH"),
        CVE(id="CVE-003", description="Test", cvss_score=5.0, severity="MEDIUM"),
    ]
    stats = vs.stats(cves)
    assert stats["total"] == 3
    assert stats["max_cvss"] == 10.0
    assert stats["avg_cvss"] == 7.5


def test_export_json():
    """Test JSON export."""
    import tempfile
    vs = VulnSeeker(use_cache=False)
    cves = [CVE(id="CVE-001", description="Test", cvss_score=10.0)]

    with tempfile.NamedTemporaryFile(suffix=".json", delete=False) as f:
        temp_path = f.name

    try:
        count = vs.export(cves, temp_path, "json")
        assert count == 1
        import json
        with open(temp_path) as f:
            data = json.load(f)
        assert data["count"] == 1
    finally:
        os.unlink(temp_path)


def test_export_csv():
    """Test CSV export."""
    import tempfile
    vs = VulnSeeker(use_cache=False)
    cves = [CVE(id="CVE-001", description="Test", cvss_score=10.0)]

    with tempfile.NamedTemporaryFile(suffix=".csv", delete=False) as f:
        temp_path = f.name

    try:
        count = vs.export(cves, temp_path, "csv")
        assert count == 1
    finally:
        os.unlink(temp_path)


def test_export_markdown():
    """Test Markdown export."""
    import tempfile
    vs = VulnSeeker(use_cache=False)
    cves = [CVE(id="CVE-001", description="Test", cvss_score=10.0)]

    with tempfile.NamedTemporaryFile(suffix=".md", delete=False) as f:
        temp_path = f.name

    try:
        count = vs.export(cves, temp_path, "markdown")
        assert count == 1
        with open(temp_path) as f:
            content = f.read()
        assert "CVE-001" in content
    finally:
        os.unlink(temp_path)


if __name__ == "__main__":
    test_cve_creation()
    test_cve_properties()
    test_cve_exploitable()
    test_cve_to_dict()
    test_vulnseeker_init()
    test_vulnseeker_search_mock()
    test_risk_analysis_generation()
    test_stats()
    test_export_json()
    test_export_csv()
    test_export_markdown()
    print("✅ All tests passed!")
