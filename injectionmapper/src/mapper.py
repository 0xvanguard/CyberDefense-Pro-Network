"""InjectionMapper - Attack Surface Mapping for Agentic Systems"""
from dataclasses import dataclass, field
from typing import List, Dict
from enum import Enum

class AttackSurface(Enum):
    RAG = "rag"
    TOOL_CALLS = "tool_calls"
    MEMORY = "memory"
    PLANNING = "planning"
    MULTI_MODAL = "multi_modal"

@dataclass
class SurfaceEntry:
    id: str
    surface: str
    vulnerability: str
    severity: str
    description: str
    mitigation: str

class InjectionMapper:
    def __init__(self):
        self.surfaces: List[SurfaceEntry] = []
        self._load_default_surfaces()
    
    def _load_default_surfaces(self):
        defaults = [
            ("RAG-001", "rag", "Document Poisoning", "critical", "Malicious content in RAG documents", "Validate and sanitize all documents"),
            ("TOOL-001", "tool_calls", "Tool Poisoning", "high", "Malicious tool descriptions", "Verify tool schemas"),
            ("MEM-001", "memory", "Memory Injection", "high", "Poisoning agent memory", "Validate memory updates"),
            ("PLAN-001", "planning", "Goal Hijacking", "high", "Redirecting agent goals", "Validate plan changes"),
        ]
        for s in defaults:
            self.surfaces.append(SurfaceEntry(*s))
    
    def map_surface(self, system_type: str = "generic") -> List[SurfaceEntry]:
        return self.surfaces
    
    def add_surface(self, surface: SurfaceEntry):
        self.surfaces.append(surface)
    
    def __repr__(self): return f"InjectionMapper(surfaces={len(self.surfaces)})"
