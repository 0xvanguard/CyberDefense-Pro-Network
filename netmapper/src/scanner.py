"""NetMapper — Network Scanner & Topology Mapper

Discovers hosts, ports, services, and vulnerabilities on a network.
Maps topology, detects OS, grabs banners, and checks for known issues.
"""

import socket
import ipaddress
import time
import json
from typing import Dict, List, Optional, Any
from dataclasses import dataclass, field, asdict
from enum import Enum


# ─── Enums ───────────────────────────────────────────────────────────

class PortState(Enum):
    OPEN = "open"
    CLOSED = "closed"
    FILTERED = "filtered"


class HostStatus(Enum):
    UP = "up"
    DOWN = "down"
    UNKNOWN = "unknown"


# ─── Data Models ─────────────────────────────────────────────────────

@dataclass
class PortInfo:
    """Information about a scanned port."""
    port: int
    state: PortState
    service: str = ""
    version: str = ""
    banner: str = ""
    risk: str = "low"  # low, medium, high, critical

    def to_dict(self) -> Dict[str, Any]:
        d = asdict(self)
        d["state"] = self.state.value
        return d


@dataclass
class HostInfo:
    """Information about a discovered host."""
    ip: str
    hostname: str = ""
    mac: str = ""
    os_guess: str = ""
    status: HostStatus = HostStatus.UNKNOWN
    ports: List[PortInfo] = field(default_factory=list)
    latency_ms: float = 0
    scan_time: float = field(default_factory=time.time)
    open_ports: int = 0
    services: List[str] = field(default_factory=list)
    vulnerabilities: List[Dict[str, str]] = field(default_factory=list)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "ip": self.ip,
            "hostname": self.hostname,
            "mac": self.mac,
            "os_guess": self.os_guess,
            "status": self.status.value,
            "ports": [p.to_dict() for p in self.ports],
            "open_ports": self.open_ports,
            "services": self.services,
            "vulnerabilities": self.vulnerabilities,
            "latency_ms": round(self.latency_ms, 2),
        }


@dataclass
class NetworkTopology:
    """Complete network topology."""
    hosts: List[HostInfo] = field(default_factory=list)
    network_range: str = ""
    scan_start: float = 0
    scan_end: float = 0
    scan_duration: float = 0
    total_hosts: int = 0
    active_hosts: int = 0
    total_open_ports: int = 0
    total_vulnerabilities: int = 0

    def to_dict(self) -> Dict[str, Any]:
        return {
            "network_range": self.network_range,
            "total_hosts": self.total_hosts,
            "active_hosts": self.active_hosts,
            "total_open_ports": self.total_open_ports,
            "total_vulnerabilities": self.total_vulnerabilities,
            "scan_duration": f"{self.scan_duration:.2f}s",
            "hosts": [h.to_dict() for h in self.hosts],
        }

    def to_json(self, path: Optional[str] = None) -> str:
        data = json.dumps(self.to_dict(), indent=2)
        if path:
            with open(path, "w") as f:
                f.write(data)
        return data

    def get_summary(self) -> Dict[str, Any]:
        """Get scan summary."""
        services = {}
        for h in self.hosts:
            for s in h.services:
                services[s] = services.get(s, 0) + 1

        os_guesses = {}
        for h in self.hosts:
            if h.os_guess and h.os_guess != "Unknown":
                os_guesses[h.os_guess] = os_guesses.get(h.os_guess, 0) + 1

        return {
            "total_hosts": self.total_hosts,
            "active_hosts": self.active_hosts,
            "total_open_ports": self.total_open_ports,
            "total_vulnerabilities": self.total_vulnerabilities,
            "top_services": sorted(services.items(), key=lambda x: x[1], reverse=True)[:10],
            "os_distribution": sorted(os_guesses.items(), key=lambda x: x[1], reverse=True),
            "scan_duration": f"{self.scan_duration:.2f}s",
        }


# ─── Port/Service Database ───────────────────────────────────────────

