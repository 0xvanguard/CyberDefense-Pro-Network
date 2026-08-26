"""
ConstitutionalKit — Constitutional AI Implementation
"""

from .kit import ConstitutionalKit, Principle, Violation, EvalResult
from .principles_library import (
    get_all_principles,
    get_principles_by_category,
    get_principle_stats,
    ALL_CATEGORIES,
)

__version__ = "2.0.0"
__all__ = [
    "ConstitutionalKit",
    "Principle",
    "Violation",
    "EvalResult",
    "get_all_principles",
    "get_principles_by_category",
    "get_principle_stats",
    "ALL_CATEGORIES",
]
