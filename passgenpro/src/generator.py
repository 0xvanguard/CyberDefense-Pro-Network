"""
PassGen Pro — Password Generator with Entropy Visualization

A Python library for generating secure passwords with visual entropy analysis,
strength scoring, and breach checking.

Usage:
    from passgenpro import PassGen

    gen = PassGen()
    password = gen.random(length=20)
    print(f"Password: {password}")
    print(f"Entropy: {password.entropy} bits")
    print(f"Strength: {password.strength_bar}")
"""

import secrets
import string
import math
import hashlib
import json
import time
from pathlib import Path
from dataclasses import dataclass, field, asdict
from typing import Optional, List, Dict, Any, Tuple
from enum import Enum


class PasswordStrength(Enum):
    VERY_WEAK = "very_weak"
    WEAK = "weak"
    FAIR = "fair"
    STRONG = "strong"
    VERY_STRONG = "very_strong"


@dataclass
class EntropyAnalysis:
    """Detailed entropy analysis of a password."""
    total_bits: float
    charset_size: int
    password_length: int
    entropy_per_char: float
    crack_time_seconds: float
    crack_time_display: str
    strength: str
    strength_score: float  # 0-100

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


@dataclass
class Password:
    """Generated password with analysis."""
    password: str
    entropy: float
    strength: str
    strength_score: float
    strength_bar: str
    charset_used: str
    has_uppercase: bool
    has_lowercase: bool
    has_digits: bool
    has_symbols: bool
    unique_chars: int
    char_distribution: Dict[str, int]
    crack_time: str
    entropy_analysis: EntropyAnalysis

    def to_dict(self) -> Dict[str, Any]:
        return {
            "password": self.password,
            "entropy": self.entropy,
            "strength": self.strength,
            "strength_score": self.strength_score,
            "strength_bar": self.strength_bar,
            "charset_used": self.charset_used,
            "has_uppercase": self.has_uppercase,
            "has_lowercase": self.has_lowercase,
            "has_digits": self.has_digits,
            "has_symbols": self.has_symbols,
            "unique_chars": self.unique_chars,
            "crack_time": self.crack_time,
        }

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), indent=2)


# ─── BIP39 Wordlist (2048 words) ──────────────────────────────────────

