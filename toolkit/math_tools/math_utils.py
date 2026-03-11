"""
Work with math operations.
"""

def sum_if_less_than(query, *args: int) -> int | None:
    """
        Return the sum of args if the sum is less than query.
        Return None if no args are provided or sum >= query.
    """
    if not args:
        return None
    total = sum(args)
    return total if total < query else None


