"""SecureCoding101 — Interactive Secure Coding Course

10+ lessons covering SQL injection, XSS, authentication, cryptography,
input validation, CSRF, file upload, SSRF, and more.
Includes quiz questions and code vulnerability checking.
"""

import re
from dataclasses import dataclass, field
from typing import List, Dict, Optional, Any
from enum import Enum


# ─── Enums ───────────────────────────────────────────────────────────

class LessonCategory(Enum):
    INJECTION = "injection"
    WEB = "web"
    AUTH = "auth"
    CRYPTO = "crypto"
    VALIDATION = "validation"
    FILE_SECURITY = "file_security"
    NETWORK = "network"
    CONFIGURATION = "configuration"


# ─── Data Models ─────────────────────────────────────────────────────

@dataclass
class Lesson:
    """Secure coding lesson."""
    id: str
    title: str
    language: str
    category: str
    difficulty: str  # "beginner", "intermediate", "advanced"
    description: str
    vulnerable_code: str
    secure_code: str
    explanation: str
    key_points: List[str] = field(default_factory=list)
    references: List[str] = field(default_factory=list)
    exercises: List[Dict[str, str]] = field(default_factory=list)
    points: int = 100

    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id, "title": self.title, "language": self.language,
            "category": self.category, "difficulty": self.difficulty,
            "description": self.description, "points": self.points,
            "key_points": self.key_points,
        }


@dataclass
class QuizQuestion:
    """Quiz question for a lesson."""
    id: str
    lesson_id: str
    question: str
    options: List[str]
    correct_index: int
    explanation: str

    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id, "lesson_id": self.lesson_id,
            "question": self.question, "options": self.options,
            "explanation": self.explanation,
        }


# ─── SecureCoding Engine ────────────────────────────────────────────

