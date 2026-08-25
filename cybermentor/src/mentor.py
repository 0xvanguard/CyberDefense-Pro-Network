"""CyberMentor - Mentorship Platform for Cybersecurity"""
from dataclasses import dataclass
from typing import List

@dataclass
class Mentor:
    id: str
    name: str
    expertise: str
    experience_years: int

@dataclass
class Mentee:
    id: str
    name: str
    level: str
    goals: List[str]

class MentorPlatform:
    def __init__(self):
        self.mentors = []
        self.mentees = []
    
    def add_mentor(self, mentor): self.mentors.append(mentor)
    def add_mentee(self, mentee): self.mentees.append(mentee)
    def match(self, mentee): return self.mentors[0] if self.mentors else None
    def __repr__(self): return f"MentorPlatform(mentors={len(self.mentors)})"
