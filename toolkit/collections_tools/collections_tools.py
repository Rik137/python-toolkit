from toolkit.constants.const import T

"""
Module with utility functions for working with collections.
Supports: list, tuple, set, frozenset, dict.
"""

def reverse_sequence(items: T) -> T:
    """
    Reverse a sequence (list, tuple, or string).
    """
    return items[::-1]