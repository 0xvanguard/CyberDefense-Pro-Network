"""HackTheClass - K-12 Cybersecurity Curriculum"""
from dataclasses import dataclass
from typing import List

@dataclass
class Lesson:
    id: str
    grade: str
    title: str
    topic: str
    duration_min: int

class Curriculum:
    def __init__(self):
        self.lessons = [
            Lesson("L01", "K-2", "Internet Safety Basics", "safety", 30),
            Lesson("L02", "3-5", "Password Power", "auth", 45),
            Lesson("L03", "6-8", "Phishing Detection", "social", 60),
            Lesson("L04", "9-12", "Network Security", "network", 90),
            Lesson("L05", "9-12", "Python for Security", "coding", 120),
        ]
    
    def get_by_grade(self, grade): return [l for l in self.lessons if l.grade == grade]
    def __repr__(self): return f"Curriculum(lessons={len(self.lessons)})"
