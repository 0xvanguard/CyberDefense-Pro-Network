"""SecureCoding101 - Interactive Secure Coding Course"""
from dataclasses import dataclass, field
from typing import List, Optional
import re


@dataclass
class Lesson:
    """Secure coding lesson."""
    id: str
    title: str
    language: str
    topic: str
    description: str
    vulnerable_code: str
    secure_code: str
    explanation: str
    exercises: List[dict] = field(default_factory=list)
    points: int = 100


class SecureCoding:
    """
    Interactive secure coding course.
    
    Usage:
        sc = SecureCoding()
        lesson = sc.get_lesson("sql_injection")
        result = sc.check_fix(lesson.id, user_code)
    """
    
    def __init__(self):
        self.lessons = self._load_lessons()
        self.completed = set()
    
    def _load_lessons(self) -> List[Lesson]:
        """Load course lessons."""
        return [
            Lesson(
                id="sql_injection",
                title="SQL Injection Prevention",
                language="python",
                topic="database",
                description="Learn to prevent SQL injection attacks in Python applications.",
                vulnerable_code='''# VULNERABLE CODE
def get_user(username):
    query = "SELECT * FROM users WHERE username = '" + username + "'"
    cursor.execute(query)
    return cursor.fetchone()''',
                secure_code='''# SECURE CODE
def get_user(username):
    query = "SELECT * FROM users WHERE username = %s"
    cursor.execute(query, (username,))
    return cursor.fetchone()''',
                explanation="Always use parameterized queries. Never concatenate user input into SQL.",
                exercises=[
                    {"type": "fix", "description": "Fix the SQL injection vulnerability"},
                    {"type": "identify", "description": "Identify the vulnerable line"}
                ],
                points=200
            ),
            Lesson(
                id="xss_prevention",
                title="XSS Prevention",
                language="javascript",
                topic="web",
                description="Learn to prevent Cross-Site Scripting attacks.",
                vulnerable_code='''// VULNERABLE CODE
function displayComment(comment) {
    document.getElementById('comments').innerHTML += comment;
}''',
                secure_code='''// SECURE CODE
function displayComment(comment) {
    const div = document.createElement('div');
    div.textContent = comment;  // Safe: textContent escapes HTML
    document.getElementById('comments').appendChild(div);
}''',
                explanation="Never use innerHTML with user data. Use textContent or escape HTML entities.",
                exercises=[
                    {"type": "fix", "description": "Fix the XSS vulnerability"},
                    {"type": "identify", "description": "Identify the dangerous function"}
                ],
                points=200
            ),
            Lesson(
                id="auth_security",
                title="Authentication Best Practices",
                language="python",
                topic="auth",
                description="Secure authentication implementation.",
                vulnerable_code='''# VULNERABLE CODE
def login(username, password):
    if users[username] == password:  # Plain text comparison
        return True
    return False''',
                secure_code='''# SECURE CODE
import bcrypt

def login(username, password):
    stored_hash = users[username]
    return bcrypt.checkpw(password.encode(), stored_hash)''',
                explanation="Never store plain text passwords. Use bcrypt or argon2 for hashing.",
                exercises=[
                    {"type": "fix", "description": "Implement secure password hashing"},
                    {"type": "identify", "description": "Why is plain text comparison bad?"}
                ],
                points=250
            ),
            Lesson(
                id="input_validation",
                title="Input Validation",
                language="python",
                topic="validation",
                description="Proper input validation techniques.",
                vulnerable_code='''# VULNERABLE CODE
def process_age(age):
    return int(age) * 365  # No validation!''',
                secure_code='''# SECURE CODE
def process_age(age):
    try:
        age_int = int(age)
        if 0 <= age_int <= 150:
            return age_int * 365
        raise ValueError("Age out of range")
    except ValueError:
        raise ValueError("Invalid age")''',
                explanation="Always validate and sanitize user input. Check type, range, and format.",
                exercises=[
                    {"type": "fix", "description": "Add proper input validation"},
                    {"type": "identify", "description": "What can go wrong without validation?"}
                ],
                points=150
            ),
            Lesson(
                id="crypto_basics",
                title="Cryptography Basics",
                language="python",
                topic="crypto",
                description="Secure cryptographic practices.",
                vulnerable_code='''# VULNERABLE CODE
import hashlib

def hash_password(password):
    return hashlib.md5(password.encode()).hexdigest()''',
                secure_code='''# SECURE CODE
import bcrypt

def hash_password(password):
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password.encode(), salt)''',
                explanation="MD5 is broken for security. Use bcrypt for password hashing with salt.",
                exercises=[
                    {"type": "fix", "description": "Replace MD5 with bcrypt"},
                    {"type": "identify", "description": "Why is MD5 insecure?"}
                ],
                points=200
            ),
        ]
    
    def get_lesson(self, lesson_id: str) -> Optional[Lesson]:
        """Get a lesson by ID."""
        for lesson in self.lessons:
            if lesson.id == lesson_id:
                return lesson
        return None
    
    def get_lessons_by_topic(self, topic: str) -> List[Lesson]:
        """Get lessons by topic."""
        return [l for l in self.lessons if l.topic == topic]
    
    def check_fix(self, lesson_id: str, user_code: str) -> dict:
        """Check if user's fix is secure."""
        lesson = self.get_lesson(lesson_id)
        if not lesson:
            return {"error": "Lesson not found"}
        
        issues = []
        
        # Check for common vulnerabilities
        if "execute(" in user_code and "+" in user_code:
            issues.append("Still vulnerable to SQL injection - use parameterized queries")
        
        if "innerHTML" in user_code:
            issues.append("Still vulnerable to XSS - use textContent instead")
        
        if "md5" in user_code.lower():
            issues.append("MD5 is insecure - use bcrypt for password hashing")
        
        if "==" in user_code and "password" in user_code.lower():
            issues.append("Plain text password comparison - use bcrypt.checkpw")
        
        is_secure = len(issues) == 0
        
        if is_secure:
            self.completed.add(lesson_id)
        
        return {
            "is_secure": is_secure,
            "issues": issues,
            "points": lesson.points if is_secure else 0,
            "explanation": lesson.explanation
        }
    
    def get_progress(self) -> dict:
        """Get course progress."""
        total_points = sum(l.points for l in self.lessons)
        earned_points = sum(l.points for l in self.lessons if l.id in self.completed)
        
        return {
            "completed": len(self.completed),
            "total": len(self.lessons),
            "points": earned_points,
            "max_points": total_points,
            "percentage": (len(self.completed) / len(self.lessons) * 100) if self.lessons else 0
        }
    
    def __len__(self) -> int:
        return len(self.lessons)
    
    def __repr__(self) -> str:
        return f"SecureCoding(lessons={len(self.lessons)})"
