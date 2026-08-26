"""ThreatSim — Synthetic Attack Scenario Generator"""
import random
import json
from dataclasses import dataclass, field
from typing import List, Dict, Optional, Any
from datetime import datetime, timedelta
from enum import Enum

class AttackVector(Enum):
    PHISHING = "phishing"
    RANSOMWARE = "ransomware"
    DDoS = "ddos"
    SQL_INJECTION = "sql_injection"
    XSS = "xss"
    INSIDER = "insider_threat"
    SUPPLY_CHAIN = "supply_chain"
    ZERO_DAY = "zero_day"

@dataclass
class Scenario:
    id: str
    name: str
    attack_vector: str
    description: str
    mitre_techniques: List[str]
    severity: str
    objectives: List[str]
    timeline_hours: int
    indicators: List[str]

@dataclass
class SimulationResult:
    scenario_id: str
    steps_executed: int
    detections: int
    total_steps: int
    detection_rate: float
    recommendations: List[str]

class ThreatSim:
    def __init__(self):
        self.scenarios: List[Scenario] = self._load_scenarios()
        self.simulation_history: List[SimulationResult] = []
        self.counter = 0

    def _load_scenarios(self) -> List[Scenario]:
        return [
            Scenario("SC-001", "Corporate Phishing Campaign", "phishing",
                "Targeted phishing attack using credential harvesting pages",
                ["T1566", "T1059", "T1078"], "high",
                ["Steal credentials", "Gain initial access", "Escalate privileges"], 72,
                ["Suspicious email", "Fake login page", "Credential exfil"]),
            Scenario("SC-002", "Ransomware Deployment", "ransomware",
                "Ransomware attack encrypting critical business data",
                ["T1486", "T1490", "T1489"], "critical",
                ["Encrypt files", "Demand ransom", "Exfiltrate data"], 48,
                ["Unusual file activity", "Mass encryption", "Ransom note"]),
            Scenario("SC-003", "DDoS Attack", "ddos",
                "Distributed denial of service against web infrastructure",
                ["T1498", "T1499"], "high",
                ["Overwhelm services", "Cause downtime", "Distraction for other attacks"], 6,
                ["Traffic spike", "Service degradation", "Multiple source IPs"]),
            Scenario("SC-004", "SQL Injection Exploitation", "sql_injection",
                "SQL injection to extract database contents",
                ["T1190", "T1005"], "critical",
                ["Bypass authentication", "Extract data", "Modify records"], 24,
                ["Error messages", "Unusual queries", "Data exfiltration"]),
            Scenario("SC-005", "Insider Threat", "insider_threat",
                "Malicious insider exfiltrating sensitive data",
                ["T1005", "T1041", "T1048"], "critical",
                ["Access sensitive data", "Exfiltrate via USB/cloud", "Cover tracks"], 168,
                ["Unusual access patterns", "Large downloads", "Off-hours activity"]),
            Scenario("SC-006", "Supply Chain Attack", "supply_chain",
                "Compromising a software dependency to backdoor applications",
                ["T1195", "T1059", "T1071"], "critical",
                ["Compromise dependency", "Inject backdoor", "Distribute to targets"], 720,
                ["Suspicious code changes", "Unsigned updates", "New network connections"]),
        ]

    def get_scenario(self, scenario_id: str) -> Optional[Scenario]:
        for s in self.scenarios:
            if s.id == scenario_id:
                return s
        return None

    def get_scenarios_by_vector(self, vector: str) -> List[Scenario]:
        return [s for s in self.scenarios if s.attack_vector == vector]

    def get_scenarios_by_severity(self, severity: str) -> List[Scenario]:
        return [s for s in self.scenarios if s.severity == severity]

    def simulate(self, scenario_id: str) -> SimulationResult:
        scenario = self.get_scenario(scenario_id)
        if not scenario:
            return SimulationResult(scenario_id, 0, 0, 0, 0.0, ["Scenario not found"])

        total_steps = len(scenario.mitre_techniques) * 3
        detections = random.randint(0, total_steps)
        detection_rate = detections / total_steps if total_steps > 0 else 0

        recommendations = [
            f"Implement monitoring for {technique}" for technique in scenario.mitre_techniques
        ]
        recommendations.append("Conduct regular threat hunting exercises")

        result = SimulationResult(
            scenario_id=scenario_id, steps_executed=total_steps,
            detections=detections, total_steps=total_steps,
            detection_rate=detection_rate, recommendations=recommendations,
        )
        self.simulation_history.append(result)
        return result

    def generate_random(self) -> Scenario:
        self.counter += 1
        vector = random.choice(list(AttackVector))
        return Scenario(
            id=f"RAND-{self.counter:04d}", name=f"Random {vector.value.title()}",
            attack_vector=vector.value, description=f"Randomly generated {vector.value} scenario",
            mitre_techniques=[f"T{random.randint(1000, 1500)}"],
            severity=random.choice(["low", "medium", "high", "critical"]),
            objectives=["Simulate attack", "Test defenses"], timeline_hours=random.randint(1, 168),
            indicators=["Suspicious activity"],
        )

    def get_statistics(self) -> Dict[str, Any]:
        return {
            "total_scenarios": len(self.scenarios),
            "simulations_run": len(self.simulation_history),
            "avg_detection_rate": sum(s.detection_rate for s in self.simulation_history) / len(self.simulation_history) if self.simulation_history else 0,
        }

    def __len__(self) -> int:
        return len(self.scenarios)

    def __repr__(self) -> str:
        return f"ThreatSim(scenarios={len(self.scenarios)})"
