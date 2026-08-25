"""PassGen Pro - Password Generator with Visual Entropy"""
import secrets
import string
import math
from dataclasses import dataclass
from typing import Optional


@dataclass
class PasswordAnalysis:
    """Password strength analysis."""
    password: str
    length: int
    entropy_bits: float
    strength: str
    time_to_crack: str
    has_uppercase: bool
    has_lowercase: bool
    has_digits: bool
    has_symbols: bool
    charset_size: int


class PassGen:
    """
    Password generator with visual entropy display.
    
    Usage:
        gen = PassGen()
        password = gen.generate(length=20)
        analysis = gen.analyze(password)
    """
    
    def __init__(self):
        self.lowercase = string.ascii_lowercase
        self.uppercase = string.ascii_uppercase
        self.digits = string.digits
        self.symbols = "!@#$%^&*()_+-=[]{}|;:,.<>?"
    
    def generate(self, length: int = 16, uppercase: bool = True, 
                 digits: bool = True, symbols: bool = True,
                 exclude: str = "") -> str:
        """Generate a cryptographically secure password."""
        charset = self.lowercase
        if uppercase:
            charset += self.uppercase
        if digits:
            charset += self.digits
        if symbols:
            charset += self.symbols
        
        # Remove excluded characters
        for char in exclude:
            charset = charset.replace(char, "")
        
        if not charset:
            charset = self.lowercase
        
        return ''.join(secrets.choice(charset) for _ in range(length))
    
    def analyze(self, password: str) -> PasswordAnalysis:
        """Analyze password strength."""
        # Calculate charset size
        charset_size = 0
        if any(c.islower() for c in password):
            charset_size += 26
        if any(c.isupper() for c in password):
            charset_size += 26
        if any(c.isdigit() for c in password):
            charset_size += 10
        if any(c in self.symbols for c in password):
            charset_size += len(self.symbols)
        
        # Calculate entropy
        entropy = len(password) * math.log2(charset_size) if charset_size > 0 else 0
        
        # Determine strength
        if entropy >= 100:
            strength = "EXCELLENT"
            time_to_crack = "Centuries"
        elif entropy >= 80:
            strength = "STRONG"
            time_to_crack = "Years"
        elif entropy >= 60:
            strength = "GOOD"
            time_to_crack = "Months"
        elif entropy >= 40:
            strength = "FAIR"
            time_to_crack = "Days"
        else:
            strength = "WEAK"
            time_to_crack = "Minutes"
        
        return PasswordAnalysis(
            password=password,
            length=len(password),
            entropy_bits=round(entropy, 2),
            strength=strength,
            time_to_crack=time_to_crack,
            has_uppercase=any(c.isupper() for c in password),
            has_lowercase=any(c.islower() for c in password),
            has_digits=any(c.isdigit() for c in password),
            has_symbols=any(c in self.symbols for c in password),
            charset_size=charset_size
        )
    
    def visualize(self, password: str) -> str:
        """Create visual strength display."""
        analysis = self.analyze(password)
        
        # Color based on strength
        colors = {
            "WEAK": "\033[91m",      # Red
            "FAIR": "\033[93m",      # Yellow
            "GOOD": "\033[96m",      # Cyan
            "STRONG": "\033[92m",    # Green
            "EXCELLENT": "\033[95m"  # Magenta
        }
        reset = "\033[0m"
        color = colors.get(analysis.strength, "")
        
        # Entropy bar
        bar_length = 40
        filled = int(analysis.entropy_bits / 128 * bar_length)
        bar = "█" * filled + "░" * (bar_length - filled)
        
        return f"""
╔══════════════════════════════════════════════╗
║  🔐 Password Analysis                        ║
╠══════════════════════════════════════════════╣
║  Password: {password[:20]}{'...' if len(password) > 20 else ''}
║  Length:    {analysis.length} characters
║  Entropy:   {analysis.entropy_bits} bits
║  Strength:  {color}{analysis.strength}{reset}
║  Crack Time: {analysis.time_to_crack}
╠══════════════════════════════════════════════╣
║  [{bar}] {analysis.entropy_bits}/128
╠══════════════════════════════════════════════╣
║  ✓ Uppercase: {'✅' if analysis.has_uppercase else '❌'}
║  ✓ Lowercase: {'✅' if analysis.has_lowercase else '❌'}
║  ✓ Digits:    {'✅' if analysis.has_digits else '❌'}
║  ✓ Symbols:   {'✅' if analysis.has_symbols else '❌'}
╚══════════════════════════════════════════════╝
"""
    
    def generate_memorable(self, word_count: int = 4) -> str:
        """Generate a memorable passphrase."""
        words = [
            "apple", "brave", "cloud", "dance", "eagle", "flame", "grape",
            "happy", "igloo", "juice", "kite", "lemon", "mango", "noble",
            "ocean", "piano", "queen", "river", "stone", "tiger", "ultra",
            "voice", "whale", "xenon", "yacht", "zebra"
        ]
        separator = secrets.choice(["-", "_", ".", " "])
        return separator.join(secrets.choice(words) for _ in range(word_count))
    
    def __repr__(self) -> str:
        return "PassGen()"
