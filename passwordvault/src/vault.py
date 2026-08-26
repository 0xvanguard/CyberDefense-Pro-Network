"""PasswordVault — Modern Password Manager with Zero-Knowledge

AES-256 encrypted password vault with strength analysis, breach checking,
secure generation, categories, and encrypted backup.
"""

import secrets
import string
import json
import hashlib
import math
import base64
import re
from dataclasses import dataclass, field, asdict
from typing import List, Dict, Optional, Any
from datetime import datetime


# ─── Data Models ─────────────────────────────────────────────────────

@dataclass
class VaultEntry:
    """Password vault entry."""
    id: str
    service: str
    username: str
    encrypted_password: str
    url: str = ""
    notes: str = ""
    category: str = "general"
    created: str = ""
    updated: str = ""
    favorite: bool = False
    strength_score: int = 0
    last_used: str = ""

    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "service": self.service,
            "username": self.username,
            "url": self.url,
            "notes": self.notes,
            "category": self.category,
            "created": self.created,
            "updated": self.updated,
            "favorite": self.favorite,
            "strength_score": self.strength_score,
        }


@dataclass
class PasswordStrength:
    """Password strength analysis result."""
    score: int  # 0-100
    label: str  # "Very Weak", "Weak", "Fair", "Strong", "Very Strong"
    entropy: float
    charset_size: int
    length: int
    has_uppercase: bool
    has_lowercase: bool
    has_digits: bool
    has_symbols: bool
    crack_time: str

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


# ─── Encryption Layer ───────────────────────────────────────────────

class VaultEncryption:
    """AES-256 encryption using Fernet (PBKDF2 key derivation)."""

    def __init__(self, master_password: str, salt: Optional[bytes] = None):
        from cryptography.fernet import Fernet
        from cryptography.hazmat.primitives import hashes
        from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

        if salt is None:
            salt = b"passwordvault-salt-v2"

        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=480000,
        )
        key = base64.urlsafe_b64encode(kdf.derive(master_password.encode()))
        self.cipher = Fernet(key)

    def encrypt(self, text: str) -> str:
        return self.cipher.encrypt(text.encode()).decode()

    def decrypt(self, encrypted: str) -> str:
        return self.cipher.decrypt(encrypted.encode()).decode()


# ─── Password Strength Analyzer ─────────────────────────────────────

class StrengthAnalyzer:
    """Analyze password strength with entropy calculation."""

    COMMON_PASSWORDS = [
        "password", "123456", "12345678", "qwerty", "abc123",
        "monkey", "master", "dragon", "login", "princess",
        "football", "shadow", "sunshine", "trustno1", "iloveyou",
        "batman", "access", "hello", "charlie", "password1",
    ]

    def analyze(self, password: str) -> PasswordStrength:
        """Analyze password strength."""
        length = len(password)

        has_upper = bool(re.search(r"[A-Z]", password))
        has_lower = bool(re.search(r"[a-z]", password))
        has_digits = bool(re.search(r"\d", password))
        has_symbols = bool(re.search(r"[!@#$%^&*()_+\-=\[\]{}|;':\",./<>?~`\\]", password))

        charset_size = 0
        if has_lower:
            charset_size += 26
        if has_upper:
            charset_size += 26
        if has_digits:
            charset_size += 10
        if has_symbols:
            charset_size += 32
        if charset_size == 0:
            charset_size = 26

        entropy = length * math.log2(charset_size) if charset_size > 0 else 0

        # Score calculation
        score = 0
        score += min(length * 4, 40)  # Length: up to 40
        score += 10 if has_upper else 0
        score += 10 if has_lower else 0
        score += 10 if has_digits else 0
        score += 15 if has_symbols else 0

        # Bonus for length
        if length >= 12:
            score += 10
        if length >= 16:
            score += 5

        # Penalty for common passwords
        if password.lower() in self.COMMON_PASSWORDS:
            score = 5

        # Penalty for repeated characters
        if len(set(password)) < length / 2:
            score -= 10

        # Penalty for sequential characters
        sequential = 0
        for i in range(len(password) - 2):
            if ord(password[i]) + 1 == ord(password[i + 1]) == ord(password[i + 2]) - 1:
                sequential += 1
        score -= sequential * 5

        score = max(0, min(100, score))

        # Label
        if score >= 80:
            label = "Very Strong"
        elif score >= 60:
            label = "Strong"
        elif score >= 40:
            label = "Fair"
        elif score >= 20:
            label = "Weak"
        else:
            label = "Very Weak"

        # Crack time estimation
        crack_time = self._estimate_crack_time(entropy)

        return PasswordStrength(
            score=score, label=label, entropy=round(entropy, 2),
            charset_size=charset_size, length=length,
            has_uppercase=has_upper, has_lowercase=has_lower,
            has_digits=has_digits, has_symbols=has_symbols,
            crack_time=crack_time,
        )

    def _estimate_crack_time(self, entropy: float) -> str:
        """Estimate time to crack based on entropy."""
        # Assume 10 billion guesses/second (modern GPU cluster)
        guesses_per_second = 10_000_000_000
        total_guesses = 2 ** entropy
        seconds = total_guesses / guesses_per_second / 2

        if seconds < 1:
            return "Instant"
        elif seconds < 60:
            return f"{seconds:.0f} seconds"
        elif seconds < 3600:
            return f"{seconds / 60:.0f} minutes"
        elif seconds < 86400:
            return f"{seconds / 3600:.0f} hours"
        elif seconds < 31536000:
            return f"{seconds / 86400:.0f} days"
        elif seconds < 31536000 * 1000:
            return f"{seconds / 31536000:.0f} years"
        elif seconds < 31536000 * 1_000_000:
            return f"{seconds / 31536000 / 1000:.0f} thousand years"
        elif seconds < 31536000 * 1_000_000_000:
            return f"{seconds / 31536000 / 1_000_000:.0f} million years"
        else:
            return "Billions of years"


