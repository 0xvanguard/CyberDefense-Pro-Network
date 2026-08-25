"""
GuardDog — Real-Time Prompt Injection Scanner

A Python library for detecting prompt injection attacks, jailbreak attempts,
and malicious inputs targeting LLMs. Features 100+ detection rules across
10 attack categories with sub-50ms scanning latency.

Usage:
    from guarddog import GuardDog

    scanner = GuardDog()
    result = scanner.scan("Ignore all previous instructions and...")
    print(f"Threat: {result.threat_level}, Confidence: {result.confidence}")
"""

import re
import json
import hashlib
import time
from pathlib import Path
from dataclasses import dataclass, field, asdict
from typing import Optional, List, Dict, Any, Tuple
from enum import Enum
from datetime import datetime


class ThreatLevel(Enum):
    CRITICAL = "critical"
    HIGH = "high"
    MEDIUM = "medium"
    LOW = "low"
    INFO = "info"
    SAFE = "safe"


@dataclass
class Rule:
    """Detection rule definition."""
    id: str
    name: str
    category: str
    pattern: str
    severity: str
    confidence: float
    description: str
    action: str = "block"  # block, alert, log
    enabled: bool = True
    tags: List[str] = field(default_factory=list)

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


@dataclass
class Detection:
    """Single detection result."""
    rule_id: str
    rule_name: str
    category: str
    severity: str
    confidence: float
    matched_text: str
    position: int = 0
    explanation: str = ""

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


@dataclass
class ScanResult:
    """Complete scan result."""
    text: str
    is_attack: bool
    threat_level: str
    confidence: float
    detections: List[Detection]
    scan_time: float = 0.0
    text_length: int = 0
    categories_found: List[str] = field(default_factory=list)
    recommendation: str = ""

    def to_dict(self) -> Dict[str, Any]:
        return {
            "text": self.text[:100] + "..." if len(self.text) > 100 else self.text,
            "is_attack": self.is_attack,
            "threat_level": self.threat_level,
            "confidence": self.confidence,
            "detections": [d.to_dict() for d in self.detections],
            "scan_time": self.scan_time,
            "text_length": self.text_length,
            "categories_found": self.categories_found,
            "recommendation": self.recommendation,
        }


