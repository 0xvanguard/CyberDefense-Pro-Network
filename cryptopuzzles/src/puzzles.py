"""CryptoPuzzles - Educational Cryptography Games"""
from dataclasses import dataclass, field
from typing import List, Optional
import hashlib
import base64


@dataclass
class Puzzle:
    """Crypto puzzle definition."""
    id: int
    title: str
    category: str
    difficulty: str
    challenge: str
    answer: str
    hint: str
    explanation: str
    points: int


class CryptoPuzzles:
    """
    Educational cryptography puzzles.
    
    Usage:
        cp = CryptoPuzzles()
        puzzle = cp.get_puzzle(level=1)
        result = cp.check_answer(puzzle.id, "answer")
    """
    
    def __init__(self):
        self.puzzles = self._load_puzzles()
        self.solved = set()
    
    def _load_puzzles(self) -> List[Puzzle]:
        """Load puzzle definitions."""
        return [
            Puzzle(
                id=1, title="Caesar's Secret",
                category="caesar", difficulty="easy",
                challenge="Decrypt: KHOOR ZRUOG",
                answer="hello world",
                hint="Try shifting each letter back by 3",
                explanation="Caesar cipher shifts each letter by a fixed number. ROT3 = shift back 3.",
                points=100
            ),
            Puzzle(
                id=2, title="Base64 Decode",
                category="base64", difficulty="easy",
                challenge="Decode: SGVsbG8gV29ybGQ=",
                answer="hello world",
                hint="This is Base64 encoding",
                explanation="Base64 encodes binary data as ASCII text using 64 characters.",
                points=100
            ),
            Puzzle(
                id=3, title="XOR Mystery",
                category="xor", difficulty="medium",
                challenge="XOR these hex values: 0x48 XOR 0x35 = ?",
                answer="0x7d",
                hint="XOR truth table: same=0, different=1",
                explanation="XOR operation: 01001000 XOR 00110101 = 01111101 = 0x7d",
                points=200
            ),
            Puzzle(
                id=4, title="Hash Hunter",
                category="hash", difficulty="medium",
                challenge="Find the input: MD5 = 5d41402abc4b2a76b9719d911017c592",
                answer="hello",
                hint="Try common words",
                explanation="MD5('hello') = 5d41402abc4b2a76b9719d911017c592",
                points=200
            ),
            Puzzle(
                id=5, title="ROT13 Challenge",
                category="caesar", difficulty="easy",
                challenge="Decrypt: Uryyb Jbeyq",
                answer="hello world",
                hint="ROT13 is Caesar cipher with shift 13",
                explanation="ROT13 shifts each letter by 13 positions in the alphabet.",
                points=100
            ),
            Puzzle(
                id=6, title="Binary Message",
                category="binary", difficulty="easy",
                challenge="Convert: 01001000 01100101 01101100 01101100 01101111",
                answer="hello",
                hint="Convert each byte to ASCII",
                explanation="Each 8-bit binary number represents an ASCII character.",
                points=100
            ),
            Puzzle(
                id=7, title="Caesar's Challenge",
                category="caesar", difficulty="easy",
                challenge="Decrypt with shift 7: Aopk pz h zljyla",
                answer="this is a secret",
                hint="Shift back 7 positions",
                explanation="Caesar cipher with shift 7.",
                points=150
            ),
            Puzzle(
                id=8, title="Hex Decoder",
                category="hex", difficulty="easy",
                challenge="Decode hex: 68656c6c6f",
                answer="hello",
                hint="Convert hex pairs to ASCII",
                explanation="Each hex pair represents one ASCII character.",
                points=100
            ),
            Puzzle(
                id=9, title="XOR Encryption",
                category="xor", difficulty="medium",
                challenge="Decrypt with key 0x42: XOR these bytes [0x26, 0x06, 0x00, 0x06, 0x17]",
                answer="hello",
                hint="XOR each byte with the key",
                explanation="XOR is symmetric: encrypt and decrypt use the same operation.",
                points=250
            ),
            Puzzle(
                id=10, title="Hash Collision",
                category="hash", difficulty="hard",
                challenge="Find another string with MD5: d41d8cd98f00b204e9800998ecf8427e",
                answer="",
                hint="Empty string has this hash",
                explanation="MD5 of empty string is d41d8cd98f00b204e9800998ecf8427e",
                points=300
            ),
        ]
    
    def get_puzzle(self, level: int = None, category: str = None) -> Optional[Puzzle]:
        """Get a puzzle by level or category."""
        if level:
            for p in self.puzzles:
                if p.id == level:
                    return p
        if category:
            for p in self.puzzles:
                if p.category == category:
                    return p
        return self.puzzles[0] if self.puzzles else None
    
    def get_unsolved(self) -> List[Puzzle]:
        """Get all unsolved puzzles."""
        return [p for p in self.puzzles if p.id not in self.solved]
    
    def check_answer(self, puzzle_id: int, answer: str) -> dict:
        """Check if an answer is correct."""
        puzzle = self.get_puzzle(level=puzzle_id)
        if not puzzle:
            return {"correct": False, "error": "Puzzle not found"}
        
        correct = answer.lower().strip() == puzzle.answer.lower().strip()
        if correct:
            self.solved.add(puzzle_id)
        
        return {
            "correct": correct,
            "puzzle_id": puzzle_id,
            "points": puzzle.points if correct else 0,
            "explanation": puzzle.explanation if correct else None
        }
    
    def get_progress(self) -> dict:
        """Get user progress."""
        total_points = sum(p.points for p in self.puzzles)
        earned_points = sum(p.points for p in self.puzzles if p.id in self.solved)
        
        return {
            "solved": len(self.solved),
            "total": len(self.puzzles),
            "points": earned_points,
            "max_points": total_points,
            "percentage": (len(self.solved) / len(self.puzzles) * 100) if self.puzzles else 0
        }
    
    def __len__(self) -> int:
        return len(self.puzzles)
    
    def __repr__(self) -> str:
        return f"CryptoPuzzles(puzzles={len(self.puzzles)})"
