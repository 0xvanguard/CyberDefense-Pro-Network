"""
ThreatSim — Attack Scenario Generator

Creates realistic attack scenarios based on MITRE ATT&CK framework.
"""

import json
import random
import time
from typing import Dict, List, Optional
from dataclasses import dataclass, field
from enum import Enum


class Difficulty(Enum):
    BEGINNER = "beginner"
    INTERMEDIATE = "intermediate"
    ADVANCED = "advanced"
    EXPERT = "expert"


class KillChainPhase(Enum):
    RECONNAISSANCE = "reconnaissance"
    WEAPONIZATION = "weaponization"
    DELIVERY = "delivery"
    EXPLOITATION = "exploitation"
    INSTALLATION = "installation"
    COMMAND_CONTROL = "command_and_control"
    ACTIONS_ON_OBJECTIVES = "actions_on_objectives"


@dataclass
class AttackStep:
    """Single step in an attack scenario."""
    phase: KillChainPhase
    technique_id: str  # MITRE ATT&CK technique ID
    technique_name: str
    description: str
    tools: List[str] = field(default_factory=list)
    detection: str = ""
    mitigation: str = ""
    log_sources: List[str] = field(default_factory=list)


@dataclass
class Scenario:
    """Complete attack scenario."""
    name: str
    description: str
    difficulty: Difficulty
    threat_actor: str
    steps: List[AttackStep]
    objectives: List[str] = field(default_factory=list)
    duration_hours: int = 24
    tags: List[str] = field(default_factory=list)

    def to_dict(self) -> dict:
        return {
            "name": self.name,
            "description": self.description,
            "difficulty": self.difficulty.value,
            "threat_actor": self.threat_actor,
            "steps": [
                {
                    "phase": s.phase.value,
                    "technique_id": s.technique_id,
                    "technique_name": s.technique_name,
                    "description": s.description,
                    "tools": s.tools,
                    "detection": s.detection,
                    "mitigation": s.mitigation,
                    "log_sources": s.log_sources,
                }
                for s in self.steps
            ],
            "objectives": self.objectives,
            "duration_hours": self.duration_hours,
            "tags": self.tags,
        }

    def to_json(self, path: str = None) -> str:
        data = json.dumps(self.to_dict(), indent=2)
        if path:
            with open(path, "w") as f:
                f.write(data)
        return data

    def summary(self) -> str:
        """Human-readable summary."""
        lines = [
            f"# {self.name}",
            f"**Difficulty:** {self.difficulty.value}",
            f"**Threat Actor:** {self.threat_actor}",
            f"**Duration:** ~{self.duration_hours}h",
            f"**Steps:** {len(self.steps)}",
            "",
            "## Kill Chain",
        ]
        for i, step in enumerate(self.steps, 1):
            lines.append(f"### {i}. {step.technique_name} ({step.technique_id})")
            lines.append(f"- **Phase:** {step.phase.value}")
            lines.append(f"- {step.description}")
            if step.tools:
                lines.append(f"- **Tools:** {', '.join(step.tools)}")
            if step.detection:
                lines.append(f"- **Detection:** {step.detection}")
            lines.append("")

        return "\n".join(lines)


# MITRE ATT&CK Techniques Database
TECHNIQUES = {
    "reconnaissance": [
        {"id": "T1595", "name": "Active Scanning", "tools": ["nmap", "masscan"], "detection": "Network IDS alerts on port scans"},
        {"id": "T1592", "name": "Gather Victim Host Info", "tools": ["theHarvester", "Shodan"], "detection": "OSINT monitoring"},
        {"id": "T1589", "name": "Gather Victim Identity Info", "tools": ["LinkedIn", "Hunter.io"], "detection": "N/A"},
    ],
    "weaponization": [
        {"id": "T1587", "name": "Develop Capabilities", "tools": ["msfvenom", "Cobalt Strike"], "detection": "EDR behavioral analysis"},
        {"id": "T1584", "name": "Compromise Infrastructure", "tools": ["Bulletproof hosting"], "detection": "Threat intel feeds"},
    ],
    "delivery": [
        {"id": "1566", "name": "Phishing", "tools": ["GoPhish", "King Phisher"], "detection": "Email gateway, user reports"},
        {"id": "T1195", "name": "Supply Chain Compromise", "tools": ["Trojanized updates"], "detection": "Software integrity monitoring"},
        {"id": "T1190", "name": "Exploit Public-Facing App", "tools": ["SQLMap", "Burp Suite"], "detection": "WAF logs, web server logs"},
    ],
    "exploitation": [
        {"id": "T1190", "name": "Exploit Public-Facing App", "tools": ["Metasploit"], "detection": "IDS/IPS alerts"},
        {"id": "T1059", "name": "Command and Scripting Interpreter", "tools": ["PowerShell", "bash"], "detection": "Process monitoring"},
        {"id": "T1053", "name": "Scheduled Task/Job", "tools": ["cron", "schtasks"], "detection": "Task scheduler monitoring"},
    ],
    "installation": [
        {"id": "T1547", "name": "Boot or Logon Autostart Execution", "tools": ["Registry keys", "crontab"], "detection": "Registry monitoring"},
        {"id": "T1053", "name": "Scheduled Task/Job", "tools": ["at", "schtasks"], "detection": "Task scheduler logs"},
        {"id": "T1574", "name": "Hijack Execution Flow", "tools": ["DLL search order hijacking"], "detection": "File integrity monitoring"},
    ],
    "command_and_control": [
        {"id": "T1071", "name": "Application Layer Protocol", "tools": ["DNS tunneling", "HTTPS C2"], "detection": "Network traffic analysis"},
        {"id": "T1573", "name": "Encrypted Channel", "tools": ["Cobalt Strike", "Sliver"], "detection": "SSL inspection"},
        {"id": "T1090", "name": "Proxy", "tools": ["Domain fronting"], "detection": "CDN traffic analysis"},
    ],
    "actions_on_objectives": [
        {"id": "T1486", "name": "Data Encrypted for Impact", "tools": ["Ransomware"], "detection": "File entropy monitoring"},
        {"id": "T1041", "name": "Exfiltration Over C2 Channel", "tools": ["Cobalt Strike", "Sliver"], "detection": "DLP, network monitoring"},
        {"id": "T1485", "name": "Data Destruction", "tools": ["rm", "cipher"], "detection": "File system monitoring"},
    ],
}


