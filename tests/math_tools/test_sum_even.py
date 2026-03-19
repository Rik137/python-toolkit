from toolkit.math_tools.math_tools import sum_even

def test_sum_even_with_even_numbers():
    assert sum_even([2, 2, 3]) == 4

def test_sum_even_with_no_even_numbers():
    assert sum_even([3, 3, 3,]) == 0

def test_sum_even_empty_list():
    assert sum_even([]) is None

def test_sum_even_with_none_input():
    assert sum_even(None) is None