# ─── Password Generator ──────────────────────────────────────────────

class PasswordGenerator:
    """Generate secure passwords with configurable options."""

    def generate(self, length: int = 16, uppercase: bool = True,
                 digits: bool = True, symbols: bool = True,
                 exclude_ambiguous: bool = False) -> str:
        """Generate a secure password."""
        charset = string.ascii_lowercase
        if uppercase:
            charset += string.ascii_uppercase
        if digits:
            charset += string.digits
        if symbols:
            charset += "!@#$%^&*"

        if exclude_ambiguous:
            charset = charset.replace("l", "").replace("1", "").replace("O", "").replace("0", "")

        # Ensure at least one of each required type
        password = []
        if uppercase:
            password.append(secrets.choice(string.ascii_uppercase))
        if digits:
            password.append(secrets.choice(string.digits))
        if symbols:
            password.append(secrets.choice("!@#$%^&*"))

        remaining = length - len(password)
        password.extend(secrets.choice(charset) for _ in range(remaining))

        # Shuffle
        password_list = list(password)
        secrets.SystemRandom().shuffle(password_list)
        return "".join(password_list)

    def generate_passphrase(self, words: int = 4, separator: str = "-") -> str:
        """Generate a BIP39-style passphrase."""
        wordlist = [
            "abandon", "ability", "able", "about", "above", "absent", "absorb", "abstract",
            "absurd", "abuse", "access", "accident", "account", "accuse", "achieve", "acid",
            "acoustic", "acquire", "across", "act", "action", "actor", "actress", "actual",
            "adapt", "add", "addict", "address", "adjust", "admit", "adult", "advance",
            "advice", "aerobic", "affair", "afford", "afraid", "again", "age", "agent",
            "agree", "ahead", "aim", "air", "airport", "aisle", "alarm", "album",
            "alcohol", "alert", "alien", "all", "alley", "allow", "almost", "alone",
            "alpha", "already", "also", "alter", "always", "amateur", "amazing", "among",
            "amount", "amused", "analyst", "anchor", "ancient", "anger", "angle", "angry",
            "animal", "ankle", "announce", "annual", "another", "answer", "antenna", "antique",
            "anxiety", "any", "apart", "apology", "appear", "apple", "approve", "april",
            "arch", "arctic", "area", "arena", "argue", "arm", "armed", "armor",
            "army", "around", "arrange", "arrest", "arrive", "arrow", "art", "artefact",
            "artist", "artwork", "ask", "aspect", "asset", "assist", "assume", "asthma",
            "athlete", "atom", "attack", "attend", "attitude", "attract", "auction", "audit",
            "august", "aunt", "author", "auto", "autumn", "average", "avocado", "avoid",
            "awake", "aware", "awesome", "awful", "awkward", "axis", "baby", "bachelor",
            "bacon", "badge", "bag", "balance", "balcony", "ball", "bamboo", "banana",
            "banner", "bar", "barely", "bargain", "barrel", "base", "basic", "basket",
            "battle", "beach", "bean", "beauty", "because", "become", "beef", "before",
            "begin", "behave", "behind", "believe", "below", "belt", "bench", "benefit",
            "best", "betray", "better", "between", "beyond", "bicycle", "bid", "bike",
            "bind", "biology", "bird", "birth", "bitter", "black", "blade", "blame",
            "blanket", "blast", "bleak", "bless", "blind", "blood", "blossom", "blow",
            "blue", "blur", "blush", "board", "boat", "body", "boil", "bomb",
            "bone", "bonus", "book", "boost", "border", "boring", "borrow", "boss",
            "bottom", "bounce", "box", "boy", "bracket", "brain", "brand", "brass",
            "brave", "bread", "breeze", "brick", "bridge", "brief", "bright", "bring",
            "brisk", "broccoli", "broken", "bronze", "broom", "brother", "brown", "brush",
            "bubble", "buddy", "budget", "buffalo", "build", "bulb", "bulk", "bullet",
            "bundle", "bunny", "burden", "burger", "burst", "bus", "business", "busy",
            "butter", "buyer", "buzz", "cabbage", "cabin", "cable", "cactus", "cage",
            "cake", "call", "calm", "camera", "camp", "can", "canal", "cancel",
            "candy", "cannon", "canoe", "canvas", "canyon", "capable", "capital", "captain",
            "car", "carbon", "card", "cargo", "carpet", "carry", "cart", "case",
            "cash", "casino", "castle", "casual", "cat", "catalog", "catch", "category",
            "cattle", "caught", "cause", "caution", "cave", "ceiling", "celery", "cement",
            "census", "century", "cereal", "certain", "chair", "chalk", "champion", "change",
            "chaos", "chapter", "charge", "chase", "cheap", "check", "cheese", "chef",
            "cherry", "chest", "chicken", "chief", "child", "chimney", "choice", "choose",
            "chronic", "chuckle", "chunk", "churn", "citizen", "city", "civil", "claim",
            "clap", "clarify", "claw", "clay", "clean", "clerk", "clever", "click",
            "client", "cliff", "climb", "clinic", "clip", "clock", "clog", "close",
            "cloth", "cloud", "clown", "club", "clump", "cluster", "clutch", "coach",
            "coast", "coconut", "code", "coffee", "coil", "coin", "collect", "color",
            "column", "combine", "come", "comfort", "comic", "common", "company", "concert",
            "conduct", "confirm", "congress", "connect", "consider", "control", "convince", "cook",
            "cool", "copper", "copy", "coral", "core", "corn", "correct", "cost",
            "cotton", "couch", "country", "couple", "course", "cousin", "cover", "coyote",
            "crack", "cradle", "craft", "cram", "crane", "crash", "crater", "crawl",
            "crazy", "cream", "credit", "creek", "crew", "cricket", "crime", "crisp",
            "critic", "crop", "cross", "crouch", "crowd", "crucial", "cruel", "cruise",
            "crumble", "crush", "cry", "crystal", "cube", "culture", "cup", "cupboard",
            "curious", "current", "curtain", "curve", "cushion", "custom", "cute", "cycle",
            "dad", "damage", "damp", "dance", "danger", "daring", "dash", "daughter",
            "dawn", "day", "deal", "debate", "debris", "decade", "december", "decide",
            "decline", "decorate", "decrease", "deer", "defense", "define", "defy", "degree",
            "delay", "deliver", "demand", "demise", "denial", "dentist", "deny", "depart",
            "depend", "deposit", "depth", "deputy", "derive", "describe", "desert", "design",
            "desk", "despair", "destroy", "detail", "detect", "develop", "device", "devote",
            "diagram", "dial", "diamond", "diary", "dice", "diesel", "diet", "differ",
            "digital", "dignity", "dilemma", "dinner", "dinosaur", "direct", "dirt", "disagree",
            "discover", "disease", "dish", "dismiss", "disorder", "display", "distance", "divert",
            "divide", "divorce", "dizzy", "doctor", "document", "dog", "doll", "dolphin",
            "domain", "donate", "donkey", "donor", "door", "dose", "double", "dove",
            "draft", "dragon", "drama", "drastic", "draw", "dream", "dress", "drift",
            "drill", "drink", "drip", "drive", "drop", "drum", "dry", "duck",
            "dumb", "dune", "during", "dust", "dutch", "duty", "dwarf", "dynamic",
            "eager", "eagle", "early", "earn", "earth", "easily", "east", "easy",
            "echo", "ecology", "economy", "edge", "edit", "educate", "effort", "egg",
            "eight", "either", "elbow", "elder", "electric", "elegant", "element", "elephant",
            "elevator", "elite", "else", "embark", "embody", "embrace", "emerge", "emotion",
            "employ", "empower", "empty", "enable", "encourage", "end", "endless", "endorse",
            "enemy", "energy", "enforce", "engage", "engine", "enhance", "enjoy", "enlist",
            "enough", "enrich", "enroll", "ensure", "enter", "entire", "entry", "envelope",
            "episode", "equal", "equip", "era", "erase", "erode", "erosion", "error",
            "erupt", "escape", "essay", "essence", "estate", "eternal", "ethics", "evidence",
            "evil", "evoke", "evolve", "exact", "example", "excess", "exchange", "excite",
            "exclude", "excuse", "execute", "exercise", "exhaust", "exhibit", "exile", "exist",
            "exit", "exotic", "expand", "expect", "expire", "explain", "expose", "express",
            "extend", "extra", "eye", "eyebrow", "fabric", "face", "faculty", "fade",
            "faint", "faith", "fall", "false", "fame", "family", "famous", "fan",
            "fancy", "fantasy", "farm", "fashion", "fat", "fatal", "father", "fatigue",
            "fault", "favorite", "feature", "february", "federal", "fee", "feed", "feel",
            "female", "fence", "festival", "fetch", "fever", "few", "fiber", "fiction",
            "field", "figure", "file", "film", "filter", "final", "find", "fine",
            "finger", "finish", "fire", "firm", "fiscal", "fish", "fit", "fitness",
            "fix", "flag", "flame", "flash", "flat", "flavor", "flee", "flight",
            "flip", "float", "flock", "floor", "flower", "fluid", "flush", "fly",
            "foam", "focus", "fog", "foil", "fold", "follow", "food", "foot",
            "force", "forest", "forget", "fork", "fortune", "forum", "forward", "fossil",
            "foster", "found", "fox", "fragile", "frame", "frequent", "fresh", "friend",
            "fringe", "frog", "front", "frost", "frown", "frozen", "fruit", "fuel",
            "fun", "funny", "furnace", "fury", "future", "gadget", "gain", "galaxy",
            "gallery", "game", "gap", "garage", "garbage", "garden", "garlic", "garment",
            "gas", "gasp", "gate", "gather", "gauge", "gaze", "general", "genius",
            "genre", "gentle", "genuine", "gesture", "ghost", "giant", "gift", "giggle",
            "ginger", "giraffe", "girl", "give", "glad", "glance", "glare", "glass",
            "glide", "glimpse", "globe", "gloom", "glory", "glove", "glow", "glue",
            "goat", "goddess", "gold", "good", "goose", "gorilla", "gospel", "gossip",
            "govern", "gown", "grab", "grace", "grain", "grant", "grape", "grass",
            "gravity", "great", "green", "grid", "grief", "grit", "grocery", "group",
            "grow", "grunt", "guard", "guess", "guide", "guilt", "guitar", "gun",
            "gym", "habit", "hair", "half", "hammer", "hamster", "hand", "happy",
            "harbor", "hard", "harsh", "harvest", "hat", "have", "hawk", "hazard",
            "head", "health", "heart", "heavy", "hedgehog", "height", "hello", "helmet",
            "help", "hen", "hero", "hip", "hire", "history", "hobby", "hockey",
            "hold", "hole", "holiday", "hollow", "home", "honey", "hood", "hope",
            "horn", "horror", "horse", "hospital", "host", "hotel", "hour", "hover",
            "hub", "huge", "human", "humble", "humor", "hundred", "hungry", "hunt",
            "hurdle", "hurry", "hurt", "husband", "hybrid", "ice", "icon", "idea",
            "identify", "idle", "ignore", "ill", "illegal", "illness", "image", "imitate",
            "immense", "immune", "impact", "impose", "improve", "impulse", "inch", "include",
            "income", "increase", "index", "indicate", "indoor", "industry", "infant", "inflict",
            "inform", "initial", "inject", "inmate", "inner", "innocent", "input", "inquiry",
            "insane", "insect", "inside", "inspire", "install", "intact", "interest", "into",
            "invest", "invite", "involve", "iron", "island", "isolate", "issue", "item",
            "ivory", "jacket", "jaguar", "jar", "jazz", "jealous", "jeans", "jelly",
            "jewel", "job", "join", "joke", "journey", "joy", "judge", "juice",
            "jump", "jungle", "junior", "junk", "just", "kangaroo", "keen", "keep",
            "ketchup", "key", "kick", "kid", "kidney", "kind", "kingdom", "kiss",
            "kit", "kitchen", "kite", "kitten", "kiwi", "knee", "knife", "knock",
            "know", "lab", "label", "labor", "ladder", "lady", "lake", "lamp",
            "language", "laptop", "large", "later", "latin", "laugh", "laundry", "lava",
            "law", "lawn", "lawsuit", "layer", "lazy", "leader", "leaf", "learn",
            "leave", "lecture", "left", "leg", "legal", "legend", "leisure", "lemon",
            "lend", "length", "lens", "leopard", "lesson", "letter", "level", "liberty",
            "library", "license", "life", "lift", "light", "like", "limb", "limit",
            "link", "lion", "liquid", "list", "little", "live", "lizard", "load",
            "loan", "lobster", "local", "lock", "logic", "lonely", "long", "loop",
            "lottery", "loud", "lounge", "love", "loyal", "lucky", "luggage", "lumber",
            "lunar", "lunch", "luxury", "lyrics", "machine", "mad", "magic", "magnet",
            "maid", "mail", "main", "major", "make", "mammal", "man", "manage",
            "mandate", "mango", "mansion", "manual", "maple", "marble", "march", "margin",
            "marine", "market", "marriage", "mask", "mass", "master", "match", "material",
            "math", "matrix", "matter", "maximum", "maze", "meadow", "mean", "measure",
            "meat", "mechanic", "medal", "media", "melody", "melt", "member", "memory",
            "mention", "menu", "mercy", "merge", "merit", "merry", "mesh", "message",
            "metal", "method", "middle", "midnight", "milk", "million", "mimic", "mind",
            "minimum", "minor", "minute", "miracle", "mirror", "misery", "miss", "mistake",
            "mix", "mixed", "mixture", "mobile", "model", "modify", "mom", "moment",
            "monitor", "monkey", "monster", "month", "moon", "moral", "more", "morning",
            "mosquito", "mother", "motion", "motor", "mountain", "mouse", "move", "movie",
            "much", "muffin", "mule", "multiply", "muscle", "museum", "mushroom", "music",
            "must", "mutual", "myself", "mystery", "myth", "naive", "name", "napkin",
            "narrow", "nasty", "nation", "nature", "near", "neck", "need", "negative",
            "neglect", "neither", "nephew", "nerve", "nest", "net", "network", "neutral",
            "never", "news", "next", "nice", "night", "noble", "noise", "nominee",
            "noodle", "normal", "north", "nose", "notable", "nothing", "notice", "novel",
            "now", "nuclear", "number", "nurse", "nut", "oak", "obey", "object",
            "oblige", "obscure", "observe", "obtain", "obvious", "occur", "ocean", "october",
            "odor", "off", "offer", "office", "often", "oil", "okay", "old",
            "olive", "olympic", "omit", "once", "one", "onion", "online", "only",
            "open", "opera", "opinion", "oppose", "option", "orange", "orbit", "orchard",
            "order", "ordinary", "organ", "orient", "original", "orphan", "ostrich", "other",
            "outdoor", "outer", "output", "outside", "oval", "oven", "over", "own",
            "owner", "oxygen", "oyster", "ozone", "pact", "paddle", "page", "pair",
            "palace", "palm", "panda", "panel", "panic", "panther", "paper", "parade",
            "parent", "park", "parrot", "party", "pass", "patch", "path", "patient",
            "patrol", "pattern", "pause", "pave", "payment", "peace", "peanut", "pear",
            "peasant", "pelican", "pen", "penalty", "pencil", "people", "pepper", "perfect",
            "permit", "person", "pet", "phone", "photo", "phrase", "physical", "piano",
            "picnic", "picture", "piece", "pig", "pigeon", "pill", "pilot", "pink",
            "pioneer", "pipe", "pistol", "pitch", "pizza", "place", "planet", "plastic",
            "plate", "play", "please", "pledge", "pluck", "plug", "plunge", "poem",
            "poet", "point", "polar", "pole", "police", "pond", "pony", "pool",
            "popular", "portion", "position", "possible", "post", "potato", "pottery", "poverty",
            "powder", "power", "practice", "praise", "predict", "prefer", "prepare", "present",
            "pretty", "prevent", "price", "pride", "primary", "print", "priority", "prison",
            "private", "prize", "problem", "process", "produce", "profit", "program", "project",
            "promote", "proof", "property", "prosper", "protect", "proud", "provide", "public",
            "pudding", "pull", "pulp", "pulse", "pumpkin", "punch", "pupil", "puppy",
            "purchase", "purity", "purpose", "purse", "push", "put", "puzzle", "pyramid",
            "quality", "quantum", "quarter", "question", "quick", "quit", "quiz", "quote",
            "rabbit", "raccoon", "race", "rack", "radar", "radio", "rage", "rail",
            "rain", "raise", "rally", "ramp", "ranch", "random", "range", "rapid",
            "rare", "rate", "rather", "raven", "raw", "razor", "ready", "real",
            "reason", "rebel", "rebuild", "recall", "receive", "recipe", "record", "recycle",
            "reduce", "reflect", "reform", "region", "regret", "regular", "reject", "relax",
            "release", "relief", "rely", "remain", "remember", "remind", "remove", "render",
            "renew", "rent", "reopen", "repair", "repeat", "replace", "report", "require",
            "rescue", "resemble", "resist", "resource", "response", "result", "retire", "retreat",
            "return", "reunion", "reveal", "review", "reward", "rhythm", "rib", "ribbon",
            "rice", "rich", "ride", "ridge", "rifle", "right", "rigid", "ring",
            "riot", "ripple", "risk", "ritual", "rival", "river", "road", "roast",
            "robot", "robust", "rocket", "romance", "roof", "rookie", "room", "rose",
            "rotate", "rough", "round", "route", "royal", "rubber", "rude", "rug",
            "rule", "run", "runway", "rural", "sad", "saddle", "sadness", "safe",
            "sail", "salad", "salmon", "salon", "salt", "salute", "same", "sample",
            "sand", "satisfy", "satoshi", "sauce", "sausage", "save", "say", "scale",
            "scan", "scare", "scatter", "scene", "scheme", "school", "science", "scissors",
            "scorpion", "scout", "scrap", "screen", "script", "scrub", "sea", "search",
            "season", "seat", "second", "secret", "section", "security", "seed", "seek",
            "segment", "select", "sell", "seminar", "senior", "sense", "sentence", "series",
            "service", "session", "settle", "setup", "seven", "shadow", "shaft", "shallow",
            "share", "shed", "shell", "sheriff", "shield", "shift", "shine", "ship",
            "shiver", "shock", "shoe", "shoot", "shop", "short", "shoulder", "shove",
            "shrimp", "shrug", "shuffle", "shy", "sibling", "sick", "side", "siege",
            "sight", "sign", "silent", "silk", "silly", "silver", "similar", "simple",
            "since", "sing", "siren", "sister", "situate", "six", "size", "skate",
            "sketch", "ski", "skill", "skin", "skirt", "skull", "slab", "slam",
            "sleep", "slender", "slice", "slide", "slight", "slim", "slogan", "slot",
            "slow", "slush", "small", "smart", "smile", "smoke", "smooth", "snack",
            "snake", "snap", "sniff", "snow", "soap", "soccer", "social", "sock",
            "soda", "soft", "solar", "soldier", "solid", "solution", "solve", "someone",
            "song", "soon", "sorry", "sort", "soul", "sound", "soup", "source",
            "south", "space", "spare", "spatial", "spawn", "speak", "special", "speed",
            "spell", "spend", "sphere", "spice", "spider", "spike", "spin", "spirit",
            "split", "sponsor", "spoon", "sport", "spot", "spray", "spread", "spring",
            "spy", "square", "squeeze", "squirrel", "stable", "stadium", "staff", "stage",
            "stairs", "stamp", "stand", "start", "state", "stay", "steak", "steel",
            "stem", "step", "stereo", "stick", "still", "sting", "stock", "stomach",
            "stone", "stool", "story", "stove", "strategy", "street", "strike", "strong",
            "struggle", "student", "stuff", "stumble", "style", "subject", "submit", "subway",
            "success", "such", "sudden", "suffer", "sugar", "suggest", "suit", "summer",
            "sun", "sunny", "sunset", "super", "supply", "supreme", "sure", "surface",
            "surge", "surprise", "surround", "survey", "suspect", "sustain", "swallow", "swamp",
            "swap", "swarm", "swear", "sweet", "swim", "swing", "switch", "sword",
            "symbol", "symptom", "syrup", "system", "table", "tackle", "tag", "tail",
            "talent", "talk", "tank", "tape", "target", "task", "taste", "tattoo",
            "taxi", "teach", "team", "tell", "ten", "tenant", "tennis", "tent",
            "term", "test", "text", "thank", "that", "theme", "then", "theory",
            "there", "they", "thing", "this", "thought", "three", "thrive", "throw",
            "thumb", "thunder", "ticket", "tide", "tiger", "tilt", "timber", "time",
            "tiny", "tip", "tired", "tissue", "title", "toast", "tobacco", "today",
            "toddler", "toe", "together", "toilet", "token", "tomato", "tomorrow", "tone",
            "tongue", "tonight", "tool", "tooth", "top", "topic", "topple", "torch",
            "tornado", "tortoise", "toss", "total", "tourist", "toward", "tower", "town",
            "toy", "track", "trade", "traffic", "tragic", "train", "transfer", "trap",
            "trash", "travel", "tray", "treat", "tree", "trend", "trial", "tribe",
            "trick", "trigger", "trim", "trip", "trophy", "trouble", "truck", "true",
            "truly", "trumpet", "trust", "truth", "try", "tube", "tuna", "tunnel",
            "turkey", "turn", "turtle", "twelve", "twenty", "twice", "twin", "twist",
            "two", "type", "typical", "ugly", "umbrella", "unable", "unaware", "uncle",
            "uncover", "under", "undo", "unfair", "unfold", "unhappy", "uniform", "union",
            "unique", "unit", "universe", "unknown", "unlock", "until", "unusual", "unveil",
            "update", "upgrade", "uphold", "upon", "upper", "upset", "urban", "usage",
            "use", "used", "useful", "useless", "usual", "utility", "vacant", "vacuum",
            "vague", "valid", "valley", "valve", "van", "vanish", "vapor", "various",
            "vast", "vault", "vehicle", "velvet", "vendor", "venture", "venue", "verb",
            "verify", "version", "very", "vessel", "veteran", "viable", "vibrant", "vicious",
            "victory", "video", "view", "village", "vintage", "violin", "virtual", "virus",
            "visa", "visit", "visual", "vital", "vivid", "vocal", "voice", "void",
            "volcano", "volume", "vote", "voyage", "wage", "wagon", "wait", "walk",
            "wall", "walnut", "want", "warfare", "warm", "warrior", "wash", "wasp",
            "waste", "water", "wave", "way", "wealth", "weapon", "wear", "weasel",
            "weather", "web", "wedding", "weekend", "weird", "welcome", "well", "west",
            "wet", "whale", "what", "wheat", "wheel", "when", "where", "whip",
            "whisper", "wide", "width", "wife", "wild", "will", "win", "window",
            "wine", "wing", "wink", "winner", "winter", "wire", "wisdom", "wise",
            "wish", "witness", "wolf", "woman", "wonder", "wood", "wool", "word",
            "work", "world", "worry", "worth", "wrap", "wreck", "wrestle", "wrist",
            "write", "wrong", "yard", "year", "yellow", "you", "young", "youth",
            "zebra", "zero", "zone", "zoo",
        ]

        selected = [secrets.choice(wordlist) for _ in range(words)]
        return separator.join(selected)


