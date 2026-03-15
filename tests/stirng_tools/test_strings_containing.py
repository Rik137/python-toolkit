from toolkit.string_tools.string_filter import filter_strings_containing, remove_vowels, get_longest_string

def test_filter_strings_basic():
    data = ["apple", "banana", "pear"]
    result = filter_strings_containing(data, "a")
    assert result == ["apple", "banana", "pear"]

def test_filter_no_match():
    data = ["apple", "banana", "pear"]
    result = filter_strings_containing(data, "z")
    assert  result == []


def test_filter_empty_string():
    data = ["apple", "banana", "pear", ""]
    result = filter_strings_containing(data, "")
    assert result == ["apple", "banana", "pear", ""]

def test_filter_empty_list():
    data = []
    result = filter_strings_containing(data, "")
    assert result == []