COMMON_PORTS = {
    20: "FTP-Data", 21: "FTP", 22: "SSH", 23: "Telnet", 25: "SMTP",
    53: "DNS", 80: "HTTP", 110: "POP3", 111: "RPCBind",
    135: "MSRPC", 139: "NetBIOS", 143: "IMAP",
    443: "HTTPS", 445: "SMB", 993: "IMAPS", 995: "POP3S",
    1433: "MSSQL", 1521: "Oracle", 3306: "MySQL",
    3389: "RDP", 5432: "PostgreSQL", 5900: "VNC",
    6379: "Redis", 8080: "HTTP-Alt", 8443: "HTTPS-Alt",
    27017: "MongoDB", 5601: "Kibana", 9200: "Elasticsearch",
    9090: "Prometheus", 1883: "MQTT", 6443: "Kubernetes",
}

# Known vulnerable service configurations
VULNERABLE_SERVICES = {
    "Telnet": {"risk": "high", "issue": "Telnet transmits data in cleartext"},
    "FTP": {"risk": "medium", "issue": "FTP transmits credentials in cleartext (use SFTP)"},
    "SMB": {"risk": "medium", "issue": "SMB may be vulnerable to EternalBlue if unpatched"},
    "RDP": {"risk": "medium", "issue": "RDP exposed — brute force risk"},
    "VNC": {"risk": "high", "issue": "VNC exposed — often unauthenticated"},
    "Redis": {"risk": "critical", "issue": "Redis exposed — may allow unauthorized access"},
    "MongoDB": {"risk": "critical", "issue": "MongoDB exposed — check authentication"},
    "MySQL": {"risk": "high", "issue": "MySQL exposed — brute force risk"},
    "PostgreSQL": {"risk": "high", "issue": "PostgreSQL exposed — brute force risk"},
    "MSSQL": {"risk": "high", "issue": "MSSQL exposed — brute force risk"},
    "Elasticsearch": {"risk": "critical", "issue": "Elasticsearch exposed — data leak risk"},
    "Kibana": {"risk": "high", "issue": "Kibana dashboard exposed"},
    "Prometheus": {"risk": "medium", "issue": "Prometheus metrics exposed"},
    "Kubernetes": {"risk": "critical", "issue": "K8s API exposed — cluster compromise risk"},
}

# Port risk assessment
PORT_RISK = {
    20: "low", 21: "medium", 22: "low", 23: "high", 25: "low",
    53: "low", 80: "low", 110: "medium", 111: "medium",
    135: "medium", 139: "medium", 143: "low",
    443: "low", 445: "medium", 993: "low", 995: "low",
    1433: "high", 1521: "high", 3306: "high", 3389: "medium",
    5432: "high", 5900: "high", 6379: "critical", 8080: "low",
    8443: "low", 5601: "high", 9200: "high",
    9090: "medium", 1883: "low", 6443: "critical",
    27017: "critical",
}


# ─── Network Mapper ──────────────────────────────────────────────────

