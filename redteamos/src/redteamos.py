"""RedTeamOS - Live Boot OS for AI Red Teaming"""
from dataclasses import dataclass
from typing import List

@dataclass
class Tool:
    name: str
    category: str
    description: str
    command: str

class RedTeamOS:
    def __init__(self):
        self.tools = [
            Tool("PromptKiller", "attack", "Attack prompt library", "promptkiller"),
            Tool("GuardDog", "defense", "Injection scanner", "guarddog"),
            Tool("JailbreakBench", "benchmark", "Jailbreak evaluation", "jailbreakbench"),
            Tool("ConstitutionalKit", "defense", "Constitutional AI", "constitutionalkit"),
        ]
    
    def list_tools(self): return self.tools
    def add_tool(self, tool: Tool): self.tools.append(tool)
    def __repr__(self): return f"RedTeamOS(tools={len(self.tools)})"
