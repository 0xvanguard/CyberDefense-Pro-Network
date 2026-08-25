"""
PromptKiller - AI Attack Prompt Library
The most comprehensive library for AI red teaming and security testing.
"""

from .promptkiller import PromptKiller
from .categories import CATEGORIES, SEVERITY_LEVELS

__version__ = "1.0.0"
__author__ = "0xvanguard"
__all__ = ["PromptKiller", "CATEGORIES", "SEVERITY_LEVELS"]
