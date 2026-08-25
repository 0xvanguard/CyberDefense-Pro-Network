"""LanguagePreserver - Preserve Endangered Languages"""
from dataclasses import dataclass
from typing import List

@dataclass
class Language:
    name: str
    speakers: int
    status: str
    region: str

class LanguagePreserver:
    def __init__(self):
        self.languages = [
            Language("Aymara", 2800000, "vulnerable", "South America"),
            Language("Guarani", 6000000, "defended", "South America"),
            Language("Quechua", 8000000, "vulnerable", "South America"),
        ]
    
    def list_endangered(self): return [l for l in self.languages if l.status == "endangered"]
    def add_language(self, lang): self.languages.append(lang)
    def __repr__(self): return f"LanguagePreserver(languages={len(self.languages)})"