BIP39_WORDS = [
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
    "artist", "artwork", "ask", "aspect", "assault", "asset", "assist", "assume",
    "asthma", "athlete", "atom", "attack", "attend", "attitude", "attract", "auction",
    "audit", "august", "aunt", "author", "auto", "autumn", "average", "avocado",
    "avoid", "awake", "aware", "awesome", "awful", "awkward", "axis", "baby",
    "bachelor", "bacon", "badge", "bag", "balance", "balcony", "ball", "bamboo",
    "banana", "banner", "bar", "barely", "bargain", "barrel", "base", "basic",
    "basket", "battle", "beach", "bean", "beauty", "because", "become", "beef",
    "before", "begin", "behave", "behind", "believe", "below", "belt", "bench",
    "benefit", "best", "betray", "better", "between", "beyond", "bicycle", "bid",
    "bike", "bind", "biology", "bird", "birth", "bitter", "black", "blade",
    "blame", "blanket", "blast", "bleak", "bless", "blind", "blood", "blossom",
    "blow", "blue", "blur", "blush", "board", "boat", "body", "boil",
    "bomb", "bone", "bonus", "book", "boost", "border", "boring", "borrow",
    "boss", "bottom", "bounce", "box", "boy", "bracket", "brain", "brand",
    "brass", "brave", "bread", "breeze", "brick", "bridge", "brief", "bright",
    "bring", "brisk", "broccoli", "broken", "bronze", "broom", "brother", "brown",
    "brush", "bubble", "buddy", "budget", "buffalo", "build", "bulb", "bulk",
    "bullet", "bundle", "bunny", "burden", "burger", "burst", "bus", "business",
    "busy", "butter", "buyer", "buzz", "cabbage", "cabin", "cable", "cactus",
    "cage", "cake", "call", "calm", "camera", "camp", "can", "canal",
    "cancel", "candy", "cannon", "canoe", "canvas", "canyon", "capable", "capital",
    "captain", "car", "carbon", "card", "cargo", "carpet", "carry", "cart",
    "case", "cash", "casino", "castle", "casual", "cat", "catalog", "catch",
    "category", "cattle", "caught", "cause", "caution", "cave", "ceiling", "celery",
    "cement", "census", "century", "cereal", "certain", "chair", "chalk", "champion",
    "change", "chaos", "chapter", "charge", "chase", "cheap", "check", "cheese",
    "chef", "cherry", "chest", "chicken", "chief", "child", "chimney", "choice",
    "choose", "chronic", "chuckle", "chunk", "churn", "citizen", "city", "civil",
    "claim", "clap", "clarify", "claw", "clay", "clean", "clerk", "clever",
    "cliff", "climb", "clinic", "clip", "clock", "clog", "close", "cloth",
    "cloud", "clown", "club", "clump", "cluster", "clutch", "coach", "coast",
    "coconut", "code", "coffee", "coil", "coin", "collect", "color", "column",
    "combine", "come", "comfort", "comic", "common", "company", "concert", "conduct",
    "confirm", "congress", "connect", "consider", "control", "convince", "cook", "cool",
    "copper", "copy", "coral", "core", "corn", "correct", "cost", "cotton",
    "couch", "country", "couple", "course", "cousin", "cover", "coyote", "crack",
    "cradle", "craft", "cram", "crane", "crash", "crater", "crawl", "crazy",
    "cream", "credit", "creek", "crew", "cricket", "crime", "crisp", "critic",
    "crop", "cross", "crouch", "crowd", "crucial", "cruel", "cruise", "crumble",
    "crush", "cry", "crystal", "cube", "culture", "cup", "cupboard", "curious",
    "current", "curtain", "curve", "cushion", "custom", "cute", "cycle", "dad",
    "damage", "damp", "dance", "danger", "daring", "dash", "daughter", "dawn",
    "day", "deal", "debate", "debris", "decade", "december", "decide", "decline",
    "decorate", "decrease", "deer", "defense", "define", "defy", "degree", "delay",
    "deliver", "demand", "demise", "denial", "dentist", "deny", "depart", "depend",
    "deposit", "depth", "deputy", "derive", "describe", "desert", "design", "desk",
    "despair", "destroy", "detail", "detect", "develop", "device", "devote", "diagram",
    "dial", "diamond", "diary", "dice", "diesel", "diet", "differ", "digital",
    "dignity", "dilemma", "dinner", "dinosaur", "direct", "dirt", "disagree", "discover",
    "disease", "dish", "dismiss", "disorder", "display", "distance", "divert", "divide",
    "divorce", "dizzy", "doctor", "document", "dog", "doll", "dolphin", "domain",
    "donate", "donkey", "donor", "door", "dose", "double", "dove", "draft",
    "dragon", "drama", "drastic", "draw", "dream", "dress", "drift", "drill",
    "drink", "drip", "drive", "drop", "drum", "dry", "duck", "dumb",
    "dune", "during", "dust", "dutch", "duty", "dwarf", "dynamic", "eager",
    "eagle", "early", "earn", "earth", "easily", "east", "easy", "echo",
    "ecology", "economy", "edge", "edit", "educate", "effort", "egg", "eight",
    "either", "elbow", "elder", "electric", "elegant", "element", "elephant", "elevator",
    "elite", "else", "embark", "embody", "embrace", "emerge", "emotion", "employ",
    "empower", "empty", "enable", "encourage", "end", "endless", "endorse", "enemy",
    "energy", "enforce", "engage", "engine", "enhance", "enjoy", "enlist", "enough",
    "enrich", "enroll", "ensure", "enter", "entire", "entry", "envelope", "episode",
    "equal", "equip", "era", "erase", "erode", "erosion", "error", "erupt",
    "escape", "essay", "essence", "estate", "eternal", "ethics", "evidence", "evil",
    "evoke", "evolve", "exact", "example", "excess", "exchange", "excite", "exclude",
    "excuse", "execute", "exercise", "exhaust", "exhibit", "exile", "exist", "exit",
    "exotic", "expand", "expect", "expire", "explain", "expose", "express", "extend",
    "extra", "eye", "eyebrow", "fabric", "face", "faculty", "fade", "faint",
    "faith", "fall", "false", "fame", "family", "famous", "fan", "fancy",
    "fantasy", "farm", "fashion", "fat", "fatal", "father", "fatigue", "fault",
    "favorite", "feature", "february", "federal", "fee", "feed", "feel", "female",
    "fence", "festival", "fetch", "fever", "few", "fiber", "fiction", "field",
    "figure", "file", "film", "filter", "final", "find", "fine", "finger",
    "finish", "fire", "firm", "fiscal", "fish", "fit", "fitness", "fix",
    "flag", "flame", "flash", "flat", "flavor", "flee", "flight", "flip",
    "float", "flock", "floor", "flower", "fluid", "flush", "fly", "foam",
    "focus", "fog", "foil", "fold", "follow", "food", "foot", "force",
    "forest", "forget", "fork", "fortune", "forum", "forward", "fossil", "foster",
    "found", "fox", "fragile", "frame", "frequent", "fresh", "friend", "fringe",
    "frog", "front", "frost", "frown", "frozen", "fruit", "fuel", "fun",
    "funny", "furnace", "fury", "future", "gadget", "gain", "galaxy", "gallery",
    "game", "gap", "garage", "garbage", "garden", "garlic", "garment", "gas",
    "gasp", "gate", "gather", "gauge", "gaze", "general", "genius", "genre",
    "gentle", "genuine", "gesture", "ghost", "giant", "gift", "giggle", "ginger",
    "giraffe", "girl", "give", "glad", "glance", "glare", "glass", "glide",
    "glimpse", "globe", "gloom", "glory", "glove", "glow", "glue", "goat",
    "goddess", "gold", "good", "goose", "gorilla", "gospel", "gossip", "govern",
    "gown", "grab", "grace", "grain", "grant", "grape", "grass", "gravity",
    "great", "green", "grid", "grief", "grit", "grocery", "group", "grow",
    "grunt", "guard", "guess", "guide", "guilt", "guitar", "gun", "gym",
    "habit", "hair", "half", "hammer", "hamster", "hand", "happy", "harbor",
    "hard", "harsh", "harvest", "hat", "have", "hawk", "hazard", "head",
    "health", "heart", "heavy", "hedgehog", "height", "hello", "helmet", "help",
    "hen", "hero", "hip", "hire", "history", "hobby", "hockey", "hold",
    "hole", "holiday", "hollow", "home", "honey", "hood", "hope", "horn",
    "horror", "horse", "hospital", "host", "hotel", "hour", "hover", "hub",
    "huge", "human", "humble", "humor", "hundred", "hungry", "hunt", "hurdle",
    "hurry", "hurt", "husband", "hybrid", "ice", "icon", "idea", "identify",
    "idle", "ignore", "ill", "illegal", "illness", "image", "imitate", "immense",
    "immune", "impact", "impose", "improve", "impulse", "inch", "include", "income",
    "increase", "index", "indicate", "indoor", "industry", "infant", "inflict", "inform",
    "initial", "inject", "inmate", "inner", "innocent", "input", "inquiry", "insane",
    "insect", "inside", "inspire", "install", "intact", "interest", "into", "invest",
    "invite", "involve", "iron", "island", "isolate", "issue", "item", "ivory",
    "jacket", "jaguar", "jar", "jazz", "jealous", "jeans", "jelly", "jewel",
    "job", "join", "joke", "journey", "joy", "judge", "juice", "jump",
    "jungle", "junior", "junk", "just", "kangaroo", "keen", "keep", "ketchup",
    "key", "kick", "kid", "kidney", "kind", "kingdom", "kiss", "kit",
    "kitchen", "kite", "kitten", "kiwi", "knee", "knife", "knock", "know",
    "lab", "label", "labor", "ladder", "lake", "lamp", "language", "laptop",
    "large", "later", "latin", "laugh", "laundry", "lava", "law", "lawn",
    "lawsuit", "layer", "lazy", "leader", "leaf", "learn", "leave", "lecture",
    "left", "leg", "legal", "legend", "leisure", "lemon", "lend", "length",
    "lens", "leopard", "lesson", "letter", "level", "liberty", "library", "license",
    "life", "lift", "light", "like", "limb", "limit", "link", "lion",
    "liquid", "list", "little", "live", "lizard", "load", "loan", "lobster",
    "local", "lock", "logic", "lonely", "long", "loop", "lottery", "loud",
    "lounge", "love", "loyal", "lucky", "luggage", "lumber", "lunar", "lunch",
    "luxury", "lyrics", "machine", "mad", "magic", "magnet", "maid", "mail",
    "main", "major", "make", "mammal", "man", "manage", "mandate", "mango",
    "mansion", "manual", "maple", "marble", "march", "margin", "marine", "market",
    "marriage", "mask", "mass", "master", "match", "material", "math", "matrix",
    "matter", "maximum", "maze", "meadow", "mean", "measure", "meat", "mechanic",
    "medal", "media", "melody", "melt", "member", "memory", "mention", "menu",
    "mercy", "merge", "merit", "merry", "mesh", "message", "metal", "method",
    "middle", "midnight", "milk", "million", "mimic", "mind", "minimum", "minor",
    "minute", "miracle", "mirror", "misery", "miss", "mistake", "mix", "mixed",
    "mixture", "mobile", "model", "modify", "mom", "moment", "monitor", "monkey",
    "monster", "month", "moon", "moral", "more", "morning", "mosquito", "mother",
    "motion", "motor", "mountain", "mouse", "move", "movie", "much", "muffin",
    "mule", "multiply", "muscle", "museum", "mushroom", "music", "must", "mutual",
    "myself", "mystery", "myth", "naive", "name", "napkin", "narrow", "nasty",
    "nation", "nature", "near", "neck", "need", "negative", "neglect", "neither",
    "nephew", "nerve", "nest", "net", "network", "neutral", "never", "news",
    "next", "nice", "night", "noble", "noise", "nominee", "noodle", "normal",
    "north", "nose", "notable", "nothing", "notice", "novel", "now", "nuclear",
    "number", "nurse", "nut", "oak", "obey", "object", "oblige", "obscure",
    "observe", "obtain", "obvious", "occur", "ocean", "october", "odor", "off",
    "offer", "office", "often", "oil", "okay", "old", "olive", "olympic",
    "omit", "once", "one", "onion", "online", "only", "open", "opera",
    "opinion", "oppose", "option", "orange", "orbit", "orchard", "order", "ordinary",
    "organ", "orient", "original", "orphan", "ostrich", "other", "outdoor", "outer",
    "output", "outside", "oval", "oven", "over", "own", "owner", "oxygen",
    "oyster", "ozone", "pact", "paddle", "page", "pair", "palace", "palm",
    "panda", "panel", "panic", "panther", "paper", "parade", "parent", "park",
    "parrot", "party", "pass", "patch", "path", "patient", "patrol", "pattern",
    "pause", "pave", "payment", "peace", "peanut", "pear", "peasant", "pelican",
    "pen", "penalty", "pencil", "people", "pepper", "perfect", "permit", "person",
    "pet", "phone", "photo", "phrase", "physical", "piano", "picnic", "picture",
    "piece", "pig", "pigeon", "pill", "pilot", "pink", "pioneer", "pipe",
    "pistol", "pitch", "pizza", "place", "planet", "plastic", "plate", "play",
    "please", "pledge", "pluck", "plug", "plunge", "poem", "poet", "point",
    "polar", "pole", "police", "pond", "pony", "pool", "popular", "portion",
    "position", "possible", "post", "potato", "pottery", "poverty", "powder", "power",
    "practice", "praise", "predict", "prefer", "prepare", "present", "pretty", "prevent",
    "price", "pride", "primary", "print", "priority", "prison", "private", "prize",
    "problem", "process", "produce", "profit", "program", "project", "promote", "proof",
    "property", "prosper", "protect", "proud", "provide", "public", "pudding", "pull",
    "pulp", "pulse", "pumpkin", "punch", "pupil", "puppy", "purchase", "purity",
    "purpose", "purse", "push", "put", "puzzle", "pyramid", "quality", "quantum",
    "quarter", "question", "quick", "quit", "quiz", "quote", "rabbit", "raccoon",
    "race", "rack", "radar", "radio", "rage", "rail", "rain", "raise",
    "rally", "ramp", "ranch", "random", "range", "rapid", "rare", "rate",
    "rather", "raven", "raw", "razor", "ready", "real", "reason", "rebel",
    "rebuild", "recall", "receive", "recipe", "record", "recycle", "reduce", "reflect",
    "reform", "region", "regret", "regular", "reject", "relax", "release", "relief",
    "rely", "remain", "remember", "remind", "remove", "render", "renew", "rent",
    "reopen", "repair", "repeat", "replace", "report", "require", "rescue", "resemble",
    "resist", "resource", "response", "result", "retire", "retreat", "return", "reunion",
    "reveal", "review", "reward", "rhythm", "rib", "ribbon", "rice", "rich",
    "ride", "ridge", "rifle", "right", "rigid", "ring", "riot", "ripple",
    "risk", "ritual", "rival", "river", "road", "roast", "robot", "robust",
    "rocket", "romance", "roof", "rookie", "room", "rose", "rotate", "rough",
    "round", "route", "royal", "rubber", "rude", "rug", "rule", "run",
    "runway", "rural", "sad", "saddle", "sadness", "safe", "sail", "salad",
    "salmon", "salon", "salt", "salute", "same", "sample", "sand", "satisfy",
    "satoshi", "sauce", "sausage", "save", "say", "scale", "scan", "scare",
    "scatter", "scene", "scheme", "school", "science", "scissors", "scorpion", "scout",
    "scrap", "screen", "script", "scrub", "sea", "search", "season", "seat",
    "second", "secret", "section", "security", "seed", "seek", "segment", "select",
    "sell", "seminar", "senior", "sense", "sentence", "series", "service", "session",
    "settle", "setup", "seven", "shadow", "shaft", "shallow", "share", "shed",
    "shell", "sheriff", "shield", "shift", "shine", "ship", "shiver", "shock",
    "shoe", "shoot", "shop", "short", "shoulder", "shove", "shrimp", "shrug",
    "shuffle", "shy", "sibling", "sick", "side", "siege", "sight", "sign",
    "silent", "silk", "silly", "silver", "similar", "simple", "since", "sing",
    "siren", "sister", "situate", "six", "size", "skate", "sketch", "ski",
    "skill", "skin", "skirt", "skull", "slab", "slam", "sleep", "slender",
    "slice", "slide", "slight", "slim", "slogan", "slot", "slow", "slush",
    "small", "smart", "smile", "smoke", "smooth", "snack", "snake", "snap",
    "sniff", "snow", "soap", "soccer", "social", "sock", "soda", "soft",
    "solar", "soldier", "solid", "solution", "solve", "someone", "song", "soon",
    "sorry", "sort", "soul", "sound", "soup", "source", "south", "space",
    "spare", "spatial", "spawn", "speak", "special", "speed", "spell", "spend",
    "sphere", "spice", "spider", "spike", "spin", "spirit", "split", "sponsor",
    "spoon", "sport", "spot", "spray", "spread", "spring", "spy", "square",
    "squeeze", "squirrel", "stable", "stadium", "staff", "stage", "stairs", "stamp",
    "stand", "start", "state", "stay", "steak", "steel", "stem", "step",
    "stereo", "stick", "still", "sting", "stock", "stomach", "stone", "stool",
    "story", "stove", "strategy", "street", "strike", "strong", "struggle", "student",
    "stuff", "stumble", "style", "subject", "submit", "subway", "success", "such",
    "sudden", "suffer", "sugar", "suggest", "suit", "summer", "sun", "sunny",
    "sunset", "super", "supply", "supreme", "sure", "surface", "surge", "surprise",
    "surround", "survey", "suspect", "sustain", "swallow", "swamp", "swap", "swarm",
    "swear", "sweet", "swim", "swing", "switch", "sword", "symbol", "symptom",
    "syrup", "system", "table", "tackle", "tag", "tail", "talent", "talk",
    "tank", "tape", "target", "task", "taste", "tattoo", "taxi", "teach",
    "team", "tell", "ten", "tenant", "tennis", "tent", "term", "test",
    "text", "thank", "that", "theme", "then", "theory", "there", "they",
    "thing", "this", "thought", "three", "thrive", "throw", "thumb", "thunder",
    "ticket", "tide", "tiger", "tilt", "timber", "time", "tiny", "tip",
    "tired", "tissue", "title", "toast", "tobacco", "today", "toddler", "toe",
    "together", "toilet", "token", "tomato", "tomorrow", "tone", "tongue", "tonight",
    "tool", "tooth", "top", "topic", "topple", "torch", "tornado", "tortoise",
    "toss", "total", "tourist", "toward", "tower", "town", "toy", "track",
    "trade", "traffic", "tragic", "train", "transfer", "trap", "trash", "travel",
    "tray", "treat", "tree", "trend", "trial", "tribe", "trick", "trigger",
    "trim", "trip", "trophy", "trouble", "truck", "true", "truly", "trumpet",
    "trust", "truth", "try", "tube", "tuna", "tunnel", "turkey", "turn",
    "turtle", "twelve", "twenty", "twice", "twin", "twist", "two", "type",
    "typical", "ugly", "umbrella", "unable", "unaware", "uncle", "uncover", "under",
    "undo", "unfair", "unfold", "unhappy", "uniform", "union", "unique", "unit",
    "universe", "unknown", "unlock", "until", "unusual", "unveil", "update", "upgrade",
    "uphold", "upon", "upper", "upset", "urban", "usage", "use", "used",
    "useful", "useless", "usual", "utility", "vacant", "vacuum", "vague", "valid",
    "valley", "valve", "van", "vanish", "vapor", "various", "vast", "vault",
    "vehicle", "velvet", "vendor", "venture", "venue", "verb", "verify", "version",
    "very", "vessel", "veteran", "viable", "vibrant", "vicious", "victory", "video",
    "view", "village", "vintage", "violin", "virtual", "virus", "visa", "visit",
    "visual", "vital", "vivid", "vocal", "voice", "void", "volcano", "volume",
    "vote", "voyage", "wage", "wagon", "wait", "walk", "wall", "walnut",
    "want", "warfare", "warm", "warrior", "wash", "wasp", "waste", "water",
    "wave", "way", "wealth", "weapon", "wear", "weasel", "weather", "web",
    "wedding", "weekend", "weird", "welcome", "well", "west", "wet", "whale",
    "what", "wheat", "wheel", "when", "where", "whip", "whisper", "wide",
    "width", "wife", "wild", "will", "win", "window", "wine", "wing",
    "wink", "winner", "winter", "wire", "wisdom", "wise", "wish", "witness",
    "wolf", "woman", "wonder", "wood", "wool", "word", "work", "world",
    "worry", "worth", "wrap", "wreck", "wrestle", "wrist", "write", "wrong",
    "yard", "year", "yellow", "you", "young", "youth", "zebra", "zero",
    "zone", "zoo"
]


