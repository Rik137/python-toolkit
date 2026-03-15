from toolkit.string_tools.string_filter import remove_vowels

def test_remove_vowels_basic():
    assert remove_vowels("hello world") == "hll wrld"

def test_remove_vowels_no_vowels():
    assert remove_vowels("hll wrld") == "hll wrld"

def test_remove_vowels_empty_string():
    assert remove_vowels("") is None

def test_remove_vowels_input_none():
    assert remove_vowels(None) is None