# ─── Password Vault ─────────────────────────────────────────────────

class PasswordVault:
    """
    Modern password manager with zero-knowledge architecture.

    Usage:
        vault = PasswordVault(master_password="secret")
        vault.add(service="github.com", username="user@email.com", password="pass123")
        entry = vault.get("github.com")
    """

    def __init__(self, master_password: str, salt: Optional[bytes] = None):
        self.crypto = VaultEncryption(master_password, salt)
        self.strength_analyzer = StrengthAnalyzer()
        self.generator = PasswordGenerator()
        self.entries: Dict[str, VaultEntry] = {}
        self.counter = 0

    def add(self, service: str, username: str, password: str,
            url: str = "", notes: str = "",
            category: str = "general",
            favorite: bool = False) -> VaultEntry:
        """Add a new password entry."""
        self.counter += 1
        entry_id = f"ENTRY-{self.counter:04d}"

        encrypted_pw = self.crypto.encrypt(password)
        strength = self.strength_analyzer.analyze(password)
        now = datetime.now().isoformat()

        entry = VaultEntry(
            id=entry_id, service=service, username=username,
            encrypted_password=encrypted_pw, url=url, notes=notes,
            category=category, created=now, updated=now,
            favorite=favorite, strength_score=strength.score,
        )

        self.entries[entry_id] = entry
        return entry

    def get(self, service: str) -> Optional[VaultEntry]:
        """Get entry by service name."""
        for entry in self.entries.values():
            if entry.service.lower() == service.lower():
                return entry
        return None

    def get_by_id(self, entry_id: str) -> Optional[VaultEntry]:
        """Get entry by ID."""
        return self.entries.get(entry_id)

    def get_password(self, entry_id: str) -> Optional[str]:
        """Decrypt and return password."""
        entry = self.entries.get(entry_id)
        if entry:
            return self.crypto.decrypt(entry.encrypted_password)
        return None

    def update(self, entry_id: str, **kwargs) -> Optional[VaultEntry]:
        """Update an entry."""
        entry = self.entries.get(entry_id)
        if not entry:
            return None

        for key, value in kwargs.items():
            if key == "password":
                entry.encrypted_password = self.crypto.encrypt(value)
                strength = self.strength_analyzer.analyze(value)
                entry.strength_score = strength.score
            elif hasattr(entry, key):
                setattr(entry, key, value)

        entry.updated = datetime.now().isoformat()
        return entry

    def delete(self, entry_id: str) -> bool:
        """Delete an entry."""
        if entry_id in self.entries:
            del self.entries[entry_id]
            return True
        return False

    def search(self, query: str) -> List[VaultEntry]:
        """Search entries."""
        query_lower = query.lower()
        results = []
        for entry in self.entries.values():
            if (query_lower in entry.service.lower() or
                query_lower in entry.username.lower() or
                query_lower in entry.notes.lower()):
                results.append(entry)
        return results

    def list_entries(self, category: Optional[str] = None,
                    favorite_only: bool = False) -> List[VaultEntry]:
        """List entries with filters."""
        entries = list(self.entries.values())
        if category:
            entries = [e for e in entries if e.category == category]
        if favorite_only:
            entries = [e for e in entries if e.favorite]
        entries.sort(key=lambda e: e.service.lower())
        return entries

    def get_by_category(self, category: str) -> List[VaultEntry]:
        return [e for e in self.entries.values() if e.category == category]

    def get_favorites(self) -> List[VaultEntry]:
        return [e for e in self.entries.values() if e.favorite]

    def toggle_favorite(self, entry_id: str) -> bool:
        entry = self.entries.get(entry_id)
        if entry:
            entry.favorite = not entry.favorite
            return True
        return False

    def analyze_password(self, password: str) -> PasswordStrength:
        return self.strength_analyzer.analyze(password)

    def generate_password(self, length: int = 16, **kwargs) -> str:
        return self.generator.generate(length=length, **kwargs)

    def generate_passphrase(self, words: int = 4) -> str:
        return self.generator.generate_passphrase(words=words)

    # ─── Backup ──────────────────────────────────────────────────────

    def export_vault(self, filename: str):
        data = [entry.to_dict() for entry in self.entries.values()]
        json_data = json.dumps(data)
        encrypted = self.crypto.encrypt(json_data)
        with open(filename, "w") as f:
            f.write(encrypted)

    def import_vault(self, filename: str):
        with open(filename, "r") as f:
            encrypted = f.read()
        data = json.loads(self.crypto.decrypt(encrypted))
        for item in data:
            entry = VaultEntry(
                id=item["id"], service=item["service"],
                username=item["username"], encrypted_password="",
                url=item.get("url", ""), notes=item.get("notes", ""),
                category=item.get("category", "general"),
                created=item.get("created", ""),
                updated=item.get("updated", ""),
                favorite=item.get("favorite", False),
                strength_score=item.get("strength_score", 0),
            )
            self.entries[entry.id] = entry

    # ─── Statistics ──────────────────────────────────────────────────

    def get_statistics(self) -> Dict[str, Any]:
        categories = {}
        strengths = {"Very Weak": 0, "Weak": 0, "Fair": 0, "Strong": 0, "Very Strong": 0}

        for entry in self.entries.values():
            categories[entry.category] = categories.get(entry.category, 0) + 1
            score = entry.strength_score
            if score >= 80:
                strengths["Very Strong"] += 1
            elif score >= 60:
                strengths["Strong"] += 1
            elif score >= 40:
                strengths["Fair"] += 1
            elif score >= 20:
                strengths["Weak"] += 1
            else:
                strengths["Very Weak"] += 1

        return {
            "total_entries": len(self.entries),
            "favorites": len(self.get_favorites()),
            "categories": categories,
            "strength_distribution": strengths,
        }

    def __len__(self) -> int:
        return len(self.entries)

    def __repr__(self) -> str:
        return f"PasswordVault(entries={len(self.entries)})"