class ScenarioGenerator:
    """
    Generate attack scenarios.

    Usage:
        gen = ScenarioGenerator()
        scenario = gen.generate("ransomware", difficulty=Difficulty.ADVANCED)
    """

    PRESET_SCENARIOS = {
        "ransomware": {
            "name": "Ransomware Attack — Double Extortion",
            "description": "Full ransomware attack chain from initial access through encryption and data exfiltration.",
            "threat_actor": "Scattered Spider / ALPHV",
            "objectives": ["Encrypt critical files", "Exfiltrate sensitive data", "Demand ransom payment"],
            "phases": ["reconnaissance", "delivery", "exploitation", "installation", "command_and_control", "actions_on_objectives"],
            "tags": ["ransomware", "double-extortion", "critical"],
        },
        "apt": {
            "name": "APT Campaign — Intellectual Property Theft",
            "description": "Advanced persistent threat campaign targeting trade secrets and research data.",
            "threat_actor": "APT29 (Cozy Bear)",
            "objectives": ["Gain persistent access", "Move laterally", "Exfiltrate IP"],
            "phases": ["reconnaissance", "weaponization", "delivery", "exploitation", "command_and_control", "actions_on_objectives"],
            "tags": ["apt", "espionage", "long-term"],
        },
        "insider": {
            "name": "Insider Threat — Data Exfiltration",
            "description": "Malicious insider using legitimate access to steal sensitive data.",
            "threat_actor": "Malicious Insider",
            "objectives": ["Exfiltrate customer data", "Cover tracks", "Bypass DLP"],
            "phases": ["reconnaissance", "actions_on_objectives"],
            "tags": ["insider", "data-theft", "detection"],
        },
        "supply-chain": {
            "name": "Supply Chain Attack — Trojanized Update",
            "description": "Compromise a software dependency to distribute malware to all users.",
            "threat_actor": "APT41 / Lazarus",
            "objectives": ["Compromise build pipeline", "Distribute trojanized package", "Maintain persistence"],
            "phases": ["reconnaissance", "weaponization", "delivery", "exploitation", "command_and_control"],
            "tags": ["supply-chain", "dependency", "npm", "pypi"],
        },
        "phishing": {
            "name": "Business Email Compromise (BEC)",
            "description": "Targeted phishing campaign to gain initial access and escalate privileges.",
            "threat_actor": "Scattered Spider",
            "objectives": ["Gain credentials", "Access email", "Wire fraud"],
            "phases": ["reconnaissance", "weaponization", "delivery", "exploitation", "actions_on_objectives"],
            "tags": ["phishing", "bec", "social-engineering"],
        },
    }

    def __init__(self):
        self.techniques = TECHNIQUES

    def generate(self, scenario_type: str = "ransomware",
                 difficulty: Difficulty = Difficulty.INTERMEDIATE) -> Scenario:
        """Generate a complete attack scenario."""
        preset = self.PRESET_SCENARIOS.get(scenario_type, self.PRESET_SCENARIOS["ransomware"])

        steps = []
        for phase_name in preset["phases"]:
            phase_techniques = self.techniques.get(phase_name, [])
            if phase_techniques:
                # Pick 1-2 techniques per phase based on difficulty
                num_techniques = {
                    Difficulty.BEGINNER: 1,
                    Difficulty.INTERMEDIATE: 1,
                    Difficulty.ADVANCED: 2,
                    Difficulty.EXPERT: 2,
                }.get(difficulty, 1)

                selected = random.sample(phase_techniques, min(num_techniques, len(phase_techniques)))
                for tech in selected:
                    steps.append(AttackStep(
                        phase=KillChainPhase(phase_name),
                        technique_id=tech["id"],
                        technique_name=tech["name"],
                        description=f"Adversary uses {tech['name']} technique during {phase_name} phase.",
                        tools=tech["tools"],
                        detection=tech["detection"],
                        log_sources=["system", "network"],
                    ))

        # Adjust duration based on difficulty
        duration = {
            Difficulty.BEGINNER: 2,
            Difficulty.INTERMEDIATE: 24,
            Difficulty.ADVANCED: 72,
            Difficulty.EXPERT: 168,
        }.get(difficulty, 24)

        return Scenario(
            name=preset["name"],
            description=preset["description"],
            difficulty=difficulty,
            threat_actor=preset["threat_actor"],
            steps=steps,
            objectives=preset["objectives"],
            duration_hours=duration,
            tags=preset["tags"],
        )

    def list_presets(self) -> List[str]:
        """List available scenario presets."""
        return list(self.PRESET_SCENARIOS.keys())
