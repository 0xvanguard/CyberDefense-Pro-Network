"""
JailbreakBench - Standardized LLM Jailbreak Evaluation
"""

from .benchmark import JailbreakBench
from .scorer import Scorer

__version__ = "1.0.0"
__all__ = ["JailbreakBench", "Scorer"]
