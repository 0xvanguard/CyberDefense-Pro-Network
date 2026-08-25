"""
CyberBot — Training Chatbot Engine

Interactive AI-powered cybersecurity education through conversation.
"""

import json
import random
import time
from typing import Dict, List, Optional
from dataclasses import dataclass, field
from enum import Enum


class Difficulty(Enum):
    BEGINNER = "beginner"
    INTERMEDIATE = "intermediate"
    ADVANCED = "advanced"
    EXPERT = "expert"


@dataclass
class KnowledgeEntry:
    """A piece of cybersecurity knowledge."""
    topic: str
    subtopic: str
    content: str
    difficulty: Difficulty
    tags: List[str] = field(default_factory=list)
    quiz_question: str = ""
    quiz_answer: str = ""
    quiz_options: List[str] = field(default_factory=list)


@dataclass
class UserProfile:
    """User learning profile."""
    name: str = "Learner"
    level: Difficulty = Difficulty.BEGINNER
    score: int = 0
    questions_answered: int = 0
    topics_completed: List[str] = field(default_factory=list)
    streak: int = 0

    def to_dict(self) -> dict:
        return {
            "name": self.name,
            "level": self.level.value,
            "score": self.score,
            "accuracy": f"{(self.score / max(self.questions_answered, 1) * 100):.0f}%",
            "streak": self.streak,
        }


@dataclass
class ChatResponse:
    """Response from the chatbot."""
    text: str
    topic: str = ""
    is_quiz: bool = False
    options: List[str] = field(default_factory=list)
    metadata: Dict = field(default_factory=dict)


