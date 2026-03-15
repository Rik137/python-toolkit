from toolkit.string_tools.string_filter import filter_even_length_strings

def test_filter_even_length_strings_basic_list():
    assert filter_even_length_strings(["bear", "banana", "apple"]) == ["bear", "banana"]

def test_filter_even_length_strings_basic_tuple():
    assert filter_even_length_strings(("bear", "banana", "apple")) == ["bear", "banana"]

def test_filter_even_length_strings_set():
    assert sorted(filter_even_length_strings({"bear", "banana", "apple"})) == ["banana", "bear"]

def test_filter_even_length_strings_generator():
    data = (s for s in ["apple", "pears", "banana"])
    assert filter_even_length_strings(data) == ["banana"]

def test_filter_even_length_strings_no_even():
    assert filter_even_length_strings(["apple", "pears"]) == []

def test_filter_even_length_strings_empty_iterable():
    assert filter_even_length_strings([]) == []

def test_filter_even_length_strings_none_iterable():
    assert filter_even_length_strings(None) is None