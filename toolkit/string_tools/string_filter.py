from constants import get_vowels

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
    vowels = get_vowels()
    return "".join(s for s in items if s not in vowels)