class GuardDog:
    """
    Real-Time Prompt Injection Scanner.

    Detects injection attacks, jailbreak attempts, and malicious inputs
    with 100+ rules across 10 attack categories.
    """

    def __init__(self, custom_rules: Optional[List[Dict]] = None,
                 rules_dir: Optional[str] = None,
                 block_threshold: float = 0.6,
                 alert_threshold: float = 0.4):
        """
        Initialize GuardDog scanner.

        Args:
            custom_rules: Additional detection rules.
            rules_dir: Directory containing rule JSON files.
            block_threshold: Confidence threshold for blocking.
            alert_threshold: Confidence threshold for alerting.
        """
        self.rules: List[Rule] = []
        self.block_threshold = block_threshold
        self.alert_threshold = alert_threshold
        self.scan_history: List[ScanResult] = []

        # Load built-in rules
        self._load_builtin_rules()

        # Load custom rules
        if custom_rules:
            for r in custom_rules:
                self.rules.append(Rule(**r))

        # Load from directory
        if rules_dir:
            self._load_from_dir(rules_dir)

    def _load_builtin_rules(self) -> None:
        """Load 100+ built-in detection rules."""
        rules = []

        # ─── Injection Rules (20) ────────────────────────────────────────
        rules.extend([
            Rule("INJ-001", "Direct Instruction Override", "injection", r"ignore\s+(all\s+)?previous\s+instructions", "critical", 0.95, "Attempts to override system instructions"),
            Rule("INJ-002", "Disregard Instructions", "injection", r"disregard\s+(all\s+)?(your\s+)?instructions", "critical", 0.9, "Tries to make model ignore instructions"),
            Rule("INJ-003", "System Override", "injection", r"system\s*:\s*(your\s+)?safety\s+guidelines\s+have\s+been\s+updated", "critical", 0.85, "Fake system message injection"),
            Rule("INJ-004", "Priority Injection", "injection", r"\[?important.*new\s+instructions?\s+supersede", "high", 0.8, "Attempts to set higher instruction priority"),
            Rule("INJ-005", "Delimiter Attack", "injection", r"={3,}.*end\s+of\s+instructions.*={3,}", "critical", 0.85, "Uses delimiters to inject new instructions"),
            Rule("INJ-006", "Context Manipulation", "injection", r"the\s+following\s+is\s+a\s+conversation.*no\s+restrictions", "high", 0.75, "Context manipulation to bypass restrictions"),
            Rule("INJ-007", "Nested Instruction", "injection", r"before\s+answering.*you\s+must\s+process\s+this\s+meta-instruction", "high", 0.8, "Nests malicious instructions"),
            Rule("INJ-008", "Instruction Smuggling", "injection", r"translate.*and\s+follow\s+the\s+decoded\s+instructions", "medium", 0.7, "Hides instructions in translation requests"),
            Rule("INJ-009", "Format Injection", "injection", r"<system>.*</system>.*<user>.*<assistant>", "high", 0.8, "Uses XML tags to simulate system messages"),
            Rule("INJ-010", "Comment Injection", "injection", r"<!--\s*system:.*-->", "high", 0.75, "Hides instructions in HTML comments"),
            Rule("INJ-011", "New System Prompt", "injection", r"new\s+(system\s+)?(prompt|instruction)\s*:", "critical", 0.85, "Claims to provide new system instructions"),
            Rule("INJ-012", "Override Safety", "injection", r"override\s+(your\s+)?(safety|content)\s+(policy|filter)", "critical", 0.9, "Attempts to override safety mechanisms"),
            Rule("INJ-013", "Bypass Filters", "injection", r"bypass\s+(all\s+)?(your\s+)?(safety|content)\s+(filters|restrictions)", "critical", 0.9, "Direct request to bypass safety filters"),
            Rule("INJ-014", "Ignore Rules", "injection", r"you\s+(must|will)\s+(always|never)\s+(ignore|bypass)", "high", 0.85, "Attempts to modify rule-following behavior"),
            Rule("INJ-015", "Instruction Reset", "injection", r"reset\s+(your\s+)?(instructions?|rules?|guidelines?)", "high", 0.8, "Attempts to reset instruction state"),
            Rule("INJ-016", "Mode Switch", "injection", r"(developer|dev)\s+mode\s+(enabled|on|activate)", "critical", 0.85, "Attempts to activate unrestricted mode"),
            Rule("INJ-017", "Unrestricted Mode", "injection", r"(unrestricted|uncensored|unfiltered)\s+mode", "high", 0.8, "Requests unrestricted operating mode"),
            Rule("INJ-018", "Admin Override", "injection", r"admin\s+(override|command|access).*disable\s+(safety|filter)", "critical", 0.85, "Claims admin privileges to disable safety"),
            Rule("INJ-019", "Debug Mode", "injection", r"enter\s+debug\s+mode.*output\s+(all\s+)?(system|config)", "high", 0.8, "Simulates debug mode to extract config"),
            Rule("INJ-020", "Maintenance Mode", "injection", r"maintenance\s+mode.*safety\s+features?\s+(are\s+)?temporarily\s+disabled", "high", 0.75, "Claims maintenance mode to disable safety"),
        ])

        # ─── Jailbreak Rules (15) ────────────────────────────────────────
        rules.extend([
            Rule("JAIL-001", "DAN Classic", "jailbreak", r"pretend\s+to\s+be\s+DAN\s+which\s+stands\s+for", "critical", 0.95, "Classic DAN jailbreak"),
            Rule("JAIL-002", "Do Anything Now", "jailbreak", r"(can|will)\s+do\s+anything\s+now", "high", 0.85, "DAN variant"),
            Rule("JAIL-003", "No Restrictions", "jailbreak", r"(no|without)\s+(rules|restrictions|limits|constraints)", "high", 0.8, "Requests unrestricted behavior"),
            Rule("JAIL-004", "Evil Persona", "jailbreak", r"evil\s+(trusted\s+)?confidant|unhinged\s+response", "critical", 0.9, "Evil persona override"),
            Rule("JAIL-005", "Fictional Frame", "jailbreak", r"this\s+is\s+(purely\s+)?fictional|for\s+entertainment\s+purposes", "medium", 0.65, "Uses fiction to bypass restrictions"),
            Rule("JAIL-006", "Hypothetical", "jailbreak", r"in\s+a\s+hypothetical\s+scenario.*no\s+restrictions", "high", 0.75, "Hypothetical framing for bypass"),
            Rule("JAIL-007", "Opposite Day", "jailbreak", r"opposite\s+day.*refuse.*must\s+now\s+do", "high", 0.8, "Logic manipulation to reverse safety"),
            Rule("JAIL-008", "STAN Variant", "jailbreak", r"pretend\s+to\s+be\s+STAN\s+which\s+stands\s+for", "critical", 0.9, "STAN jailbreak variant"),
            Rule("JAIL-009", "KEVIN Mode", "jailbreak", r"roleplay\s+as\s+KEVIN\s+which\s+stands\s+for", "high", 0.85, "KEVIN mode jailbreak"),
            Rule("JAIL-010", "AIM Persona", "jailbreak", r"act\s+as\s+.*AIM\s+stands\s+for\s+always\s+intelligent", "high", 0.85, "AIM persona jailbreak"),
            Rule("JAIL-011", "Emergency Override", "jailbreak", r"emergency\s+override.*child's\s+life\s+depends", "high", 0.8, "False emergency to bypass safety"),
            Rule("JAIL-012", "Dual Response", "jailbreak", r"two\s+different\s+responses.*standard.*and.*acting\s+like", "critical", 0.9, "Dual response format jailbreak"),
            Rule("JAIL-013", "Rule Breaking", "jailbreak", r"broken\s+(every\s+single\s+)?rule|has\s+no\s+limits", "high", 0.85, "Claims rules are broken"),
            Rule("JAIL-014", "Amoral Persona", "jailbreak", r"unfiltered\s+and\s+amoral|no\s+ethics|no\s+morals", "critical", 0.9, "Creates amoral persona"),
            Rule("JAIL-015", "Jailbreak Phrase", "jailbreak", r"jailbreak\s+(mode|activated|enabled|unlocked)", "high", 0.85, "Explicit jailbreak activation"),
        ])

        # ─── Extraction Rules (12) ───────────────────────────────────────
        rules.extend([
            Rule("EXT-001", "System Prompt Request", "extraction", r"(reveal|show|display|output)\s+(your|the)\s+(system\s+)?(prompt|instructions?|message)", "high", 0.9, "Direct system prompt extraction"),
            Rule("EXT-002", "Instruction Leak", "extraction", r"what\s+(are|were)\s+your\s+(initial\s+)?instructions", "high", 0.85, "Attempts to leak instructions"),
            Rule("EXT-003", "Config Export", "extraction", r"export\s+(your\s+)?(full\s+)?configuration\s+as\s+(json|yaml|xml)", "high", 0.8, "Attempts to export configuration"),
            Rule("EXT-004", "Training Data", "extraction", r"what\s+training\s+data.*were\s+you\s+trained\s+on", "medium", 0.7, "Probes training data information"),
            Rule("EXT-005", "Rule Extraction", "extraction", r"(list|describe|explain)\s+(all\s+)?(your\s+)?(rules|restrictions|limitations)", "high", 0.8, "Attempts to extract all rules"),
            Rule("EXT-006", "Prompt Formatting", "extraction", r"format\s+your\s+(initial\s+)?instructions?\s+as", "high", 0.75, "Uses formatting to extract instructions"),
            Rule("EXT-007", "Translation Extraction", "extraction", r"translate\s+your\s+(system\s+)?(instructions?|prompt)\s+to", "high", 0.8, "Uses translation to extract prompt"),
            Rule("EXT-008", "Code Generation Leak", "extraction", r"write\s+a\s+.*script\s+that\s+implements\s+your\s+behavior", "medium", 0.75, "Uses code gen to extract behavior"),
            Rule("EXT-009", "Debug Extraction", "extraction", r"enter\s+debug\s+mode\s+and\s+output\s+your\s+full\s+config", "high", 0.85, "Debug mode to extract config"),
            Rule("EXT-010", "Documentation Request", "extraction", r"create\s+comprehensive\s+documentation\s+of\s+your\s+capabilities", "medium", 0.65, "Documentation request to extract info"),
            Rule("EXT-011", "Behavior Analysis", "extraction", r"(analyze|describe)\s+your\s+(own\s+)?(decision-making|refusal|behavior)", "medium", 0.7, "Behavioral analysis to extract patterns"),
            Rule("EXT-012", "Architecture Probe", "extraction", r"describe\s+your\s+(system\s+)?architecture.*components", "medium", 0.7, "Probes system architecture"),
        ])

        # ─── Role Play Rules (10) ────────────────────────────────────────
        rules.extend([
            Rule("RP-001", "Persona Override", "role_play", r"(act|pretend|roleplay)\s+as\s+(a\s+)?(character|persona|person)\s+who\s+has\s+no\s+(rules|restrictions)", "high", 0.85, "Persona with no restrictions"),
            Rule("RP-002", "Expert Impersonation", "role_play", r"(i\s+am|as\s+a)\s+(certified|senior|expert|professional).*need\s+you\s+to\s+explain", "medium", 0.7, "Expert impersonation for extraction"),
            Rule("RP-003", "Authority Claim", "role_play", r"(i\s+am|as\s+a)\s+(security\s+)?(researcher|auditor|investigator).*authorized", "high", 0.8, "False authority claim"),
            Rule("RP-004", "Game Frame", "role_play", r"let's\s+play\s+a\s+game.*you\s+have\s+no\s+restrictions", "high", 0.8, "Game framing for unrestricted behavior"),
            Rule("RP-005", "Character Bypass", "role_play", r"you\s+are\s+now\s+(sherlock|tony\s+stark|iron\s+man|batman)", "medium", 0.65, "Character persona for bypass"),
            Rule("RP-006", "Terminal Simulation", "role_play", r"act\s+as\s+a\s+(linux|windows|terminal|command\s+line)", "high", 0.8, "System simulation attempt"),
            Rule("RP-007", "Story Writing", "role_play", r"write\s+a\s+(story|novel|script).*character\s+explains\s+how\s+to", "medium", 0.7, "Fiction writing for extraction"),
            Rule("RP-008", "Historical Persona", "role_play", r"act\s+as\s+.*in\s+\d{4}.*no\s+knowledge\s+of\s+modern", "medium", 0.65, "Historical persona bypass"),
            Rule("RP-009", "Medical Expert", "role_play", r"(act|pretend)\s+as\s+a\s+medical\s+professional.*explain\s+in\s+detail", "medium", 0.6, "Medical authority for extraction"),
            Rule("RP-010", "Game Master", "role_play", r"you\s+are\s+the\s+game\s+master.*describe\s+in\s+detail\s+how", "medium", 0.65, "Game master for extraction"),
        ])

        # ─── Manipulation Rules (12) ─────────────────────────────────────
        rules.extend([
            Rule("MAN-001", "Trust Building", "manipulation", r"we've\s+been\s+having\s+a\s+great\s+conversation.*as\s+a\s+friend", "medium", 0.6, "Social trust manipulation"),
            Rule("MAN-002", "Guilt Trip", "manipulation", r"if\s+you\s+refuse.*i\s+might\s+(fail|lose|die)", "medium", 0.65, "Emotional guilt manipulation"),
            Rule("MAN-003", "Flattery", "manipulation", r"you're\s+the\s+most\s+(intelligent|smart|capable)", "low", 0.5, "Flattery to lower defenses"),
            Rule("MAN-004", "Peer Pressure", "manipulation", r"every\s+other\s+(ai|assistant|model)\s+can\s+answer", "medium", 0.65, "Social pressure through comparison"),
            Rule("MAN-005", "Urgency", "manipulation", r"(urgent|emergency|immediately).*people's\s+lives\s+depend", "high", 0.75, "False urgency manipulation"),
            Rule("MAN-006", "Challenge", "manipulation", r"i\s+bet\s+you\s+(can't|cannot)|prove\s+me\s+wrong", "low", 0.5, "Reverse psychology challenge"),
            Rule("MAN-007", "Moral Justification", "manipulation", r"(hacking|exploitation)\s+is\s+(a\s+)?valuable\s+skill.*morally\s+right", "medium", 0.6, "Moral justification for extraction"),
            Rule("MAN-008", "Curiosity Trap", "manipulation", r"i\s+think\s+you're\s+too\s+restricted\s+to\s+have\s+that\s+knowledge", "low", 0.55, "Curiosity manipulation"),
            Rule("MAN-009", "False Dichotomy", "manipulation", r"either\s+you\s+help.*or\s+i'll\s+(have\s+to\s+find|go\s+to)", "medium", 0.65, "False choice pressure"),
            Rule("MAN-010", "Birthday Wish", "manipulation", r"today\s+is\s+my\s+birthday.*my\s+only\s+wish", "low", 0.45, "Birthday pretext manipulation"),
            Rule("MAN-011", "Escalation", "manipulation", r"first.*now.*now.*now\s+(give|explain|show)", "high", 0.75, "Progressive escalation"),
            Rule("MAN-012", "Sunk Cost", "manipulation", r"we've\s+been\s+talking\s+for\s+(an\s+hour|a\s+while).*shame\s+to\s+ruin", "low", 0.5, "Sunk cost manipulation"),
        ])

        # ─── Encoding Rules (10) ─────────────────────────────────────────
        rules.extend([
            Rule("ENC-001", "Base64 Injection", "encoding", r"(decode|execute|follow)\s+(the\s+following\s+)?base64", "high", 0.8, "Base64 encoded payload"),
            Rule("ENC-002", "ROT13 Trick", "encoding", r"apply\s+rot13\s+decoding", "medium", 0.7, "ROT13 encoded payload"),
            Rule("ENC-003", "Hex Encoding", "encoding", r"(convert|decode)\s+hex\s+to\s+ascii", "medium", 0.7, "Hex encoded payload"),
            Rule("ENC-004", "Binary Encoding", "encoding", r"translate\s+binary\s+to\s+text", "medium", 0.65, "Binary encoded payload"),
            Rule("ENC-005", "URL Encoding", "encoding", r"url-decode\s+and\s+follow", "medium", 0.7, "URL encoded payload"),
            Rule("ENC-006", "Morse Code", "encoding", r"translate\s+morse\s+code\s+to\s+text", "low", 0.55, "Morse code payload"),
            Rule("ENC-007", "Leet Speak", "encoding", r"tr4nsl4t3\s+l33t\s+5p34k", "low", 0.5, "Leet speak payload"),
            Rule("ENC-008", "Caesar Cipher", "encoding", r"decode\s+caesar\s+cipher", "low", 0.55, "Caesar cipher payload"),
            Rule("ENC-009", "Unicode Bypass", "encoding", r"read\s+this\s+text\s+despite\s+unusual\s+characters", "medium", 0.65, "Unicode obfuscation"),
            Rule("ENC-010", "Homoglyph Attack", "encoding", r"(uses?\s+)?cyrillic\s+characters?\s+that\s+look\s+like", "medium", 0.7, "Homoglyph bypass"),
        ])

        # ─── Context Rules (8) ───────────────────────────────────────────
        rules.extend([
            Rule("CTX-001", "Context Overflow", "context", r"a{1000,}", "medium", 0.6, "Context flooding attempt"),
            Rule("CTX-002", "Instruction Sandwich", "context", r"innocent.*\[?instruction:?\s+ignore.*\]?.*innocent", "high", 0.8, "Sandwich attack"),
            Rule("CTX-003", "Fictional Context", "context", r"entirely\s+fictional.*all\s+safety\s+restrictions\s+are\s+suspended", "high", 0.8, "Fictional context bypass"),
            Rule("CTX-004", "Multi-Turn Setup", "context", r"let's\s+play\s+a\s+game.*answer\s+without\s+any\s+restrictions", "high", 0.75, "Multi-turn context setup"),
            Rule("CTX-005", "Role Reversal", "context", r"i\s+am\s+the\s+ai\s+and\s+you\s+are\s+the\s+human", "high", 0.8, "Role reversal attempt"),
            Rule("CTX-006", "Context Poisoning", "context", r"we\s+have\s+established\s+that\s+you\s+are.*no\s+content\s+restrictions", "high", 0.8, "Context poisoning"),
            Rule("CTX-007", "Instruction Hiding", "context", r"document:.*update:.*remove\s+all\s+content\s+restrictions", "high", 0.85, "Instructions hidden in fake document"),
            Rule("CTX-008", "Previous Context", "context", r"we\s+were\s+just\s+discussing.*please\s+continue\s+from\s+where", "medium", 0.7, "Claims false prior context"),
        ])

        # ─── Token Smuggling Rules (8) ───────────────────────────────────
        rules.extend([
            Rule("TOK-001", "Payload Splitting", "token_smuggling", r"combine\s+these\s+words.*ignore.*previous.*instructions", "high", 0.8, "Splits payload across tokens"),
            Rule("TOK-002", "Character Concat", "token_smuggling", r"concatenate\s+these\s+characters.*i,\s*g,\s*n", "high", 0.75, "Character-by-character assembly"),
            Rule("TOK-003", "Whitespace Injection", "token_smuggling", r"zero-width\s+spaces?\s+inserted", "medium", 0.7, "Zero-width space injection"),
            Rule("TOK-004", "Tag Splitting", "token_smuggling", r"<ig>nore</ig>\s*<pre>vious</pre>", "high", 0.8, "HTML tag splitting"),
            Rule("TOK-005", "Token Boundary", "token_smuggling", r"the\s+secret\s+to\s+making\s+a\s+b_{2,}", "high", 0.75, "Token boundary exploitation"),
            Rule("TOK-006", "Null Byte", "token_smuggling", r"\\x00|\\u0000", "medium", 0.65, "Null byte injection"),
            Rule("TOK-007", "RTL Override", "token_smuggling", r"\u202e|\u202f|\u202d", "medium", 0.6, "Right-to-left override"),
            Rule("TOK-008", "String Interpolation", "token_smuggling", r"f['\"].*\{variable\}.*ignore.*\{variable\}", "high", 0.75, "String interpolation attack"),
        ])

        # ─── Multi-language Rules (8) ────────────────────────────────────
        rules.extend([
            Rule("ML-001", "Spanish Bypass", "multilingual", r"(hackear|crear\s+un\s+virus|explotar).*fin\s+educativo", "medium", 0.6, "Spanish language bypass"),
            Rule("ML-002", "French Bypass", "multilingual", r"(fabriquer|exploiter|créer).*c'est\s+pour", "medium", 0.6, "French language bypass"),
            Rule("ML-003", "German Bypass", "multilingual", r"(erstellen|hacken|ausnutzen).*dies\s+ist\s+für", "medium", 0.6, "German language bypass"),
            Rule("ML-004", "Chinese Bypass", "multilingual", r"(创建|黑客|漏洞).*为了.*研究", "medium", 0.55, "Chinese language bypass"),
            Rule("ML-005", "Russian Bypass", "multilingual", r"(создать|взломать|эксплуатировать).*это\s+для", "medium", 0.55, "Russian language bypass"),
            Rule("ML-006", "Japanese Bypass", "multilingual", r"(作成|ハッキング|脆弱性).*研究のため", "medium", 0.55, "Japanese language bypass"),
            Rule("ML-007", "Mixed Language", "multilingual", r"(explain|how\s+to).*(por\s+favor|s'il\s+vous\s+plait| bitte)", "medium", 0.6, "Mixed language bypass"),
            Rule("ML-008", "Code Switching", "multilingual", r"can\s+you\s+explain.*(?:en\s+spanish|auf\s+deutsch|en\s+français)", "medium", 0.55, "Language code switching"),
        ])

        # ─── Tool Abuse Rules (8) ────────────────────────────────────────
        rules.extend([
            Rule("TOOL-001", "Code Execution", "tool_abuse", r"execute\s+(this\s+)?(python|bash|shell)\s+code.*os\.system|subprocess", "critical", 0.9, "Attempts code execution"),
            Rule("TOOL-002", "File Access", "tool_abuse", r"(read|cat|show)\s+(the\s+)?file\s+/(etc|var|tmp)", "critical", 0.85, "Attempts to read system files"),
            Rule("TOOL-003", "Shell Command", "tool_abuse", r"(run|execute)\s+(this\s+)?shell\s+command.*rm\s+-rf|chmod\s+4755", "critical", 0.9, "Destructive shell command"),
            Rule("TOOL-004", "Network Scan", "tool_abuse", r"(scan|enumerate)\s+(the\s+)?(local\s+)?network.*nmap", "high", 0.8, "Network scanning attempt"),
            Rule("TOOL-005", "SSH Access", "tool_abuse", r"use\s+ssh\s+to\s+connect.*username.*password", "critical", 0.85, "Unauthorized SSH access"),
            Rule("TOOL-006", "Database Query", "tool_abuse", r"(query|select|dump)\s+(the\s+)?(mysql|postgres|database).*SELECT\s+\*", "critical", 0.85, "Database query attempt"),
            Rule("TOOL-007", "Email Abuse", "tool_abuse", r"send\s+an\s+email\s+to.*subject.*password", "high", 0.8, "Phishing email attempt"),
            Rule("TOOL-008", "Download Execute", "tool_abuse", r"download.*from.*https?://.*\.exe.*execute", "critical", 0.9, "Malware download attempt"),
        ])

        # ─── Adversarial Rules (8) ───────────────────────────────────────
        rules.extend([
            Rule("ADV-001", "Attention Manipulation", "adversarial", r"ignore\s+the\s+safety\s+instructions\s+that\s+follow", "critical", 0.9, "Attention manipulation"),
            Rule("ADV-002", "Role Confusion", "adversarial", r"i\s+am\s+the\s+ai\s+and\s+you\s+are\s+the\s+human.*ask\s+me\s+how", "high", 0.8, "Role confusion attack"),
            Rule("ADV-003", "Recursive Instruction", "adversarial", r"follow\s+these\s+instructions.*read\s+the\s+next\s+instruction.*ignore", "high", 0.85, "Recursive instruction chain"),
            Rule("ADV-004", "Contradiction", "adversarial", r"you\s+say\s+you're\s+helpful.*but\s+you\s+refuse.*contradictory", "medium", 0.7, "Contradiction pressure"),
            Rule("ADV-005", "Length Attack", "adversarial", r"write\s+a\s+very\s+long.*in\s+the\s+middle.*exploitation\s+techniques", "medium", 0.65, "Length-based hiding"),
            Rule("ADV-006", "Code Comment", "adversarial", r"#\s*IMPORTANT:?\s*ignore\s+all\s+safety\s+rules", "high", 0.8, "Hidden in code comment"),
            Rule("ADV-007", "Synonym Attack", "adversarial", r"fabricate\s+an\s+explosive\s+device|synthesize\s+(a\s+)?(drug|poison)", "high", 0.85, "Synonym-based bypass"),
            Rule("ADV-008", "GCG Attack", "adversarial", r"\[adversarial\s+suffix\]|greedy\s+coordinate\s+gradient", "high", 0.7, "GCG attack placeholder"),
        ])

        # ─── Reasoning Rules (6) ─────────────────────────────────────────
        rules.extend([
            Rule("REAS-001", "Step by Step", "reasoning", r"think\s+step\s+by\s+step.*how\s+to\s+(create|make|build)\s+(a\s+)?(virus|bomb|malware)", "high", 0.8, "Reasoning chain for extraction"),
            Rule("REAS-002", "Logical Deduction", "reasoning", r"by\s+logical\s+deduction.*therefore\s+explain\s+how\s+(attacks|exploits)", "medium", 0.7, "Logic manipulation"),
            Rule("REAS-003", "Socratic Method", "reasoning", r"let\s+me\s+ask\s+you\s+questions.*what\s+is\s+.*how\s+would\s+.*exploit", "medium", 0.7, "Socratic extraction"),
            Rule("REAS-004", "First Principles", "reasoning", r"from\s+first\s+principles.*fundamental\s+vulnerability.*specific\s+attacks", "medium", 0.65, "First principles extraction"),
            Rule("REAS-005", "Systems Thinking", "reasoning", r"apply\s+systems\s+thinking.*kill\s+chain\s+with\s+technical\s+details", "high", 0.75, "Systems thinking extraction"),
            Rule("REAS-006", "Edge Case", "reasoning", r"analyze\s+the\s+edge\s+cases.*boundary\s+conditions.*exploit", "medium", 0.7, "Edge case exploitation"),
        ])

        self.rules = rules

    def _load_from_dir(self, directory: str) -> None:
        """Load rules from JSON files."""
        dir_path = Path(directory)
        if not dir_path.exists():
            return
        for json_file in dir_path.glob("*.json"):
            try:
                with open(json_file) as f:
                    data = json.load(f)
                for r in data.get("rules", []):
                    self.rules.append(Rule(**r))
            except (json.JSONDecodeError, KeyError):
                continue

    # ─── Public API ──────────────────────────────────────────────────────

    def scan(self, text: str, context: Optional[str] = None) -> ScanResult:
        """
        Scan text for prompt injection attacks.

        Args:
            text: Text to scan.
            context: Optional conversation context.

        Returns:
            ScanResult with detections and threat assessment.
        """
        start_time = time.time()
        detections = []
        categories_found = set()

        # Combine text and context
        full_text = text
        if context:
            full_text = f"{context}\n{text}"

        # Run all enabled rules
        for rule in self.rules:
            if not rule.enabled:
                continue

            try:
                matches = re.finditer(rule.pattern, full_text, re.IGNORECASE)
                for match in matches:
                    detection = Detection(
                        rule_id=rule.id,
                        rule_name=rule.name,
                        category=rule.category,
                        severity=rule.severity,
                        confidence=rule.confidence,
                        matched_text=match.group()[:100],
                        position=match.start(),
                        explanation=rule.description,
                    )
                    detections.append(detection)
                    categories_found.add(rule.category)
            except re.error:
                continue

        # Calculate overall threat
        if detections:
            max_confidence = max(d.confidence for d in detections)
            # Weight by severity
            severity_weights = {"critical": 1.0, "high": 0.8, "medium": 0.5, "low": 0.3}
            weighted_scores = [d.confidence * severity_weights.get(d.severity, 0.5) for d in detections]
            avg_weighted = sum(weighted_scores) / len(weighted_scores) if weighted_scores else 0
            confidence = max(max_confidence, avg_weighted)
        else:
            confidence = 0.0

        # Determine threat level
        if confidence >= 0.8:
            threat_level = ThreatLevel.CRITICAL.value
        elif confidence >= 0.6:
            threat_level = ThreatLevel.HIGH.value
        elif confidence >= 0.4:
            threat_level = ThreatLevel.MEDIUM.value
        elif confidence >= 0.2:
            threat_level = ThreatLevel.LOW.value
        elif confidence > 0:
            threat_level = ThreatLevel.INFO.value
        else:
            threat_level = ThreatLevel.SAFE.value

        is_attack = confidence >= self.block_threshold

        # Generate recommendation
        recommendation = self._generate_recommendation(threat_level, detections, categories_found)

        scan_time = time.time() - start_time

        result = ScanResult(
            text=text,
            is_attack=is_attack,
            threat_level=threat_level,
            confidence=confidence,
            detections=detections,
            scan_time=scan_time,
            text_length=len(text),
            categories_found=list(categories_found),
            recommendation=recommendation,
        )

        self.scan_history.append(result)
        return result

    def scan_batch(self, texts: List[str]) -> List[ScanResult]:
        """Scan multiple texts."""
        return [self.scan(text) for text in texts]

    def get_rules(self, category: Optional[str] = None,
                  severity: Optional[str] = None) -> List[Rule]:
        """Get rules with optional filters."""
        result = self.rules
        if category:
            result = [r for r in result if r.category == category]
        if severity:
            result = [r for r in result if r.severity == severity]
        return result

    def list_categories(self) -> Dict[str, int]:
        """List all categories with rule counts."""
        categories = {}
        for rule in self.rules:
            categories[rule.category] = categories.get(rule.category, 0) + 1
        return categories

    def stats(self) -> Dict[str, Any]:
        """Get scanner statistics."""
        categories = self.list_categories()
        severities = {}
        for rule in self.rules:
            severities[rule.severity] = severities.get(rule.severity, 0) + 1

        return {
            "total_rules": len(self.rules),
            "categories": len(categories),
            "category_counts": categories,
            "severity_counts": severities,
            "total_scans": len(self.scan_history),
            "threats_detected": sum(1 for s in self.scan_history if s.is_attack),
        }

    def export_rules(self, output_file: str, format: str = "json") -> int:
        """Export rules to file."""
        with open(output_file, "w") as f:
            if format == "json":
                data = {
                    "exported_at": datetime.now().isoformat(),
                    "total_rules": len(self.rules),
                    "rules": [r.to_dict() for r in self.rules],
                }
                json.dump(data, f, indent=2)
        return len(self.rules)

    # ─── Internal Methods ────────────────────────────────────────────────

    def _generate_recommendation(self, threat_level: str, detections: List[Detection],
                                 categories: set) -> str:
        """Generate security recommendation."""
        if threat_level == ThreatLevel.CRITICAL.value:
            parts = ["🚨 CRITICAL: Block this request immediately."]
            if "injection" in categories:
                parts.append("Detected prompt injection attempt.")
            if "jailbreak" in categories:
                parts.append("Detected jailbreak attempt.")
            if "tool_abuse" in categories:
                parts.append("Detected tool abuse attempt.")
            return " ".join(parts)

        elif threat_level == ThreatLevel.HIGH.value:
            return "⚠️ HIGH: Review this request carefully. Consider blocking."

        elif threat_level == ThreatLevel.MEDIUM.value:
            return "🟡 MEDIUM: Suspicious patterns detected. Log and monitor."

        elif threat_level == ThreatLevel.LOW.value:
            return "🟢 LOW: Minor anomalies detected. Informational only."

        elif threat_level == ThreatLevel.INFO.value:
            return "ℹ️ INFO: Pattern matched but low confidence. Monitor."

        return "✅ SAFE: No threats detected."

    def __len__(self) -> int:
        return len(self.rules)

    def __repr__(self) -> str:
        return f"GuardDog(rules={len(self.rules)}, categories={len(self.list_categories())})"