class NetworkMapper:
    """
    Network scanner and topology mapper.

    Usage:
        mapper = NetworkMapper(target="192.168.1.0/24")
        topology = mapper.scan()
        summary = topology.get_summary()
    """

    def __init__(self, target: str, ports: Optional[List[int]] = None,
                 timeout: float = 1.0, max_threads: int = 100):
        self.target = target
        self.ports = ports or [21, 22, 23, 25, 53, 80, 110, 135, 139, 143,
                               443, 445, 993, 995, 1433, 1521, 3306, 3389,
                               5432, 5900, 6379, 8080, 8443, 27017]
        self.timeout = timeout
        self.max_threads = max_threads
        self.scan_count = 0

    def scan(self) -> NetworkTopology:
        """Perform full network scan."""
        topology = NetworkTopology(
            network_range=self.target, scan_start=time.time()
        )

        try:
            network = ipaddress.ip_network(self.target, strict=False)
            hosts = list(network.hosts())[:256]
        except ValueError:
            hosts = [ipaddress.ip_address(self.target)]

        topology.total_hosts = len(hosts)

        for ip in hosts:
            host = self._scan_host(str(ip))
            topology.hosts.append(host)
            if host.status == HostStatus.UP:
                topology.active_hosts += 1
                topology.total_open_ports += host.open_ports
                topology.total_vulnerabilities += len(host.vulnerabilities)

        topology.scan_end = time.time()
        topology.scan_duration = topology.scan_end - topology.scan_start
        self.scan_count += 1
        return topology

    def scan_single(self, ip: str) -> HostInfo:
        """Scan a single host."""
        return self._scan_host(ip)

    def _scan_host(self, ip: str) -> HostInfo:
        """Scan a single host."""
        host = HostInfo(ip=ip)

        # Ping check via multiple ports
        start = time.time()
        for probe_port in [80, 443, 22, 445]:
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(self.timeout)
                result = sock.connect_ex((ip, probe_port))
                host.latency_ms = (time.time() - start) * 1000
                if result == 0:
                    host.status = HostStatus.UP
                    sock.close()
                    break
                sock.close()
            except Exception:
                host.latency_ms = (time.time() - start) * 1000

        if host.status == HostStatus.UNKNOWN:
            host.status = HostStatus.DOWN

        # Port scan
        if host.status == HostStatus.UP:
            host.ports = self._scan_ports(ip)
            host.open_ports = sum(1 for p in host.ports if p.state == PortState.OPEN)
            host.services = [p.service for p in host.ports if p.state == PortState.OPEN and p.service]

            # Hostname resolution
            try:
                host.hostname = socket.gethostbyaddr(ip)[0]
            except (socket.herror, socket.gaierror):
                pass

            # OS detection
            host.os_guess = self._guess_os(host.ports)

            # Vulnerability check
            host.vulnerabilities = self._check_vulnerabilities(host.ports)

        return host

    def _scan_ports(self, ip: str) -> List[PortInfo]:
        """Scan ports on a host."""
        ports = []

        for port in self.ports:
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(self.timeout / 2)
                result = sock.connect_ex((ip, port))

                if result == 0:
                    service = COMMON_PORTS.get(port, "unknown")
                    risk = PORT_RISK.get(port, "low")
                    banner = self._grab_banner(sock, service)
                    ports.append(PortInfo(
                        port=port, state=PortState.OPEN,
                        service=service, banner=banner, risk=risk,
                    ))
                else:
                    ports.append(PortInfo(port=port, state=PortState.CLOSED))

                sock.close()
            except Exception:
                ports.append(PortInfo(port=port, state=PortState.FILTERED))

        return ports

    def _grab_banner(self, sock: socket.socket, service: str) -> str:
        """Try to grab service banner."""
        try:
            sock.settimeout(1)
            if service in ("HTTP", "HTTPS", "HTTP-Alt", "HTTPS-Alt"):
                sock.send(b"HEAD / HTTP/1.0\r\nHost: test\r\n\r\n")
            elif service == "SSH":
                pass  # SSH sends banner first
            elif service == "FTP":
                pass  # FTP sends banner first
            else:
                sock.send(b"\r\n")

            banner = sock.recv(1024).decode("utf-8", errors="ignore")
            return banner[:200].strip()
        except Exception:
            return ""

    def _guess_os(self, ports: List[PortInfo]) -> str:
        """Guess OS based on open ports."""
        open_ports = {p.port for p in ports if p.state == PortState.OPEN}

        if 445 in open_ports or 139 in open_ports:
            if 3389 in open_ports:
                return "Windows Server"
            return "Windows"
        elif 22 in open_ports and (80 in open_ports or 443 in open_ports):
            if 3306 in open_ports or 5432 in open_ports:
                return "Linux (Web + DB Server)"
            return "Linux (Web Server)"
        elif 22 in open_ports:
            return "Linux/macOS"
        elif 3389 in open_ports:
            return "Windows"
        elif 5900 in open_ports:
            return "macOS/Linux (VNC)"
        elif 3306 in open_ports or 5432 in open_ports or 1433 in open_ports:
            return "Database Server"
        elif 27017 in open_ports:
            return "MongoDB Server"
        elif 6379 in open_ports:
            return "Redis Server"
        else:
            return "Unknown"

    def _check_vulnerabilities(self, ports: List[PortInfo]) -> List[Dict[str, str]]:
        """Check for known vulnerable services."""
        vulns = []
        for port_info in ports:
            if port_info.state != PortState.OPEN:
                continue
            if port_info.service in VULNERABLE_SERVICES:
                vuln = VULNERABLE_SERVICES[port_info.service]
                vulns.append({
                    "port": port_info.port,
                    "service": port_info.service,
                    "risk": vuln["risk"],
                    "issue": vuln["issue"],
                })
        return vulns

    def get_stats(self) -> Dict[str, Any]:
        """Get mapper statistics."""
        return {
            "total_scans": self.scan_count,
            "target": self.target,
            "ports_scanned": len(self.ports),
            "timeout": self.timeout,
        }
