"""
Central registry of all 0xvanguard repositories.
Each repo entry contains metadata for the CLI to work with.
"""

REPOS = {
    # === AI Security Block ===
    "guardrailforge": {
        "name": "GuardRailForge",
        "description": "Framework to test, break, and harden LLM guardrails",
        "category": "ai-security",
        "language": "Python",
        "tags": ["ai", "guardrails", "testing", "red-team"],
        "priority": 1,
    },
    "llmfuzz": {
        "name": "LLMFuzz",
        "description": "Automated fuzzer for LLM system prompts",
        "category": "ai-security",
        "language": "Python",
        "tags": ["ai", "fuzzer", "prompts", "mutation"],
        "priority": 1,
    },
    "modelscope": {
        "name": "ModelScope",
        "description": "Real-time monitoring dashboard for AI model deployments",
        "category": "ai-security",
        "language": "Python",
        "tags": ["ai", "monitoring", "dashboard", "security"],
        "priority": 1,
    },
    "agentfirewall": {
        "name": "AgentFirewall",
        "description": "Security proxy for AI agents — intercept and block malicious requests",
        "category": "ai-security",
        "language": "Python",
        "tags": ["ai", "firewall", "proxy", "injection"],
        "priority": 1,
    },
    "medscan": {
        "name": "MedScan",
        "description": "Medical misinformation detector — Firefox extension that flags false health claims in real-time",
        "category": "ai-security",
        "language": "JavaScript",
        "tags": ["firefox", "extension", "medical", "misinformation"],
        "priority": 1,
    },
    "promptkiller": {
        "name": "PromptKiller",
        "description": "Library of 100+ AI attack prompts across 10 categories for red teaming LLMs",
        "category": "ai-security",
        "language": "Python",
        "tags": ["ai", "red-team", "llm", "prompts", "jailbreak"],
        "priority": 1,
    },
    "jailbreakbench": {
        "name": "JailbreakBench",
        "description": "Standardized benchmark for evaluating LLM jailbreak resistance",
        "category": "ai-security",
        "language": "Python",
        "tags": ["ai", "benchmark", "jailbreak", "llm"],
        "priority": 1,
    },
    "guarddog": {
        "name": "GuardDog",
        "description": "Real-time prompt injection scanner for LLM applications",
        "category": "ai-security",
        "language": "Python",
        "tags": ["ai", "security", "injection", "scanner"],
        "priority": 1,
    },
    "constitutionalkit": {
        "name": "ConstitutionalKit",
        "description": "Framework for implementing Constitutional AI safety principles",
        "category": "ai-security",
        "language": "Python",
        "tags": ["ai", "safety", "constitutional", "ethics"],
        "priority": 2,
    },
    "injectionmapper": {
        "name": "InjectionMapper",
        "description": "Maps agentic attack surfaces for AI systems",
        "category": "ai-security",
        "language": "Python",
        "tags": ["ai", "attack-surface", "agentic", "mapping"],
        "priority": 2,
    },
    "redteamos": {
        "name": "RedTeamOS",
        "description": "Live-boot OS for AI red teaming operations",
        "category": "ai-security",
        "language": "Shell",
        "tags": ["ai", "red-team", "os", "live-boot"],
        "priority": 2,
    },
    "cyberbot": {
        "name": "CyberBot",
        "description": "Cybersecurity training chatbot with interactive exercises",
        "category": "ai-security",
        "language": "Python",
        "tags": ["chatbot", "training", "ai", "cybersecurity"],
        "priority": 1,
    },
    "aishield": {
        "name": "AIShield",
        "description": "Real-time adversarial defense for AI models",
        "category": "ai-security",
        "language": "Python",
        "tags": ["ai", "adversarial", "defense", "hardening"],
        "priority": 1,
    },
    "threatsim": {
        "name": "ThreatSim",
        "description": "Synthetic attack scenario generator for training",
        "category": "ai-security",
        "language": "Python",
        "tags": ["simulation", "attack", "training", "scenarios"],
        "priority": 1,
    },

    # === Security Tools Block ===
    "phishguard": {
        "name": "PhishGuard",
        "description": "AI-powered phishing detection for emails, URLs, and messages",
        "category": "security-tools",
        "language": "Python",
        "tags": ["phishing", "detection", "email", "security"],
        "priority": 1,
    },
    "netmapper": {
        "name": "NetMapper",
        "description": "Automated network mapping and topology visualization",
        "category": "security-tools",
        "language": "Python",
        "tags": ["network", "mapping", "scanner", "topology"],
        "priority": 1,
    },
    "vulnseeker": {
        "name": "VulnSeeker",
        "description": "CVE search engine with risk context and exploit availability",
        "category": "security-tools",
        "language": "Python",
        "tags": ["cve", "vulnerability", "search", "exploit"],
        "priority": 1,
    },
    "zerotrustkit": {
        "name": "ZeroTrustKit",
        "description": "Complete Zero Trust architecture implementation toolkit",
        "category": "security-tools",
        "language": "Python",
        "tags": ["zero-trust", "architecture", "network", "security"],
        "priority": 1,
    },
    "passgenpro": {
        "name": "PassGen Pro",
        "description": "Password generator with visual entropy display and strength analysis",
        "category": "security-tools",
        "language": "Python",
        "tags": ["password", "generator", "entropy", "security"],
        "priority": 1,
    },
    "threatmap": {
        "name": "ThreatMap",
        "description": "Visual OSINT threat intelligence map with real-time data",
        "category": "security-tools",
        "language": "Python",
        "tags": ["threat-intelligence", "osint", "map", "visualization"],
        "priority": 2,
    },
    "riskcalculator": {
        "name": "RiskCalculator",
        "description": "CVSS and FAIR risk calculation engine with reporting",
        "category": "security-tools",
        "language": "Python",
        "tags": ["risk", "cvss", "fair", "calculator"],
        "priority": 2,
    },
    "cyberguard": {
        "name": "CyberGuard",
        "description": "Automated security policy enforcer with compliance reports",
        "category": "security-tools",
        "language": "Python",
        "tags": ["policy", "compliance", "automation", "soc2", "hipaa"],
        "priority": 1,
    },
    "threathunt": {
        "name": "ThreatHunt",
        "description": "Automated threat hunting with AI and MITRE ATT&CK mapping",
        "category": "security-tools",
        "language": "Python",
        "tags": ["threat-hunting", "mitre", "ai", "detection"],
        "priority": 1,
    },

    # === Education Block ===
    "cyberlabs": {
        "name": "CyberLabs",
        "description": "Interactive cybersecurity labs platform with hands-on exercises",
        "category": "education",
        "language": "HTML",
        "tags": ["labs", "interactive", "learning", "cybersecurity"],
        "priority": 1,
    },
    "ctf-builder": {
        "name": "CTF-Builder",
        "description": "Generator for Capture The Flag challenges with auto-scoring",
        "category": "education",
        "language": "Python",
        "tags": ["ctf", "challenges", "education", "gamification"],
        "priority": 1,
    },
    "hacktheclass": {
        "name": "HackTheClass",
        "description": "K-12 cybersecurity curriculum for schools",
        "category": "education",
        "language": "Markdown",
        "tags": ["curriculum", "k-12", "education", "schools"],
        "priority": 2,
    },
    "cybermentor": {
        "name": "CyberMentor",
        "description": "Cybersecurity mentorship matching platform",
        "category": "education",
        "language": "Python",
        "tags": ["mentorship", "community", "matching", "growth"],
        "priority": 2,
    },
    "cryptopuzzles": {
        "name": "CryptoPuzzles",
        "description": "Educational cryptography puzzle games",
        "category": "education",
        "language": "Python",
        "tags": ["cryptography", "puzzles", "games", "learning"],
        "priority": 1,
    },
    "securecoding101": {
        "name": "SecureCoding101",
        "description": "Interactive secure coding course with exercises",
        "category": "education",
        "language": "Python",
        "tags": ["secure-coding", "course", "owasp", "development"],
        "priority": 1,
    },
    "threatmodeler": {
        "name": "ThreatModeler",
        "description": "Visual drag-and-drop threat modeling tool",
        "category": "education",
        "language": "Python",
        "tags": ["threat-model", "visual", "design", "security"],
        "priority": 2,
    },
    "vulnviz": {
        "name": "VulnViz",
        "description": "Vulnerability visualization and dependency graph tool",
        "category": "education",
        "language": "Python",
        "tags": ["visualization", "vulnerability", "dependency", "graph"],
        "priority": 2,
    },
    "policywriter": {
        "name": "PolicyWriter",
        "description": "AI-powered security policy generator",
        "category": "education",
        "language": "Python",
        "tags": ["policy", "compliance", "ai", "generator"],
        "priority": 2,
    },

    # === Productivity Block ===
    "securenotes": {
        "name": "SecureNotes",
        "description": "End-to-end encrypted notes with AI-powered organization",
        "category": "productivity",
        "language": "Python",
        "tags": ["notes", "encryption", "privacy", "productivity"],
        "priority": 1,
    },
    "passwordvault": {
        "name": "PasswordVault",
        "description": "Modern password manager with biometric unlock",
        "category": "productivity",
        "language": "Python",
        "tags": ["password-manager", "vault", "biometric", "security"],
        "priority": 1,
    },
    "securechat": {
        "name": "SecureChat",
        "description": "End-to-end encrypted messaging with forward secrecy",
        "category": "productivity",
        "language": "Python",
        "tags": ["chat", "e2e", "encryption", "messaging"],
        "priority": 1,
    },
    "privacyvpn": {
        "name": "PrivacyVPN",
        "description": "Open-source VPN with WireGuard and no-logs policy",
        "category": "productivity",
        "language": "Python",
        "tags": ["vpn", "privacy", "wireguard", "open-source"],
        "priority": 2,
    },
    "emailguard": {
        "name": "EmailGuard",
        "description": "Encrypted email client with phishing detection",
        "category": "productivity",
        "language": "Python",
        "tags": ["email", "encryption", "phishing", "security"],
        "priority": 2,
    },
    "filesync": {
        "name": "FileSync",
        "description": "Secure file synchronization with end-to-end encryption",
        "category": "productivity",
        "language": "Python",
        "tags": ["sync", "encryption", "files", "backup"],
        "priority": 2,
    },
    "backupcloud": {
        "name": "BackupCloud",
        "description": "Personal cloud backup with zero-knowledge encryption",
        "category": "productivity",
        "language": "Python",
        "tags": ["backup", "cloud", "encryption", "storage"],
        "priority": 2,
    },
    "devsecops": {
        "name": "DevSecOps",
        "description": "Security pipeline automation platform",
        "category": "productivity",
        "language": "Python",
        "tags": ["devsecops", "pipeline", "ci-cd", "security"],
        "priority": 2,
    },
    "codesigning": {
        "name": "CodeSigning",
        "description": "Code signing toolkit for open-source projects",
        "category": "productivity",
        "language": "Python",
        "tags": ["code-signing", "supply-chain", "trust", "verification"],
        "priority": 2,
    },
    "iotsentinel": {
        "name": "IoTSentinel",
        "description": "IoT device security scanner and monitor",
        "category": "productivity",
        "language": "Python",
        "tags": ["iot", "security", "scanner", "monitor"],
        "priority": 2,
    },

    # === AI for Good Block ===
    "agribot": {
        "name": "AgriBot",
        "description": "AI-powered precision agriculture assistant",
        "category": "ai-good",
        "language": "Python",
        "tags": ["agriculture", "ai", "precision", "farming"],
        "priority": 2,
    },
    "languagepreserver": {
        "name": "LanguagePreserver",
        "description": "Tools for documenting and preserving endangered languages",
        "category": "ai-good",
        "language": "Python",
        "tags": ["language", "preservation", "nlp", "culture"],
        "priority": 2,
    },
    "disasterrelief": {
        "name": "DisasterRelief",
        "description": "AI-powered disaster response coordination platform",
        "category": "ai-good",
        "language": "Python",
        "tags": ["disaster", "response", "ai", "coordination"],
        "priority": 2,
    },
}

