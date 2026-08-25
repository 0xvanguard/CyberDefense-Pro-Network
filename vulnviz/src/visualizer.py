"""VulnViz - Vulnerability Visualizer"""
from dataclasses import dataclass
from typing import List, Dict

@dataclass
class VulnNode:
    id: str
    name: str
    severity: str
    cvss: float

@dataclass
class VulnEdge:
    source: str
    target: str
    relationship: str

class VulnGraph:
    def __init__(self):
        self.nodes: List[VulnNode] = []
        self.edges: List[VulnEdge] = []
    
    def add_node(self, node): self.nodes.append(node)
    def add_edge(self, edge): self.edges.append(edge)
    def to_json(self): return {"nodes": len(self.nodes), "edges": len(self.edges)}
    def __repr__(self): return f"VulnGraph(nodes={len(self.nodes)}, edges={len(self.edges)})"
