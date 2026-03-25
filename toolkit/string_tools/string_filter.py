from typing import Iterable
from toolkit.constants.const import  VOWELS

"""
String filtering utilities.
"""

def filter_strings_containing(items: list[str], query: str) -> list[str]:
    """ Return all strings that contain the given substring """
    return [s for s in items if query in s]

def remove_vowels(items: str | None) -> str | None:
    """
    Remove all vowels from the given string.
    Return None if the string is empty.
    """
    if not items:
        return None
    return "".join(s for s in items if s not in VOWELS)

def get_longest_string(items: Iterable[str] | None) -> str | None:
    """
    Return the longest string from the given iterable.
    Return None if items is None or empty.
    """
    if not items:
        return None
    try:
        return max(items, key=len)
    except ValueError:
        return None

def filter_even_length_strings(items: Iterable[str] | None) -> list[str] | None:
    """
    Return strings with even length from the given iterable.
    Return None if items is None.
    Return empty list if no even-length strings are found.
    """
    if items is None:
        return None
    return [s for s in items if len(s) % 2 == 0]

def filter_type_str(items: Iterable) -> list[str]:
    """Return only string elements from iterable."""
    return [s for s in items if isinstance(s, str)]