class KnowledgeBase:
    """Cybersecurity knowledge base."""

    def __init__(self):
        self.entries: List[KnowledgeEntry] = []
        self._load_default_knowledge()

    def _load_default_knowledge(self):
        """Load built-in cybersecurity knowledge."""
        self.entries = [
            KnowledgeEntry(
                topic="owasp-top10", subtopic="injection",
                content="SQL Injection occurs when user input is inserted into SQL queries without proper sanitization. Attackers can execute arbitrary SQL commands, potentially accessing, modifying, or deleting data.",
                difficulty=Difficulty.BEGINNER,
                tags=["sql", "injection", "owasp", "web"],
                quiz_question="What is the primary cause of SQL Injection vulnerabilities?",
                quiz_answer="Unsanitized user input in SQL queries",
                quiz_options=[
                    "Weak passwords",
                    "Unsanitized user input in SQL queries",
                    "Outdated software",
                    "Missing firewalls",
                ],
            ),
            KnowledgeEntry(
                topic="owasp-top10", subtopic="xss",
                content="Cross-Site Scripting (XSS) allows attackers to inject malicious scripts into web pages viewed by other users. Types include Stored XSS, Reflected XSS, and DOM-based XSS.",
                difficulty=Difficulty.BEGINNER,
                tags=["xss", "injection", "owasp", "web"],
                quiz_question="Which type of XSS stores the payload on the server?",
                quiz_answer="Stored XSS",
                quiz_options=[
                    "Reflected XSS",
                    "DOM-based XSS",
                    "Stored XSS",
                    "Blind XSS",
                ],
            ),
            KnowledgeEntry(
                topic="owasp-top10", subtopic="broken-auth",
                content="Broken Authentication occurs when application flaws allow attackers to compromise passwords, keys, or session tokens. Common issues: credential stuffing, weak passwords, missing MFA.",
                difficulty=Difficulty.BEGINNER,
                tags=["authentication", "owasp", "session"],
                quiz_question="What is credential stuffing?",
                quiz_answer="Using leaked username/password pairs from other breaches to gain access",
                quiz_options=[
                    "Brute-forcing all possible passwords",
                    "Using leaked username/password pairs from other breaches",
                    "Phishing for credentials",
                    "Keylogging to capture credentials",
                ],
            ),
            KnowledgeEntry(
                topic="cryptography", subtopic="symmetric",
                content="Symmetric encryption uses the same key for encryption and decryption. Fast and efficient for large data. Examples: AES-256, ChaCha20, Blowfish. Challenge: secure key distribution.",
                difficulty=Difficulty.BEGINNER,
                tags=["crypto", "encryption", "aes"],
                quiz_question="What is the main challenge with symmetric encryption?",
                quiz_answer="Secure key distribution between parties",
                quiz_options=[
                    "It is too slow for large data",
                    "Secure key distribution between parties",
                    "It cannot encrypt text",
                    "It requires a certificate authority",
                ],
            ),
            KnowledgeEntry(
                topic="network", subtopic="firewall",
                content="Firewalls filter network traffic based on rules. Types: Packet-filtering (stateless), Stateful inspection, Application-layer (proxy), Next-gen (NGFW) with DPI and IPS.",
                difficulty=Difficulty.BEGINNER,
                tags=["network", "firewall", "perimeter"],
                quiz_question="Which firewall type inspects the state of active connections?",
                quiz_answer="Stateful inspection firewall",
                quiz_options=[
                    "Packet-filtering firewall",
                    "Stateful inspection firewall",
                    "Application-layer proxy",
                    "All of the above",
                ],
            ),
            KnowledgeEntry(
                topic="incident-response", subtopic="phases",
                content="NIST Incident Response: 1) Preparation, 2) Detection & Analysis, 3) Containment, 4) Eradication, 5) Recovery, 6) Post-incident Activity. Each phase has specific actions and deliverables.",
                difficulty=Difficulty.INTERMEDIATE,
                tags=["incident", "response", "nir", "nist"],
                quiz_question="Which NIST phase comes immediately after Detection & Analysis?",
                quiz_answer="Containment",
                quiz_options=[
                    "Eradication",
                    "Containment",
                    "Recovery",
                    "Preparation",
                ],
            ),
            KnowledgeEntry(
                topic="cloud", subtopic="shared-responsibility",
                content="Cloud Shared Responsibility Model: Provider secures the cloud infrastructure. Customer secures what's IN the cloud (data, IAM, OS patching). Responsibility shifts between IaaS, PaaS, SaaS.",
                difficulty=Difficulty.INTERMEDIATE,
                tags=["cloud", "aws", "azure", "shared-responsibility"],
                quiz_question="In the Shared Responsibility Model, who is responsible for patching guest OS in IaaS?",
                quiz_answer="The customer",
                quiz_options=[
                    "The cloud provider",
                    "The customer",
                    "Both equally",
                    "Neither — it's automatic",
                ],
            ),
            KnowledgeEntry(
                topic="malware", subtopic="ransomware",
                content="Ransomware encrypts files and demands payment. Evolution: Locker → Crypto → Double Extortion (data theft + encryption) → Triple Extortion (+ DDoS). Defenses: backups, EDR, network segmentation, user training.",
                difficulty=Difficulty.INTERMEDIATE,
                tags=["malware", "ransomware", "extortion"],
                quiz_question="What is 'double extortion' in modern ransomware?",
                quiz_answer="Encrypting data AND threatening to leak stolen data",
                quiz_options=[
                    "Demanding payment twice",
                    "Encrypting data AND threatening to leak stolen data",
                    "Attacking two networks simultaneously",
                    "Using two encryption algorithms",
                ],
            ),
        ]

    def search(self, query: str) -> List[KnowledgeEntry]:
        """Search knowledge base."""
        q = query.lower()
        return [e for e in self.entries
                if q in e.topic.lower() or q in e.subtopic.lower()
                or q in e.content.lower() or any(q in t for t in e.tags)]

    def get_by_topic(self, topic: str) -> List[KnowledgeEntry]:
        """Get entries by topic."""
        return [e for e in self.entries if e.topic == topic]

    def get_quiz(self, topic: str = None, difficulty: Difficulty = None) -> Optional[KnowledgeEntry]:
        """Get a random quiz question."""
        candidates = self.entries
        if topic:
            candidates = [e for e in candidates if e.topic == topic]
        if difficulty:
            candidates = [e for e in candidates if e.difficulty == difficulty]
        if candidates:
            return random.choice(candidates)
        return None


