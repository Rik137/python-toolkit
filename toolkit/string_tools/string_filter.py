"""
String filtering utilities.
"""

def filter_strings_containing(items: list[str], query: str) -> list[str]:
    """ Return all strings that contain the given substring """
    return [s for s in items if query in s]

def get_vowels() -> set[str]:
    """Return a set with all English vowels."""
    return {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}

def remove_vowels(items: str | None) -> str | None:
    """
    Remove all vowels from the given string.
    Return None if the string is empty.
    """
    if not items:
        return None
    vowels = get_vowels()
    return "".join(s for s in items if s not in vowels)