"""CyberLabs.io - Interactive Cybersecurity Labs Platform"""
from dataclasses import dataclass, field
from typing import List

@dataclass
class Lab:
    id: str
    title: str
    difficulty: str
    category: str
    description: str
    xp: int
    exercises: int

class CyberLabs:
    def __init__(self):
        self.labs = [
            Lab("LAB-001", "SQL Injection Basics", "easy", "web", "Learn SQL injection fundamentals", 100, 5),
            Lab("LAB-002", "XSS Workshop", "medium", "web", "Master cross-site scripting", 200, 8),
            Lab("LAB-003", "Crypto Challenge", "medium", "crypto", "Break weak encryption", 250, 6),
            Lab("LAB-004", "Network Forensics", "hard", "forensics", "Analyze packet captures", 300, 10),
            Lab("LAB-005", "AI Red Teaming", "hard", "ai", "Test LLM guardrails", 400, 12),
        ]
    
    def get_labs(self, difficulty=None):
        if difficulty: return [l for l in self.labs if l.difficulty == difficulty]
        return self.labs
    
    def __repr__(self): return f"CyberLabs(labs={len(self.labs)})"