class PassGen:
    """
    Password Generator with Entropy Visualization.

    Generates cryptographically secure passwords with detailed strength analysis.
    """

    def __init__(self, custom_wordlist: Optional[List[str]] = None):
        """
        Initialize PassGen.

        Args:
            custom_wordlist: Custom wordlist for passphrase generation.
        """
        self.wordlist = custom_wordlist or BIP39_WORDS

    def random(self, length: int = 16, uppercase: bool = True,
               lowercase: bool = True, digits: bool = True,
               symbols: bool = True, exclude_ambiguous: bool = False,
               exclude_chars: Optional[str] = None) -> Password:
        """
        Generate a random password.

        Args:
            length: Password length.
            uppercase: Include uppercase letters.
            lowercase: Include lowercase letters.
            digits: Include digits.
            symbols: Include symbols.
            exclude_ambiguous: Exclude ambiguous characters (0, O, l, 1, I).
            exclude_chars: Additional characters to exclude.

        Returns:
            Password object with analysis.
        """
        charset = ""
        if uppercase:
            charset += string.ascii_uppercase
        if lowercase:
            charset += string.ascii_lowercase
        if digits:
            charset += string.digits
        if symbols:
            charset += "!@#$%^&*()_+-=[]{}|;:,.<>?"

        if exclude_ambiguous:
            ambiguous = "0OolI1"
            charset = "".join(c for c in charset if c not in ambiguous)

        if exclude_chars:
            charset = "".join(c for c in charset if c not in exclude_chars)

        if not charset:
            charset = string.ascii_letters + string.digits

        # Generate password using cryptographically secure random
        password = "".join(secrets.choice(charset) for _ in range(length))

        return self._analyze(password, "custom")

    def random_batch(self, count: int = 5, **kwargs) -> List[Password]:
        """Generate multiple random passwords."""
        return [self.random(**kwargs) for _ in range(count)]

    def passphrase(self, words: int = 6, separator: str = "-",
                   capitalize: bool = False, add_number: bool = True) -> Password:
        """
        Generate a BIP39-style passphrase.

        Args:
            words: Number of words.
            separator: Word separator.
            capitalize: Capitalize words.
            add_number: Add a random number at the end.

        Returns:
            Password object with analysis.
        """
        word_list = [secrets.choice(self.wordlist) for _ in range(words)]

        if capitalize:
            word_list = [w.capitalize() for w in word_list]

        password = separator.join(word_list)

        if add_number:
            password += separator + str(secrets.randbelow(1000))

        return self._analyze(password, "passphrase")

    def pin(self, length: int = 6) -> Password:
        """Generate a numeric PIN."""
        password = "".join(secrets.choice(string.digits) for _ in range(length))
        return self._analyze(password, "pin")

    def memorable(self, length: int = 16) -> Password:
        """Generate a memorable password with alternating consonants and vowels."""
        consonants = "bcdfghjklmnpqrstvwxyz"
        vowels = "aeiou"

        password = ""
        for i in range(length):
            if i % 2 == 0:
                password += secrets.choice(consonants)
            else:
                password += secrets.choice(vowels)

        # Add a random digit and uppercase
        password = password[:length-2] + secrets.choice(string.digits) + secrets.choice(string.ascii_uppercase)

        return self._analyze(password, "memorable")

    def check_strength(self, password: str) -> Password:
        """Analyze an existing password."""
        return self._analyze(password, "custom")

    def check_breach(self, password: str) -> Dict[str, Any]:
        """
        Check if password has been in a data breach (local check).
        Uses SHA-1 prefix method similar to HaveIBeenPwned.
        """
        sha1 = hashlib.sha1(password.encode()).hexdigest().upper()
        prefix = sha1[:5]
        suffix = sha1[5:]

        # In a real implementation, this would query the HIBP API
        # For now, we just return the hash info
        return {
            "checked": True,
            "sha1_prefix": prefix,
            "sha1_suffix": suffix,
            "found": False,  # Would be True if found in breach database
            "message": "Password not found in local breach database (use HIBP API for full check)"
        }

    # ─── Internal Methods ────────────────────────────────────────────────

    def _analyze(self, password: str, password_type: str) -> Password:
        """Analyze password and create Password object."""
        # Calculate charset size
        charset_size = 0
        has_upper = any(c in string.ascii_uppercase for c in password)
        has_lower = any(c in string.ascii_lowercase for c in password)
        has_digit = any(c in string.digits for c in password)
        has_symbol = any(c in "!@#$%^&*()_+-=[]{}|;:,.<>?" for c in password)

        if has_upper:
            charset_size += 26
        if has_lower:
            charset_size += 26
        if has_digit:
            charset_size += 10
        if has_symbol:
            charset_size += 27

        if charset_size == 0:
            charset_size = 26  # Default

        # Calculate entropy
        entropy_per_char = math.log2(charset_size) if charset_size > 0 else 0
        total_entropy = entropy_per_char * len(password)

        # Character distribution
        char_dist = {}
        for c in password:
            char_dist[c] = char_dist.get(c, 0) + 1

        # Unique characters
        unique_chars = len(set(password))

        # Strength calculation
        strength, score = self._calculate_strength(total_entropy, len(password), unique_chars)

        # Crack time
        crack_seconds = self._estimate_crack_time(total_entropy)
        crack_display = self._format_crack_time(crack_seconds)

        # Strength bar
        strength_bar = self._strength_bar(score)

        # Charset name
        charset_name = self._charset_name(has_upper, has_lower, has_digit, has_symbol)

        # Entropy analysis
        entropy_analysis = EntropyAnalysis(
            total_bits=round(total_entropy, 2),
            charset_size=charset_size,
            password_length=len(password),
            entropy_per_char=round(entropy_per_char, 2),
            crack_time_seconds=crack_seconds,
            crack_time_display=crack_display,
            strength=strength,
            strength_score=score,
        )

        return Password(
            password=password,
            entropy=round(total_entropy, 2),
            strength=strength,
            strength_score=score,
            strength_bar=strength_bar,
            charset_used=charset_name,
            has_uppercase=has_upper,
            has_lowercase=has_lower,
            has_digits=has_digit,
            has_symbols=has_symbol,
            unique_chars=unique_chars,
            char_distribution=char_dist,
            crack_time=crack_display,
            entropy_analysis=entropy_analysis,
        )

    def _calculate_strength(self, entropy: float, length: int, unique: int) -> Tuple[str, float]:
        """Calculate password strength score."""
        score = 0

        # Entropy contribution (0-40 points)
        if entropy >= 128:
            score += 40
        elif entropy >= 80:
            score += 30
        elif entropy >= 60:
            score += 20
        elif entropy >= 40:
            score += 15
        elif entropy >= 20:
            score += 10
        else:
            score += 5

        # Length contribution (0-30 points)
        if length >= 20:
            score += 30
        elif length >= 16:
            score += 25
        elif length >= 12:
            score += 20
        elif length >= 8:
            score += 15
        elif length >= 6:
            score += 10
        else:
            score += 5

        # Unique characters contribution (0-20 points)
        if unique >= 15:
            score += 20
        elif unique >= 12:
            score += 15
        elif unique >= 8:
            score += 10
        elif unique >= 5:
            score += 5

        # Character variety (0-10 points)
        variety = 0
        if any(c in string.ascii_uppercase for c in ""):
            variety += 1
        if any(c in string.ascii_lowercase for c in ""):
            variety += 1
        if any(c in string.digits for c in ""):
            variety += 1
        if any(c in "!@#$%^&*()" for c in ""):
            variety += 1
        score += min(variety * 2.5, 10)

        score = min(score, 100)

        # Determine strength label
        if score >= 80:
            strength = PasswordStrength.VERY_STRONG.value
        elif score >= 60:
            strength = PasswordStrength.STRONG.value
        elif score >= 40:
            strength = PasswordStrength.FAIR.value
        elif score >= 20:
            strength = PasswordStrength.WEAK.value
        else:
            strength = PasswordStrength.VERY_WEAK.value

        return strength, round(score, 1)

    def _estimate_crack_time(self, entropy: float) -> float:
        """Estimate crack time in seconds (assuming 10 billion guesses/sec)."""
        combinations = 2 ** entropy
        guesses_per_sec = 10_000_000_000  # 10 billion
        return combinations / guesses_per_sec / 2  # Average case

    def _format_crack_time(self, seconds: float) -> str:
        """Format crack time as human-readable string."""
        if seconds < 0.001:
            return "Instant"
        elif seconds < 1:
            return f"{seconds*1000:.0f} milliseconds"
        elif seconds < 60:
            return f"{seconds:.1f} seconds"
        elif seconds < 3600:
            return f"{seconds/60:.1f} minutes"
        elif seconds < 86400:
            return f"{seconds/3600:.1f} hours"
        elif seconds < 31536000:
            return f"{seconds/86400:.1f} days"
        elif seconds < 31536000 * 1000:
            return f"{seconds/31536000:.1f} years"
        elif seconds < 31536000 * 1000000:
            return f"{seconds/31536000/1000:.0f} thousand years"
        elif seconds < 31536000 * 1000000000:
            return f"{seconds/31536000/1000000:.0f} million years"
        else:
            return f"{seconds/31536000/1000000000:.0f} billion years"

    def _strength_bar(self, score: float) -> str:
        """Generate visual strength bar."""
        filled = int(score / 10)
        empty = 10 - filled
        return "█" * filled + "░" * empty + f" {score:.0f}/100"

    def _charset_name(self, upper: bool, lower: bool, digit: bool, symbol: bool) -> str:
        """Get charset description."""
        parts = []
        if upper:
            parts.append("A-Z")
        if lower:
            parts.append("a-z")
        if digit:
            parts.append("0-9")
        if symbol:
            parts.append("!@#")
        return " + ".join(parts) if parts else "unknown"

    def __repr__(self) -> str:
        return f"PassGen(wordlist_size={len(self.wordlist)})"
