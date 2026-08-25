"""ThreatModeler - Visual Threat Modeling Tool"""
from dataclasses import dataclass, field
from typing import List, Dict, Optional
from enum import Enum
import json


class STRIDECategory(Enum):
    SPOOFING = "spoofing"
    TAMPERING = "tampering"
    REPUDIATION = "repudiation"
    INFO_DISCLOSURE = "information_disclosure"
    DENIAL_OF_SERVICE = "denial_of_service"
    ELEVATION = "elevation_of_privilege"


class RiskLevel(Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"


@dataclass
class Component:
    """System component."""
    id: str
    name: str
    type: str
    description: str
    trust_boundary: bool = False


@dataclass
class Threat:
    """Threat entry."""
    id: str
    component: str
    category: str
    description: str
    risk_level: str
    mitigation: str
    status: str = "open"


@dataclass
class ThreatModel:
    """Complete threat model."""
    id: str
    name: str
    description: str
    components: List[Component] = field(default_factory=list)
    threats: List[Threat] = field(default_factory=list)
    created: str = ""
    updated: str = ""


class ThreatModeler:
    """
    Visual threat modeling tool.
    
    Usage:
        tm = ThreatModeler()
        model = tm.create_model(name="My App", components=["Web", "DB"])
        tm.add_threat(model.id, component="Web", threat="SQL Injection")
    """
    
    # STRIDE threat templates
    STRIDE_TEMPLATES = {
        "spoofing": [
            "Identity spoofing via stolen credentials",
            "Session hijacking",
            "DNS spoofing"
        ],
        "tampering": [
            "Data modification in transit",
            "Configuration tampering",
            "Code injection"
        ],
        "repudiation": [
            "Log deletion",
            "Transaction denial",
            "Audit trail bypass"
        ],
        "information_disclosure": [
            "Data leakage via logs",
            "Error message exposure",
            "Directory traversal"
        ],
        "denial_of_service": [
            "Resource exhaustion",
            "Flooding attack",
            "Dependency failure"
        ],
        "elevation_of_privilege": [
            "Privilege escalation via vulnerability",
            "Role manipulation",
            "Container escape"
        ]
    }
    
    def __init__(self):
        self.models: Dict[str, ThreatModel] = {}
        self.counter = 0
    
    def create_model(self, name: str, description: str = "",
                     components: List[str] = None) -> ThreatModel:
        """Create a new threat model."""
        self.counter += 1
        model_id = f"TM-{self.counter:03d}"
        
        comp_list = []
        if components:
            for i, comp_name in enumerate(components):
                comp_list.append(Component(
                    id=f"COMP-{i+1:03d}",
                    name=comp_name,
                    type="component",
                    description=f"{comp_name} component"
                ))
        
        model = ThreatModel(
            id=model_id,
            name=name,
            description=description,
            components=comp_list
        )
        
        self.models[model_id] = model
        return model
    
    def add_component(self, model_id: str, name: str, 
                      comp_type: str = "component",
                      trust_boundary: bool = False) -> Optional[Component]:
        """Add a component to a model."""
        model = self.models.get(model_id)
        if not model:
            return None
        
        comp = Component(
            id=f"COMP-{len(model.components)+1:03d}",
            name=name,
            type=comp_type,
            description=f"{name} component",
            trust_boundary=trust_boundary
        )
        model.components.append(comp)
        return comp
    
    def add_threat(self, model_id: str, component: str,
                   threat: str, category: str = "tampering",
                   risk_level: str = "medium",
                   mitigation: str = "") -> Optional[Threat]:
        """Add a threat to a model."""
        model = self.models.get(model_id)
        if not model:
            return None
        
        threat_entry = Threat(
            id=f"THR-{len(model.threats)+1:03d}",
            component=component,
            category=category,
            description=threat,
            risk_level=risk_level,
            mitigation=mitigation or "Implement appropriate controls"
        )
        model.threats.append(threat_entry)
        return threat_entry
    
    def get_stride_threats(self, component: str) -> List[str]:
        """Get STRIDE threats for a component."""
        threats = []
        for category, templates in self.STRIDE_TEMPLATES.items():
            for template in templates:
                threats.append(f"{component}: {template}")
        return threats
    
    def get_model(self, model_id: str) -> Optional[ThreatModel]:
        """Get a model by ID."""
        return self.models.get(model_id)
    
    def get_statistics(self, model_id: str) -> Dict:
        """Get model statistics."""
        model = self.get_model(model_id)
        if not model:
            return {}
        
        by_risk = {}
        by_category = {}
        for threat in model.threats:
            by_risk[threat.risk_level] = by_risk.get(threat.risk_level, 0) + 1
            by_category[threat.category] = by_category.get(threat.category, 0) + 1
        
        return {
            "total_components": len(model.components),
            "total_threats": len(model.threats),
            "by_risk": by_risk,
            "by_category": by_category
        }
    
    def export_model(self, model_id: str, output_file: str):
        """Export model to JSON."""
        model = self.get_model(model_id)
        if not model:
            return
        
        data = {
            "id": model.id,
            "name": model.name,
            "components": [{"id": c.id, "name": c.name, "type": c.type} 
                          for c in model.components],
            "threats": [{"id": t.id, "component": t.component, 
                        "category": t.category, "description": t.description,
                        "risk_level": t.risk_level} for t in model.threats]
        }
        
        with open(output_file, 'w') as f:
            json.dump(data, f, indent=2)
    
    def __len__(self) -> int:
        return len(self.models)
    
    def __repr__(self) -> str:
        return f"ThreatModeler(models={len(self.models)})"
