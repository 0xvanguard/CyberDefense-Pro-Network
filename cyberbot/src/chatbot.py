"""CyberBot — Cybersecurity Training Chatbot"""
import re
import random
from dataclasses import dataclass, field
from typing import List, Dict, Optional
from enum import Enum

class Topic(Enum):
    PASSWORD = "password"
    NETWORK = "network"
    MALWARE = "malware"
    PHISHING = "phishing"
    ENCRYPTION = "encryption"
    FIREWALL = "firewall"
    VULNERABILITY = "vulnerability"
    GENERAL = "general"

@dataclass
class ChatResponse:
    response: str
    topic: str
    confidence: float
    follow_ups: List[str] = field(default_factory=list)

class CyberBot:
    def __init__(self, name: str = "CyberBot"):
        self.name = name
        self.knowledge_base = self._load_knowledge()
        self.conversation_history: List[Dict] = []
        self.score = 0

    def _load_knowledge(self) -> Dict[str, Dict]:
        return {
            "password": {
                "keywords": ["password", "passphrase", "credential", "login", "auth"],
                "responses": [
                    "🔑 Use passwords of 12+ characters with uppercase, lowercase, numbers, and symbols.",
                    "🔐 Never reuse passwords across sites. Use a password manager.",
                    "🎯 Passphrases like 'correct-horse-battery-staple' are both strong and memorable.",
                    "⚠️ Enable MFA wherever possible — it stops 99% of account compromise attacks.",
                ],
            },
            "network": {
                "keywords": ["network", "firewall", "router", "switch", "vlan", "subnet", "scan"],
                "responses": [
                    "🌐 Network segmentation limits blast radius of breaches.",
                    "🔥 Configure firewalls with default-deny: block everything, allow only what's needed.",
                    "📊 Regular network scanning helps identify unauthorized devices.",
                    "🛡️ Use VLANs to isolate sensitive systems from general network traffic.",
                ],
            },
            "malware": {
                "keywords": ["malware", "virus", "trojan", "ransomware", "worm", "rootkit"],
                "responses": [
                    "🦠 Keep systems patched — most malware exploits known vulnerabilities.",
                    "💾 Maintain offline backups to recover from ransomware.",
                    "🔍 Use EDR solutions for real-time malware detection.",
                    "📧 Most malware enters via email attachments — train users to verify senders.",
                ],
            },
            "phishing": {
                "keywords": ["phishing", "scam", "social engineering", "email", "spear"],
                "responses": [
                    "🎣 Check sender addresses carefully — attackers spoof legitimate domains.",
                    "🔗 Hover over links before clicking to verify the actual URL.",
                    "⚠️ Legitimate companies never ask for passwords via email.",
                    "🔍 Look for urgency tactics — 'Your account will be closed!' is a red flag.",
                ],
            },
            "encryption": {
                "keywords": ["encrypt", "decrypt", "cipher", "aes", "rsa", "tls", "ssl", "crypto"],
                "responses": [
                    "🔐 AES-256 is the gold standard for symmetric encryption.",
                    "🔑 RSA-2048+ for asymmetric, but prefer ECC for better performance.",
                    "🌐 Always use TLS 1.2+ — older versions have known vulnerabilities.",
                    "💾 Encrypt data at rest AND in transit for defense in depth.",
                ],
            },
            "firewall": {
                "keywords": ["firewall", "iptables", "nftables", "ufw", "rules"],
                "responses": [
                    "🔥 Default deny: block all traffic, then explicitly allow needed services.",
                    "📝 Log firewall drops to detect reconnaissance attempts.",
                    "🔄 Review firewall rules quarterly — remove stale entries.",
                    "🌍 Use WAF for web applications to filter HTTP-level attacks.",
                ],
            },
            "vulnerability": {
                "keywords": ["vulnerability", "cve", "exploit", "patch", "scan", "pentest"],
                "responses": [
                    "🔍 Scan for vulnerabilities weekly and patch critical findings within 24 hours.",
                    "📋 Maintain a vulnerability management program with SLAs per severity.",
                    "🧪 Regular penetration testing validates your security controls.",
                    "📖 Subscribe to CISA KEV for known exploited vulnerabilities.",
                ],
            },
            "general": {
                "keywords": [],
                "responses": [
                    "🛡️ Security is defense in depth — no single control is enough.",
                    "📚 Stay updated on threats via NIST, CISA, and security blogs.",
                    "🧪 Practice in CTFs and labs to build real skills.",
                    "🤝 Security is everyone's responsibility — foster a security culture.",
                ],
            },
        }

    def chat(self, user_input: str) -> ChatResponse:
        user_lower = user_input.lower()
        best_topic = "general"
        best_score = 0
        for topic, data in self.knowledge_base.items():
            if topic == "general":
                continue
            score = sum(1 for kw in data["keywords"] if kw in user_lower)
            if score > best_score:
                best_score = score
                best_topic = topic
        response_text = random.choice(self.knowledge_base[best_topic]["responses"])
        follow_ups = self._generate_follow_ups(best_topic)
        self.conversation_history.append({"user": user_input, "bot": response_text, "topic": best_topic})
        return ChatResponse(
            response=response_text, topic=best_topic,
            confidence=min(0.5 + best_score * 0.15, 0.99),
            follow_ups=follow_ups,
        )

    def _generate_follow_ups(self, topic: str) -> List[str]:
        follow_ups = {
            "password": ["How do I create a strong passphrase?", "What's the best password manager?"],
            "network": ["How do I set up network segmentation?", "What ports should I block?"],
            "malware": ["How do I remove ransomware?", "What's the best antivirus?"],
            "phishing": ["How do I report phishing?", "What's spear phishing?"],
            "encryption": ["How does AES encryption work?", "What's end-to-end encryption?"],
            "firewall": ["How do I configure iptables?", "What's a WAF?"],
            "vulnerability": ["How do I scan for CVEs?", "What's CVSS scoring?"],
            "general": ["What are the OWASP Top 10?", "How do I start in cybersecurity?"],
        }
        return follow_ups.get(topic, [])

    def get_score(self) -> int:
        return self.score

    def get_statistics(self) -> Dict:
        topics = {}
        for msg in self.conversation_history:
            t = msg["topic"]
            topics[t] = topics.get(t, 0) + 1
        return {"total_messages": len(self.conversation_history), "topics_covered": topics}

    def __len__(self) -> int:
        return len(self.conversation_history)

    def __repr__(self) -> str:
        return f"CyberBot(name={self.name}, messages={len(self)})"
