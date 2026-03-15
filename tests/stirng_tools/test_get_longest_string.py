from toolkit.string_tools.string_filter import get_longest_string

def test_get_longest_string_basic():
    assert get_longest_string(["apple", "banana", "pear"]) == "banana"

def test_get_longest_string_empty_list():
    assert get_longest_string([]) is None

def test_get_longest_string_none():
    assert get_longest_string(None) is None

def test_get_longest_string_same_length():
    assert get_longest_string(["apple", "pears"]) == "apple"

def test_get_longest_string_one_element():
    assert get_longest_string(["apple"]) == "apple"

def test_get_longest_string_generator():
    data = (x for x in ["a", "bbb", "cc"])
    assert get_longest_string(data) == "bbb"

def test_get_longest_string_tuple():
    assert get_longest_string(("a", "bbb", "cc")) == "bbb"

def test_get_longest_string_empty_generator():
    data = (x for x in [])
    assert get_longest_string(data) is None