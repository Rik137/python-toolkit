from toolkit.string_tools.string_filter import filter_strings_containing, remove_vowels

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

def test_remove_vowels_basic():
    assert remove_vowels("hello world") == "hll wrld"

def test_remove_vowels_no_vowels():
    assert remove_vowels("hll wrld") == "hll wrld"

def test_remove_vowels_empty_string():
    assert remove_vowels("") is None

def test_remove_vowels_input_none():
    assert remove_vowels(None) is None