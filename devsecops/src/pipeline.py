"""DevSecOps — Security Pipeline Automation"""
from dataclasses import dataclass, field
from typing import List, Dict, Optional
from datetime import datetime
from enum import Enum

class PipelineStage(Enum):
    CODE = "code"
    BUILD = "build"
    TEST = "test"
    SAST = "sast"
    DAST = "dast"
    DEPENDENCY = "dependency"
    CONTAINER = "container"
    DEPLOY = "deploy"

@dataclass
class SecurityGate:
    stage: str
    passed: bool
    findings: int
    severity_breakdown: Dict[str, int]

class DevSecOps:
    def __init__(self, project_name: str = "default"):
        self.project_name = project_name
        self.gates: List[SecurityGate] = []
        self.scan_count = 0

    def run_gate(self, stage: str, findings: int = 0, severity_breakdown: Optional[Dict[str, int]] = None) -> SecurityGate:
        severity_breakdown = severity_breakdown or {}
        critical = severity_breakdown.get("critical", 0)
        high = severity_breakdown.get("high", 0)
        passed = critical == 0 and high < 5
        gate = SecurityGate(stage=stage, passed=passed, findings=findings, severity_breakdown=severity_breakdown)
        self.gates.append(gate)
        self.scan_count += 1
        return gate

    def run_full_pipeline(self) -> List[SecurityGate]:
        stages = ["code", "build", "test", "sast", "dast", "dependency", "container", "deploy"]
        for stage in stages:
            self.run_gate(stage, findings=0)
        return self.gates

    def get_statistics(self) -> Dict:
        passed = sum(1 for g in self.gates if g.passed)
        return {"total_gates": len(self.gates), "passed": passed, "failed": len(self.gates) - passed}

    def __len__(self) -> int:
        return len(self.gates)

    def __repr__(self) -> str:
        return f"DevSecOps(project={self.project_name}, gates={len(self.gates)})"
