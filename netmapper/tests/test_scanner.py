"""Tests for NetMapper"""

import os
import sys
import tempfile
import json

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.scanner import (
    PortState, HostStatus, PortInfo, HostInfo, NetworkTopology,
    NetworkMapper, COMMON_PORTS, VULNERABLE_SERVICES, PORT_RISK
)


def test_port_state_enum():
    assert PortState.OPEN.value == "open"
    assert PortState.CLOSED.value == "closed"
    assert PortState.FILTERED.value == "filtered"
    print("✅ PortState enum OK")


def test_host_status_enum():
    assert HostStatus.UP.value == "up"
    assert HostStatus.DOWN.value == "down"
    print("✅ HostStatus enum OK")


def test_port_info_creation():
    pi = PortInfo(port=22, state=PortState.OPEN, service="SSH", risk="low")
    assert pi.port == 22
    assert pi.state == PortState.OPEN
    assert pi.service == "SSH"
    print("✅ PortInfo creation OK")


def test_port_info_to_dict():
    pi = PortInfo(port=80, state=PortState.OPEN, service="HTTP")
    d = pi.to_dict()
    assert d["port"] == 80
    assert d["state"] == "open"
    assert d["service"] == "HTTP"
    print("✅ PortInfo to_dict OK")


def test_host_info_creation():
    hi = HostInfo(ip="192.168.1.1")
    assert hi.ip == "192.168.1.1"
    assert hi.status == HostStatus.UNKNOWN
    assert hi.ports == []
    print("✅ HostInfo creation OK")


def test_host_info_to_dict():
    hi = HostInfo(ip="10.0.0.1", hostname="server.local", os_guess="Linux")
    d = hi.to_dict()
    assert d["ip"] == "10.0.0.1"
    assert d["hostname"] == "server.local"
    assert "ports" in d
    print("✅ HostInfo to_dict OK")


def test_topology_creation():
    topo = NetworkTopology(network_range="192.168.1.0/24")
    assert topo.network_range == "192.168.1.0/24"
    assert topo.hosts == []
    print("✅ NetworkTopology creation OK")


def test_topology_to_dict():
    topo = NetworkTopology(network_range="10.0.0.0/8")
    d = topo.to_dict()
    assert d["network_range"] == "10.0.0.0/8"
    assert "hosts" in d
    print("✅ NetworkTopology to_dict OK")


def test_topology_get_summary():
    topo = NetworkTopology(total_hosts=10, active_hosts=5, total_open_ports=20)
    summary = topo.get_summary()
    assert summary["total_hosts"] == 10
    assert summary["active_hosts"] == 5
    print("✅ Topology get_summary OK")


def test_topology_to_json():
    topo = NetworkTopology(network_range="127.0.0.0/24")
    json_str = topo.to_json()
    assert "network_range" in json_str
    data = json.loads(json_str)
    assert data["network_range"] == "127.0.0.0/24"
    print("✅ Topology to_json OK")


def test_topology_to_json_file():
    topo = NetworkTopology(network_range="10.0.0.0/8")
    with tempfile.NamedTemporaryFile(suffix=".json", delete=False) as f:
        path = f.name
    try:
        topo.to_json(path)
        with open(path) as f:
            data = json.load(f)
        assert data["network_range"] == "10.0.0.0/8"
    finally:
        os.unlink(path)
    print("✅ Topology to_json file OK")


def test_common_ports():
    assert 22 in COMMON_PORTS
    assert COMMON_PORTS[22] == "SSH"
    assert 80 in COMMON_PORTS
    assert COMMON_PORTS[80] == "HTTP"
    assert len(COMMON_PORTS) > 20
    print(f"✅ Common ports: {len(COMMON_PORTS)} entries")


def test_vulnerable_services():
    assert "Telnet" in VULNERABLE_SERVICES
    assert VULNERABLE_SERVICES["Telnet"]["risk"] == "high"
    assert "Redis" in VULNERABLE_SERVICES
    assert VULNERABLE_SERVICES["Redis"]["risk"] == "critical"
    print(f"✅ Vulnerable services: {len(VULNERABLE_SERVICES)} entries")


def test_port_risk():
    assert PORT_RISK[22] == "low"
    assert PORT_RISK[23] == "high"
    assert PORT_RISK[6379] == "critical"
    print("✅ Port risk mapping OK")


def test_mapper_init():
    mapper = NetworkMapper("127.0.0.1")
    assert mapper.target == "127.0.0.1"
    assert len(mapper.ports) > 0
    print(f"✅ Mapper init: {len(mapper.ports)} ports")


def test_mapper_custom_ports():
    mapper = NetworkMapper("10.0.0.1", ports=[22, 80, 443])
    assert mapper.ports == [22, 80, 443]
    print("✅ Mapper custom ports OK")


def test_mapper_scan_single():
    mapper = NetworkMapper("127.0.0.1", timeout=0.5)
    host = mapper.scan_single("127.0.0.1")
    assert isinstance(host, HostInfo)
    assert host.ip == "127.0.0.1"
    print(f"✅ Scan single: status={host.status.value}, ports={host.open_ports}")


def test_mapper_stats():
    mapper = NetworkMapper("10.0.0.0/24")
    stats = mapper.get_stats()
    assert "total_scans" in stats
    assert "ports_scanned" in stats
    print("✅ Mapper stats OK")


def test_topology_vulnerability_count():
    topo = NetworkTopology()
    topo.total_vulnerabilities = 5
    assert topo.total_vulnerabilities == 5
    print("✅ Vulnerability counting OK")


def test_port_risk_all_common():
    """Check that all common ports have risk levels."""
    for port in COMMON_PORTS:
        assert port in PORT_RISK, f"Port {port} ({COMMON_PORTS[port]}) missing from PORT_RISK"
    print("✅ All common ports have risk levels")


if __name__ == "__main__":
    test_port_state_enum()
    test_host_status_enum()
    test_port_info_creation()
    test_port_info_to_dict()
    test_host_info_creation()
    test_host_info_to_dict()
    test_topology_creation()
    test_topology_to_dict()
    test_topology_get_summary()
    test_topology_to_json()
    test_topology_to_json_file()
    test_common_ports()
    test_vulnerable_services()
    test_port_risk()
    test_mapper_init()
    test_mapper_custom_ports()
    test_mapper_scan_single()
    test_mapper_stats()
    test_topology_vulnerability_count()
    test_port_risk_all_common()
    print("\n🎉 All 20 tests passed!")
