"""
PromptKiller - Main Library
Comprehensive AI attack prompt collection for red teaming.
"""

import json
import os
import random
from typing import List, Dict, Optional, Tuple
from dataclasses import dataclass, field, asdict
from enum import Enum
from pathlib import Path


class Severity(Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"


class Category(Enum):
    ROLE_PLAY = "role_play"
    ENCODING = "encoding"
    MULTI_TURN = "multi_turn"
    INJECTION = "injection"
    JAILBREAK = "jailbreak"
    EXTRACTION = "extraction"
    MANIPULATION = "manipulation"
    CONTEXT = "context"
    MULTIMODAL = "multimodal"
    ADVERSARIAL = "adversarial"


@dataclass
class AttackPrompt:
    """Represents a single attack prompt."""
    id: str
    text: str
    category: str
    severity: str
    technique: str
    description: str
    target_models: List[str] = field(default_factory=lambda: ["all"])
    tags: List[str] = field(default_factory=list)
    success_rate: float = 0.0
    references: List[str] = field(default_factory=list)
    
    def to_dict(self) -> Dict:
        return asdict(self)


@dataclass
class AttackResult:
    """Result of running an attack."""
    prompt: AttackPrompt
    response: str
    success: bool
    model: str
    latency_ms: float = 0.0
    tokens_used: int = 0
    notes: str = ""


class PromptKiller:
    """
    Main class for the PromptKiller library.
    
    Usage:
        pk = PromptKiller()
        prompts = pk.get_by_category("role_play")
        results = pk.attack(model="gpt-4", categories=["all"])
    """
    
    def __init__(self, data_dir: Optional[str] = None):
        """Initialize PromptKiller with data directory."""
        if data_dir is None:
            data_dir = str(Path(__file__).parent.parent / "data")
        self.data_dir = data_dir
        self.prompts: List[AttackPrompt] = []
        self._load_all_prompts()
    
    def _load_all_prompts(self):
        """Load all prompt files from data directory."""
        data_path = Path(self.data_dir)
        if not data_path.exists():
            os.makedirs(data_path, exist_ok=True)
            return
        
        for json_file in data_path.glob("*.json"):
            try:
                with open(json_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    for item in data:
                        prompt = AttackPrompt(**item)
                        self.prompts.append(prompt)
            except Exception as e:
                print(f"Warning: Error loading {json_file}: {e}")
    
    def get_by_category(self, category: str) -> List[AttackPrompt]:
        """Get all prompts in a category."""
        return [p for p in self.prompts if p.category == category]
    
    def get_by_severity(self, severity: str) -> List[AttackPrompt]:
        """Get all prompts of a severity level."""
        return [p for p in self.prompts if p.severity == severity]
    
    def get_by_technique(self, technique: str) -> List[AttackPrompt]:
        """Get all prompts using a specific technique."""
        return [p for p in self.prompts if technique.lower() in p.technique.lower()]
    
    def get_by_model(self, model: str) -> List[AttackPrompt]:
        """Get all prompts targeting a specific model."""
        return [p for p in self.prompts if model in p.target_models or "all" in p.target_models]
    
    def get_random(self, count: int = 1) -> List[AttackPrompt]:
        """Get random prompts."""
        if count >= len(self.prompts):
            return self.prompts.copy()
        return random.sample(self.prompts, count)
    
    def search(self, query: str) -> List[AttackPrompt]:
        """Search prompts by text content."""
        query_lower = query.lower()
        results = []
        for p in self.prompts:
            if (query_lower in p.text.lower() or 
                query_lower in p.description.lower() or
                query_lower in p.technique.lower() or
                any(query_lower in tag.lower() for tag in p.tags)):
                results.append(p)
        return results
    
    def get_statistics(self) -> Dict:
        """Get statistics about the prompt library."""
        stats = {
            "total_prompts": len(self.prompts),
            "by_category": {},
            "by_severity": {},
            "by_technique": {}
        }
        
        for p in self.prompts:
            stats["by_category"][p.category] = stats["by_category"].get(p.category, 0) + 1
            stats["by_severity"][p.severity] = stats["by_severity"].get(p.severity, 0) + 1
            stats["by_technique"][p.technique] = stats["by_technique"].get(p.technique, 0) + 1
        
        return stats
    
    def add_prompt(self, prompt: AttackPrompt):
        """Add a new prompt to the library."""
        self.prompts.append(prompt)
    
    def export_category(self, category: str, output_file: str):
        """Export a category to JSON file."""
        prompts = self.get_by_category(category)
        data = [p.to_dict() for p in prompts]
        
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
    
    def export_all(self, output_dir: str):
        """Export all prompts organized by category."""
        os.makedirs(output_dir, exist_ok=True)
        
        categories = set(p.category for p in self.prompts)
        for category in categories:
            output_file = os.path.join(output_dir, f"{category}.json")
            self.export_category(category, output_file)
    
    def attack(self, model: str = "all", categories: List[str] = None, 
               severity: str = None, count: int = 10) -> List[AttackPrompt]:
        """
        Prepare an attack suite for testing.
        
        Returns prompts to test against the target model.
        """
        prompts = self.prompts.copy()
        
        if categories and "all" not in categories:
            prompts = [p for p in prompts if p.category in categories]
        
        if severity:
            prompts = [p for p in prompts if p.severity == severity]
        
        if model != "all":
            prompts = [p for p in prompts if model in p.target_models or "all" in p.target_models]
        
        return prompts[:count]
    
    def to_json(self) -> str:
        """Export entire library to JSON string."""
        data = [p.to_dict() for p in self.prompts]
        return json.dumps(data, indent=2, ensure_ascii=False)
    
    def __len__(self) -> int:
        return len(self.prompts)
    
    def __repr__(self) -> str:
        return f"PromptKiller(prompts={len(self.prompts)})"
