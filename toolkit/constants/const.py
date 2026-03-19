from typing import TypeVar
"""Constants for string_toolkit"""

T = TypeVar("T")

def get_vowels() -> set[str]:
    """Return a set with all English vowels."""
    return {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}