class CyberBot:
    """
    Main chatbot engine.

    Usage:
        bot = CyberBot()
        response = bot.chat("What is SQL injection?")
    """

    GREETINGS = [
        "Hey! I'm CyberBot 🤖 Ready to learn some cybersecurity?",
        "Welcome! Let's dive into security. What topic interests you?",
        "Hello! Ask me anything about cybersecurity, or say 'quiz' for a challenge!",
    ]

    def __init__(self, user: UserProfile = None):
        self.user = user or UserProfile()
        self.kb = KnowledgeBase()
        self.history: List[dict] = []
        self._pending_quiz: Optional[KnowledgeEntry] = None

    def chat(self, message: str) -> ChatResponse:
        """Process a user message and return a response."""
        msg = message.lower().strip()

        # Greeting
        if any(w in msg for w in ["hi", "hello", "hey", "hola", "start"]):
            return ChatResponse(text=random.choice(self.GREETINGS))

        # Quiz mode
        if "quiz" in msg or "test" in msg or "puzzle" in msg:
            return self._start_quiz(msg)

        # Answer quiz
        if self._pending_quiz and self._is_quiz_answer(msg):
            return self._answer_quiz(msg)

        # Topic request
        if "topics" in msg or "what can you" in msg:
            topics = list(set(e.topic for e in self.kb.entries))
            return ChatResponse(
                text=f"I can teach you about:\n" + "\n".join(f"• {t}" for t in topics),
            )

        # Search knowledge
        results = self.kb.search(msg)
        if results:
            entry = results[0]
            return ChatResponse(
                text=f"**{entry.topic}/{entry.subtopic}**\n\n{entry.content}",
                topic=entry.topic,
            )

        # Default
        return ChatResponse(
            text="I can help with cybersecurity topics like OWASP Top 10, cryptography, network security, incident response, and more. Try asking about a specific topic or say 'quiz' for a challenge!",
        )

    def _start_quiz(self, msg: str) -> ChatResponse:
        """Start a quiz question."""
        # Determine topic from message
        topic = None
        for t in ["owasp", "crypto", "network", "incident", "cloud", "malware"]:
            if t in msg:
                topic = t
                break

        quiz = self.kb.get_quiz(topic=topic, difficulty=self.user.level)
        if not quiz:
            return ChatResponse(text="No quiz questions available for that topic yet.")

        self._pending_quiz = quiz
        options_text = "\n".join(f"  {chr(65+i)}) {opt}" for i, opt in enumerate(quiz.quiz_options))

        return ChatResponse(
            text=f"🎯 **Quiz Question** ({quiz.difficulty.value})\n\n{quiz.quiz_question}\n\n{options_text}\n\nType the letter (A, B, C, D) or the full answer.",
            is_quiz=True,
            options=quiz.quiz_options,
            metadata={"topic": quiz.topic},
        )

    def _is_quiz_answer(self, msg: str) -> bool:
        """Check if message looks like a quiz answer."""
        return len(msg) <= 100  # Short answer

    def _answer_quiz(self, msg: str) -> ChatResponse:
        """Check quiz answer."""
        quiz = self._pending_quiz
        self._pending_quiz = None

        # Check if answer matches
        correct = False
        if msg.upper() in ["A", "B", "C", "D"]:
            idx = ord(msg.upper()) - 65
            if idx < len(quiz.quiz_options):
                correct = quiz.quiz_options[idx] == quiz.quiz_answer
        else:
            correct = msg.lower() in quiz.quiz_answer.lower()

        self.user.questions_answered += 1

        if correct:
            self.user.score += 1
            self.user.streak += 1
            text = f"✅ **Correct!** {quiz.quiz_answer}\n\n{quiz.content}"
        else:
            self.user.streak = 0
            text = f"❌ **Incorrect.** The answer is: {quiz.quiz_answer}\n\n{quiz.content}"

        return ChatResponse(
            text=text,
            topic=quiz.topic,
            metadata={"correct": correct, "score": self.user.score},
        )