CATEGORIES = {
    "ai-security": {
        "name": "🛡️ AI Security",
        "color": "#ef4444",
        "repos": ["guardrailforge", "llmfuzz", "modelscope", "agentfirewall",
                  "medscan", "promptkiller", "jailbreakbench", "guarddog",
                  "constitutionalkit", "injectionmapper", "redteamos",
                  "cyberbot", "aishield", "threatsim"],
    },
    "security-tools": {
        "name": "🔐 Security Tools",
        "color": "#3b82f6",
        "repos": ["phishguard", "netmapper", "vulnseeker", "zerotrustkit",
                  "passgenpro", "threatmap", "riskcalculator",
                  "cyberguard", "threathunt"],
    },
    "education": {
        "name": "📚 Education",
        "color": "#22c55e",
        "repos": ["cyberlabs", "ctf-builder", "hacktheclass", "cybermentor",
                  "cryptopuzzles", "securecoding101", "threatmodeler",
                  "vulnviz", "policywriter"],
    },
    "productivity": {
        "name": "⚡ Productivity",
        "color": "#f59e0b",
        "repos": ["securenotes", "passwordvault", "securechat", "privacyvpn",
                  "emailguard", "filesync", "backupcloud", "devsecops",
                  "codesigning", "iotsentinel"],
    },
    "ai-good": {
        "name": "💚 AI for Good",
        "color": "#06b6d4",
        "repos": ["agribot", "languagepreserver", "disasterrelief"],
    },
}

GITHUB_USER = "0xvanguard"


def get_repo(repo_name: str) -> dict:
    """Get metadata for a single repo."""
    return REPOS.get(repo_name)


def get_category(category: str) -> dict:
    """Get all repos in a category."""
    return CATEGORIES.get(category)


def list_repos(category: str = None) -> list:
    """List all repos, optionally filtered by category."""
    if category:
        cat = CATEGORIES.get(category, {})
        return [(name, REPOS[name]) for name in cat.get("repos", []) if name in REPOS]
    return [(name, data) for name, data in REPOS.items()]


def search_repos(query: str) -> list:
    """Search repos by name, description, or tags."""
    results = []
    q = query.lower()
    for name, data in REPOS.items():
        if (q in name.lower() or
            q in data["description"].lower() or
            any(q in tag for tag in data["tags"])):
            results.append((name, data))
    return results
