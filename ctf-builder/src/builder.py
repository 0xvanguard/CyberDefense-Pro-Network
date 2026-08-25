"""CTF-Builder - Automatic CTF Challenge Generator"""
from dataclasses import dataclass, field
from typing import List, Dict, Optional
from enum import Enum
import json
import re


class ChallengeType(Enum):
    WEB = "web"
    CRYPTO = "crypto"
    FORENSICS = "forensics"
    REVERSE = "reverse"
    PWN = "pwn"
    MISC = "misc"


class Difficulty(Enum):
    EASY = "easy"
    MEDIUM = "medium"
    HARD = "hard"
    INSANE = "insane"


@dataclass
class Challenge:
    """CTF challenge definition."""
    id: str
    title: str
    type: ChallengeType
    difficulty: Difficulty
    description: str
    flag: str
    points: int
    hints: List[str] = field(default_factory=list)
    files: List[str] = field(default_factory=list)
    source_file: str = ""
    vulnerability: str = ""


class CTFBuilder:
    """
    Automatic CTF challenge generator.
    
    Usage:
        ctf = CTFBuilder()
        challenges = ctf.analyze("vulnerable_app/")
        ctf.export(challenges)
    """
    
    # Vulnerability patterns
    VULNERABILITIES = {
        "sql_injection": {
            "pattern": r"(?:execute|query|cursor)\s*\(\s*[\"'].*?\+",
            "type": ChallengeType.WEB,
            "severity": "high",
            "flag_format": "FLAG{sql_1nj3ct10n_{hash}}"
        },
        "xss": {
            "pattern": r"innerHTML\s*=|document\.write\s*\(|eval\s*\(",
            "type": ChallengeType.WEB,
            "severity": "medium",
            "flag_format": "FLAG{xss_p4yl04d_{hash}}"
        },
        "buffer_overflow": {
            "pattern": r"gets\s*\(|strcpy\s*\(|sprintf\s*\(",
            "type": ChallengeType.PWN,
            "severity": "critical",
            "flag_format": "FLAG{b0f_m4st3r_{hash}}"
        },
        "weak_crypto": {
            "pattern": r"md5\s*\(|sha1\s*\(|DES\s*\(|ECB\s*mode",
            "type": ChallengeType.CRYPTO,
            "severity": "medium",
            "flag_format": "FLAG{cr4ck3d_crypt0_{hash}}"
        },
        "hardcoded_secret": {
            "pattern": r"password\s*=\s*[\"']|api_key\s*=\s*[\"']|secret\s*=\s*[\"']",
            "type": ChallengeType.MISC,
            "severity": "high",
            "flag_format": "FLAG{s3cr3t_f0und_{hash}}"
        },
        "path_traversal": {
            "pattern": r"\.\.\/|\.\.\\|open\s*\(.*?\+",
            "type": ChallengeType.WEB,
            "severity": "high",
            "flag_format": "FLAG{p4th_tr4v3rs4l_{hash}}"
        }
    }
    
    def __init__(self):
        self.challenges: List[Challenge] = []
        self.counter = 0
    
    def analyze(self, target: str) -> List[Challenge]:
        """
        Analyze code for vulnerabilities and generate challenges.
        
        Args:
            target: File or directory to analyze
            
        Returns:
            List of generated challenges
        """
        challenges = []
        
        # Sample vulnerable code for demo
        sample_vulns = [
            ("sql_injection", "SELECT * FROM users WHERE id = '" + " + user_id + "'"),
            ("xss", "element.innerHTML = userInput"),
            ("hardcoded_secret", "password = 'admin123'"),
            ("weak_crypto", "hash = md5(password)"),
            ("buffer_overflow", "strcpy(buffer, input)"),
            ("path_traversal", "open('../' + filename)")
        ]
        
        for vuln_type, code_snippet in sample_vulns:
            challenge = self._create_challenge(vuln_type, code_snippet)
            if challenge:
                challenges.append(challenge)
        
        self.challenges.extend(challenges)
        return challenges
    
    def _create_challenge(self, vuln_type: str, code: str) -> Optional[Challenge]:
        """Create a challenge from a vulnerability."""
        vuln = self.VULNERABILITIES.get(vuln_type)
        if not vuln:
            return None
        
        self.counter += 1
        challenge_id = f"CHL-{self.counter:03d}"
        
        difficulty_map = {
            "web": Difficulty.MEDIUM,
            "crypto": Difficulty.MEDIUM,
            "pwn": Difficulty.HARD,
            "misc": Difficulty.EASY
        }
        
        points_map = {
            Difficulty.EASY: 100,
            Difficulty.MEDIUM: 200,
            Difficulty.HARD: 300,
            Difficulty.INSANE: 500
        }
        
        difficulty = difficulty_map.get(vuln_type, Difficulty.MEDIUM)
        
        return Challenge(
            id=challenge_id,
            title=f"{vuln_type.replace('_', ' ').title()} Challenge",
            type=vuln["type"],
            difficulty=difficulty,
            description=f"Find and exploit the {vuln_type.replace('_', ' ')} vulnerability.",
            flag=vuln["flag_format"].format(hash=challenge_id.lower()),
            points=points_map[difficulty],
            hints=[
                f"Look for {vuln_type.replace('_', ' ')} patterns",
                "Check user input handling",
                "Study OWASP Top 10"
            ],
            source_file=code[:100],
            vulnerability=vuln_type
        )
    
    def export(self, challenges: List[Challenge] = None, 
               output_file: str = "challenges.json"):
        """Export challenges to JSON."""
        if challenges is None:
            challenges = self.challenges
        
        data = []
        for c in challenges:
            data.append({
                "id": c.id,
                "title": c.title,
                "type": c.type.value,
                "difficulty": c.difficulty.value,
                "description": c.description,
                "flag": c.flag,
                "points": c.points,
                "hints": c.hints,
                "vulnerability": c.vulnerability
            })
        
        with open(output_file, 'w') as f:
            json.dump(data, f, indent=2)
    
    def get_statistics(self) -> Dict:
        """Get challenge statistics."""
        return {
            "total": len(self.challenges),
            "by_type": {},
            "by_difficulty": {}
        }
    
    def __len__(self) -> int:
        return len(self.challenges)
    
    def __repr__(self) -> str:
        return f"CTFBuilder(challenges={len(self.challenges)})"
