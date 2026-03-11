"""
String filtering utilities.
"""

def filter_strings_containing(items: list[str], query: str) -> list[str]:
    """ Return all strings that contain the given substring """
    return [s for s in items if query in s]