class SecureCoding:
    """
    Interactive secure coding course.

    Usage:
        sc = SecureCoding()
        lesson = sc.get_lesson("sql_injection")
        result = sc.check_fix(lesson.id, user_code)
    """

    def __init__(self):
        self.lessons: List[Lesson] = self._load_lessons()
        self.quizzes: List[QuizQuestion] = self._load_quizzes()
        self.completed: set = set()
        self.quiz_results: Dict[str, bool] = {}

    def _load_lessons(self) -> List[Lesson]:
        return [
            Lesson(
                id="sql_injection", title="SQL Injection Prevention",
                language="python", category="injection", difficulty="beginner",
                description="Learn to prevent SQL injection attacks in Python applications.",
                vulnerable_code='''# VULNERABLE CODE\ndef get_user(username):\n    query = "SELECT * FROM users WHERE username = \'" + username + "\'"\n    cursor.execute(query)\n    return cursor.fetchone()''',
                secure_code='''# SECURE CODE\ndef get_user(username):\n    query = "SELECT * FROM users WHERE username = %s"\n    cursor.execute(query, (username,))\n    return cursor.fetchone()''',
                explanation="Always use parameterized queries. Never concatenate user input into SQL.",
                key_points=["Use parameterized queries", "Never concatenate user input", "Use ORM when possible"],
                references=["OWASP SQL Injection", "CWE-89"],
                exercises=[{"type": "fix", "description": "Fix the SQL injection vulnerability"}],
                points=200,
            ),
            Lesson(
                id="xss_prevention", title="XSS Prevention",
                language="javascript", category="web", difficulty="beginner",
                description="Learn to prevent Cross-Site Scripting attacks.",
                vulnerable_code='''// VULNERABLE CODE\nfunction displayComment(comment) {\n    document.getElementById('comments').innerHTML += comment;\n}''',
                secure_code='''// SECURE CODE\nfunction displayComment(comment) {\n    const div = document.createElement('div');\n    div.textContent = comment;\n    document.getElementById('comments').appendChild(div);\n}''',
                explanation="Never use innerHTML with user data. Use textContent or escape HTML entities.",
                key_points=["Use textContent instead of innerHTML", "Escape HTML entities", "Use CSP headers"],
                references=["OWASP XSS", "CWE-79"],
                exercises=[{"type": "fix", "description": "Fix the XSS vulnerability"}],
                points=200,
            ),
            Lesson(
                id="auth_security", title="Authentication Best Practices",
                language="python", category="auth", difficulty="intermediate",
                description="Secure authentication implementation.",
                vulnerable_code='''# VULNERABLE CODE\ndef login(username, password):\n    if users[username] == password:\n        return True\n    return False''',
                secure_code='''# SECURE CODE\nimport bcrypt\n\ndef login(username, password):\n    stored_hash = users[username]\n    return bcrypt.checkpw(password.encode(), stored_hash)''',
                explanation="Never store plain text passwords. Use bcrypt or argon2 for hashing.",
                key_points=["Use bcrypt/argon2", "Never store plaintext passwords", "Implement account lockout"],
                references=["OWASP Authentication", "CWE-256"],
                exercises=[{"type": "fix", "description": "Implement secure password hashing"}],
                points=250,
            ),
            Lesson(
                id="input_validation", title="Input Validation",
                language="python", category="validation", difficulty="beginner",
                description="Proper input validation techniques.",
                vulnerable_code='''# VULNERABLE CODE\ndef process_age(age):\n    return int(age) * 365''',
                secure_code='''# SECURE CODE\ndef process_age(age):\n    try:\n        age_int = int(age)\n        if 0 <= age_int <= 150:\n            return age_int * 365\n        raise ValueError("Age out of range")\n    except ValueError:\n        raise ValueError("Invalid age")''',
                explanation="Always validate and sanitize user input. Check type, range, and format.",
                key_points=["Validate type and range", "Whitelist preferred over blacklist", "Use allowlists"],
                references=["OWASP Input Validation", "CWE-20"],
                exercises=[{"type": "fix", "description": "Add proper input validation"}],
                points=150,
            ),
            Lesson(
                id="crypto_basics", title="Cryptography Basics",
                language="python", category="crypto", difficulty="intermediate",
                description="Secure cryptographic practices.",
                vulnerable_code='''# VULNERABLE CODE\nimport hashlib\n\ndef hash_password(password):\n    return hashlib.md5(password.encode()).hexdigest()''',
                secure_code='''# SECURE CODE\nimport bcrypt\n\ndef hash_password(password):\n    salt = bcrypt.gensalt()\n    return bcrypt.hashpw(password.encode(), salt)''',
                explanation="MD5 is broken for security. Use bcrypt for password hashing with salt.",
                key_points=["Never use MD5/SHA1 for passwords", "Use bcrypt/argon2 with salt", "Use AES-GCM for encryption"],
                references=["OWASP Cryptographic Failures", "CWE-327"],
                exercises=[{"type": "fix", "description": "Replace MD5 with bcrypt"}],
                points=200,
            ),
            Lesson(
                id="csrf_prevention", title="CSRF Prevention",
                language="javascript", category="web", difficulty="intermediate",
                description="Prevent Cross-Site Request Forgery attacks.",
                vulnerable_code='''<!-- VULNERABLE CODE -->\n<form action="/transfer" method="POST">\n    <input name="amount" value="1000">\n    <button>Transfer</button>\n</form>''',
                secure_code='''<!-- SECURE CODE -->\n<form action="/transfer" method="POST">\n    <input type="hidden" name="csrf_token" value="{{csrf_token}}">\n    <input name="amount" value="1000">\n    <button>Transfer</button>\n</form>''',
                explanation="Always use CSRF tokens in state-changing requests. Validate tokens server-side.",
                key_points=["Use CSRF tokens", "Validate tokens server-side", "Use SameSite cookies"],
                references=["OWASP CSRF", "CWE-352"],
                exercises=[{"type": "fix", "description": "Add CSRF protection"}],
                points=200,
            ),
            Lesson(
                id="file_upload", title="Secure File Upload",
                language="python", category="file_security", difficulty="intermediate",
                description="Secure file upload handling.",
                vulnerable_code='''# VULNERABLE CODE\ndef upload(file):\n    filename = file.filename\n    file.save(f"/uploads/{filename}")  # Path traversal!''',
                secure_code='''# SECURE CODE\nimport os\nimport uuid\n\ndef upload(file):\n    ext = os.path.splitext(file.filename)[1].lower()\n    if ext not in ALLOWED_EXTENSIONS:\n        raise ValueError("Invalid file type")\n    safe_name = f"{uuid.uuid4()}{ext}"\n    file.save(f"/uploads/{safe_name}")''',
                explanation="Validate file type, use random filenames, store outside webroot.",
                key_points=["Validate file extension", "Use random filenames", "Store outside webroot"],
                references=["OWASP File Upload", "CWE-434"],
                exercises=[{"type": "fix", "description": "Secure the file upload"}],
                points=200,
            ),
            Lesson(
                id="ssrf_prevention", title="SSRF Prevention",
                language="python", category="network", difficulty="advanced",
                description="Prevent Server-Side Request Forgery.",
                vulnerable_code='''# VULNERABLE CODE\ndef fetch_url(url):\n    response = requests.get(url)  # SSRF!\n    return response.text''',
                secure_code='''# SECURE CODE\nimport ipaddress\nfrom urllib.parse import urlparse\n\ndef fetch_url(url):\n    parsed = urlparse(url)\n    if parsed.scheme not in ("http", "https"):\n        raise ValueError("Invalid scheme")\n    ip = ipaddress.ip_address(socket.gethostbyname(parsed.hostname))\n    if ip.is_private or ip.is_loopback:\n        raise ValueError("Internal access blocked")\n    return requests.get(url, timeout=5)''',
                explanation="Validate and sanitize URLs. Block internal IPs. Use allowlists.",
                key_points=["Block internal IPs", "Validate URL scheme", "Use allowlists for domains"],
                references=["OWASP SSRF", "CWE-918"],
                exercises=[{"type": "fix", "description": "Prevent SSRF"}],
                points=300,
            ),
            Lesson(
                id="command_injection", title="Command Injection Prevention",
                language="python", category="injection", difficulty="intermediate",
                description="Prevent OS command injection.",
                vulnerable_code='''# VULNERABLE CODE\nimport os\n\ndef ping(host):\n    os.system(f"ping -c 1 {host}")''',
                secure_code='''# SECURE CODE\nimport subprocess\nimport shlex\n\ndef ping(host):\n    if not re.match(r"^[a-zA-Z0-9.-]+$", host):\n        raise ValueError("Invalid hostname")\n    subprocess.run(["ping", "-c", "1", host], capture_output=True)''',
                explanation="Never use os.system with user input. Use subprocess with argument lists.",
                key_points=["Use subprocess with list args", "Validate input with regex", "Never use shell=True"],
                references=["OWASP Command Injection", "CWE-78"],
                exercises=[{"type": "fix", "description": "Prevent command injection"}],
                points=250,
            ),
            Lesson(
                id="path_traversal", title="Path Traversal Prevention",
                language="python", category="file_security", difficulty="beginner",
                description="Prevent directory traversal attacks.",
                vulnerable_code='''# VULNERABLE CODE\ndef read_file(filename):\n    with open(f"/data/{filename}") as f:\n        return f.read()''',
                secure_code='''# SECURE CODE\nimport os\n\ndef read_file(filename):\n    base_dir = "/data"\n    safe_path = os.path.normpath(os.path.join(base_dir, filename))\n    if not safe_path.startswith(base_dir):\n        raise ValueError("Path traversal detected")\n    with open(safe_path) as f:\n        return f.read()''',
                explanation="Validate and normalize file paths. Check that resolved path stays within allowed directory.",
                key_points=["Use os.path.normpath", "Validate resolved path", "Use allowlists for filenames"],
                references=["OWASP Path Traversal", "CWE-22"],
                exercises=[{"type": "fix", "description": "Prevent path traversal"}],
                points=200,
            ),
            Lesson(
                id="hardcoded_secrets", title="Hardcoded Secrets Prevention",
                language="python", category="configuration", difficulty="beginner",
                description="Avoid hardcoding secrets in source code.",
                vulnerable_code='''# VULNERABLE CODE\nAPI_KEY = "sk-1234567890abcdef"\nDB_PASSWORD = "supersecret123"\n\ndef connect():\n    return db.connect(password=DB_PASSWORD)''',
                secure_code='''# SECURE CODE\nimport os\n\nAPI_KEY = os.environ.get("API_KEY")\nDB_PASSWORD = os.environ.get("DB_PASSWORD")\n\ndef connect():\n    if not DB_PASSWORD:\n        raise ValueError("DB_PASSWORD not set")\n    return db.connect(password=DB_PASSWORD)''',
                explanation="Never hardcode secrets. Use environment variables or secret managers.",
                key_points=["Use environment variables", "Use secret managers", "Never commit secrets to git"],
                references=["OWASP Secrets Management", "CWE-798"],
                exercises=[{"type": "fix", "description": "Remove hardcoded secrets"}],
                points=150,
            ),
            Lesson(
                id="insecure_deserialization", title="Insecure Deserialization",
                language="python", category="web", difficulty="advanced",
                description="Prevent insecure deserialization attacks.",
                vulnerable_code='''# VULNERABLE CODE\nimport pickle\n\ndef load_data(data):\n    return pickle.loads(data)  # Dangerous!''',
                secure_code='''# SECURE CODE\nimport json\n\ndef load_data(data):\n    return json.loads(data)  # Safe: JSON only''',
                explanation="Never unpickle untrusted data. Use JSON or other safe formats.",
                key_points=["Never pickle untrusted data", "Use JSON instead", "Validate data before deserialization"],
                references=["OWASP Deserialization", "CWE-502"],
                exercises=[{"type": "fix", "description": "Fix insecure deserialization"}],
                points=300,
            ),
        ]

    def _load_quizzes(self) -> List[QuizQuestion]:
        return [
            QuizQuestion("q1", "sql_injection",
                "Which method prevents SQL injection?",
                ["String concatenation", "Parameterized queries", "Escaping quotes", "Using eval()"],
                1, "Parameterized queries separate SQL from data."),
            QuizQuestion("q2", "xss_prevention",
                "Which property is safe for displaying user text?",
                ["innerHTML", "outerHTML", "textContent", "document.write()"],
                2, "textContent escapes HTML automatically."),
            QuizQuestion("q3", "auth_security",
                "Which is the best password hashing algorithm?",
                ["MD5", "SHA1", "SHA256", "bcrypt"],
                3, "bcrypt includes salt and is designed for passwords."),
            QuizQuestion("q4", "crypto_basics",
                "Why is MD5 insecure for passwords?",
                ["Too slow", "Too fast (rainbow tables)", "Not available", "Case sensitive"],
                1, "MD5 is too fast, enabling rainbow table attacks."),
            QuizQuestion("q5", "csrf_prevention",
                "What token protects against CSRF?",
                ["Session token", "CSRF token", "API key", "JWT"],
                1, "CSRF tokens are unique per-session and per-request."),
        ]

    def get_lesson(self, lesson_id: str) -> Optional[Lesson]:
        for lesson in self.lessons:
            if lesson.id == lesson_id:
                return lesson
        return None

    def get_lessons_by_category(self, category: str) -> List[Lesson]:
        return [l for l in self.lessons if l.category == category]

    def get_lessons_by_difficulty(self, difficulty: str) -> List[Lesson]:
        return [l for l in self.lessons if l.difficulty == difficulty]

    def get_quiz(self, lesson_id: str) -> Optional[QuizQuestion]:
        for q in self.quizzes:
            if q.lesson_id == lesson_id:
                return q
        return None

    def answer_quiz(self, quiz_id: str, answer_index: int) -> Dict[str, Any]:
        for q in self.quizzes:
            if q.id == quiz_id:
                correct = answer_index == q.correct_index
                self.quiz_results[quiz_id] = correct
                return {
                    "correct": correct,
                    "correct_answer": q.options[q.correct_index],
                    "explanation": q.explanation,
                }
        return {"error": "Quiz not found"}

    def check_fix(self, lesson_id: str, user_code: str) -> Dict[str, Any]:
        lesson = self.get_lesson(lesson_id)
        if not lesson:
            return {"error": "Lesson not found"}

        issues = []

        if "execute(" in user_code and "+" in user_code and "SELECT" in user_code.upper():
            issues.append("Still vulnerable to SQL injection - use parameterized queries")

        if "innerHTML" in user_code:
            issues.append("Still vulnerable to XSS - use textContent instead")

        if "md5" in user_code.lower():
            issues.append("MD5 is insecure - use bcrypt for password hashing")

        if "== password" in user_code or "==password" in user_code:
            issues.append("Plain text password comparison - use bcrypt.checkpw")

        if "os.system(" in user_code:
            issues.append("os.system is vulnerable to command injection - use subprocess")

        if "pickle.loads(" in user_code:
            issues.append("pickle.loads is insecure - use JSON")

        is_secure = len(issues) == 0

        if is_secure:
            self.completed.add(lesson_id)

        return {
            "is_secure": is_secure,
            "issues": issues,
            "points": lesson.points if is_secure else 0,
            "explanation": lesson.explanation,
        }

    def get_progress(self) -> Dict[str, Any]:
        total_points = sum(l.points for l in self.lessons)
        earned_points = sum(l.points for l in self.lessons if l.id in self.completed)
        quizzes_taken = len(self.quiz_results)
        quizzes_passed = sum(1 for v in self.quiz_results.values() if v)

        return {
            "completed": len(self.completed),
            "total": len(self.lessons),
            "points": earned_points,
            "max_points": total_points,
            "percentage": (len(self.completed) / len(self.lessons) * 100) if self.lessons else 0,
            "quizzes_taken": quizzes_taken,
            "quizzes_passed": quizzes_passed,
        }

    def get_categories(self) -> Dict[str, int]:
        cats = {}
        for l in self.lessons:
            cats[l.category] = cats.get(l.category, 0) + 1
        return cats

    def __len__(self) -> int:
        return len(self.lessons)

    def __repr__(self) -> str:
        return f"SecureCoding(lessons={len(self.lessons)})"
