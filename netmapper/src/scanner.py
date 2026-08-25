"""
NetMapper — Network Scanner

Discovers hosts, ports, and services on a network.
"""

import socket
import ipaddress
import time
import json
from typing import Dict, List, Optional, Set
from dataclasses import dataclass, field, asdict
from enum import Enum


class PortState(Enum):
    OPEN = "open"
    CLOSED = "closed"
    FILTERED = "filtered"


@dataclass
class PortInfo:
    """Information about a scanned port."""
    port: int
    state: PortState
    service: str = ""
    version: str = ""
    banner: str = ""

    def to_dict(self) -> dict:
        return {
            "port": self.port,
            "state": self.state.value,
            "service": self.service,
            "version": self.version,
        }


@dataclass
class HostInfo:
    """Information about a discovered host."""
    ip: str
    hostname: str = ""
    mac: str = ""
    os_guess: str = ""
    is_up: bool = False
    ports: List[PortInfo] = field(default_factory=list)
    latency_ms: float = 0
    scan_time: float = field(default_factory=time.time)

    def to_dict(self) -> dict:
        return {
            "ip": self.ip,
            "hostname": self.hostname,
            "os_guess": self.os_guess,
            "is_up": self.is_up,
            "ports": [p.to_dict() for p in self.ports],
            "latency_ms": self.latency_ms,
        }


@dataclass
class NetworkTopology:
    """Complete network topology."""
    hosts: List[HostInfo] = field(default_factory=list)
    network_range: str = ""
    scan_start: float = 0
    scan_end: float = 0
    scan_duration: float = 0

    def to_dict(self) -> dict:
        return {
            "network_range": self.network_range,
            "total_hosts": len(self.hosts),
            "active_hosts": sum(1 for h in self.hosts if h.is_up),
            "scan_duration": f"{self.scan_duration:.2f}s",
            "hosts": [h.to_dict() for h in self.hosts],
        }

    def to_json(self, path: str = None) -> str:
        data = json.dumps(self.to_dict(), indent=2)
        if path:
            with open(path, "w") as f:
                f.write(data)
        return data


# Common port-to-service mappings
COMMON_PORTS = {
    21: "FTP", 22: "SSH", 23: "Telnet", 25: "SMTP",
    53: "DNS", 80: "HTTP", 110: "POP3", 111: "RPCBind",
    135: "MSRPC", 139: "NetBIOS", 143: "IMAP",
    443: "HTTPS", 445: "SMB", 993: "IMAPS", 995: "POP3S",
    1433: "MSSQL", 1521: "Oracle", 3306: "MySQL",
    3389: "RDP", 5432: "PostgreSQL", 5900: "VNC",
    6379: "Redis", 8080: "HTTP-Alt", 8443: "HTTPS-Alt",
    27017: "MongoDB",
}


class NetworkScanner:
    """
    Network scanner.

    Usage:
        scanner = NetworkScanner(target="192.168.1.0/24")
        topology = scanner.scan()
    """

    def __init__(self, target: str, ports: List[int] = None,
                 timeout: float = 1.0, max_threads: int = 100):
        self.target = target
        self.ports = ports or [22, 80, 443, 3389, 8080, 3306, 5432]
        self.timeout = timeout
        self.max_threads = max_threads

    def scan(self) -> NetworkTopology:
        """Perform network scan."""
        topology = NetworkTopology(network_range=self.target, scan_start=time.time())

        try:
            network = ipaddress.ip_network(self.target, strict=False)
            hosts = list(network.hosts())[:256]  # Limit to 256 hosts
        except ValueError:
            # Single IP
            hosts = [ipaddress.ip_address(self.target)]

        for ip in hosts:
            host = self._scan_host(str(ip))
            topology.hosts.append(host)

        topology.scan_end = time.time()
        topology.scan_duration = topology.scan_end - topology.scan_start
        return topology

    def _scan_host(self, ip: str) -> HostInfo:
        """Scan a single host."""
        host = HostInfo(ip=ip)

        # Ping check
        start = time.time()
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(self.timeout)
            result = sock.connect_ex((ip, 80))
            host.latency_ms = (time.time() - start) * 1000

            if result == 0:
                host.is_up = True
            else:
                # Try port 443
                try:
                    sock2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    sock2.settimeout(self.timeout)
                    result2 = sock2.connect_ex((ip, 443))
                    if result2 == 0:
                        host.is_up = True
                    sock2.close()
                except Exception:
                    pass

            sock.close()
        except Exception:
            host.latency_ms = (time.time() - start) * 1000

        # Port scan (only if host is up)
        if host.is_up:
            host.ports = self._scan_ports(ip)

            # Try hostname resolution
            try:
                host.hostname = socket.gethostbyaddr(ip)[0]
            except (socket.herror, socket.gaierror):
                pass

            # OS fingerprint (simplified)
            host.os_guess = self._guess_os(host.ports)

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
                    banner = self._grab_banner(sock)
                    ports.append(PortInfo(
                        port=port,
                        state=PortState.OPEN,
                        service=service,
                        banner=banner,
                    ))
                else:
                    ports.append(PortInfo(
                        port=port,
                        state=PortState.CLOSED,
                    ))

                sock.close()
            except Exception:
                ports.append(PortInfo(
                    port=port,
                    state=PortState.FILTERED,
                ))

        return ports

    def _grab_banner(self, sock: socket.socket) -> str:
        """Try to grab service banner."""
        try:
            sock.settimeout(1)
            sock.send(b"HEAD / HTTP/1.0\r\n\r\n")
            banner = sock.recv(1024).decode("utf-8", errors="ignore")
            return banner[:200]
        except Exception:
            return ""

    def _guess_os(self, ports: List[PortInfo]) -> str:
        """Guess OS based on open ports."""
        open_ports = {p.port for p in ports if p.state == PortState.OPEN}

        if 445 in open_ports or 139 in open_ports:
            return "Windows"
        elif 22 in open_ports and 80 in open_ports:
            return "Linux/Web Server"
        elif 22 in open_ports:
            return "Linux"
        elif 3389 in open_ports:
            return "Windows"
        elif 5900 in open_ports:
            return "macOS/Linux (VNC)"
        elif 3306 in open_ports or 5432 in open_ports:
            return "Database Server"
        else:
            return "Unknown"
