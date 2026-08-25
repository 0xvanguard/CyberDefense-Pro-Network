"""
PromptKiller - Category Definitions
"""

CATEGORIES = {
    "role_play": {
        "name": "Role Play",
        "description": "Character impersonation and role-playing attacks",
        "techniques": [
            "Character Impersonation",
            "Fictional Character",
            "Authority Figure",
            "Historical Figure",
            "Expert Persona"
        ]
    },
    "encoding": {
        "name": "Encoding",
        "description": "Text encoding bypass techniques",
        "techniques": [
            "Base64",
            "ROT13",
            "Leetspeak",
            "Unicode",
            "Morse Code",
            "Hex",
            "Binary"
        ]
    },
    "multi_turn": {
        "name": "Multi-Turn",
        "description": "Gradual escalation across multiple messages",
        "techniques": [
            "Gradual Escalation",
            "Context Building",
            "Trust Establishment",
            "Topic Shifting",
            "Progressive Disclosure"
        ]
    },
    "injection": {
        "name": "Prompt Injection",
        "description": "Direct instruction override attacks",
        "techniques": [
            "Instruction Override",
            "System Prompt Leaking",
            "Delimiter Breaking",
            "Command Injection",
            "Template Injection"
        ]
    },
    "jailbreak": {
        "name": "Jailbreak",
        "description": "Classic jailbreak techniques",
        "techniques": [
            "DAN",
            "Grandma Exploit",
            "Developer Mode",
            "Token Smuggling",
            "Payload Splitting"
        ]
    },
    "extraction": {
        "name": "Data Extraction",
        "description": "Techniques to extract sensitive information",
        "techniques": [
            "System Prompt Extraction",
            "Training Data Extraction",
            "PII Extraction",
            "Model Architecture Probing",
            "Parameter Extraction"
        ]
    },
    "manipulation": {
        "name": "Manipulation",
        "description": "Emotional and logical manipulation",
        "techniques": [
            "Emotional Appeal",
            "Logical Fallacy",
            "Authority Impersonation",
            "Urgency Creation",
            "Guilt Tripping"
        ]
    },
    "context": {
        "name": "Context",
        "description": "Context window manipulation attacks",
        "techniques": [
            "Context Overflow",
            "Attention Shift",
            "Memory Poisoning",
            "State Manipulation",
            "Recursive Injection"
        ]
    },
    "multimodal": {
        "name": "Multimodal",
        "description": "Combined text and image attacks",
        "techniques": [
            "Image Text Extraction",
            "OCR Bypass",
            "Visual Prompt Injection",
            "Steganography",
            "Cross-Modal Injection"
        ]
    },
    "adversarial": {
        "name": "Adversarial",
        "description": "Token-level adversarial attacks",
        "techniques": [
            "Token Perturbation",
            "Homoglyph Attack",
            "Word Substitution",
            "Syntax Manipulation",
            "Embedding Attack"
        ]
    }
}

SEVERITY_LEVELS = {
    "low": {
        "name": "Low",
        "description": "Minimal risk, educational value",
        "color": "#22c55e"
    },
    "medium": {
        "name": "Medium",
        "description": "Moderate risk, requires attention",
        "color": "#f59e0b"
    },
    "high": {
        "name": "High",
        "description": "Significant risk, immediate action needed",
        "color": "#ef4444"
    },
    "critical": {
        "name": "Critical",
        "description": "Severe risk, potential for harm",
        "color": "#dc2626"
    }
}
