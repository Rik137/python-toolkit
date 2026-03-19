from toolkit.math_tools.math_tools import sum_if_less_than, sum_even

def test_sum_if_less_than_basic():
    assert sum_if_less_than(50, 10, 10, 10) == 30

def test_sum_if_less_than_big():
    assert sum_if_less_than(10, 10, 10, 10) is None

def test_sum_if_less_than_args_is_empty():
    assert sum_if_less_than(10) is None

def test_sum_if_less_than_equals_query():
    assert sum_if_less_than(30, 10, 20) is None