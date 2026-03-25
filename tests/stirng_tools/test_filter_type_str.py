import pytest

from toolkit.string_tools.string_filter import filter_type_str


def test_filter_type_str_mixed_types():
    data = ["hello", "world", 34, (3, 4), {"Hello"}]
    assert filter_type_str(data) == ["hello", "world"]


def test_filter_type_str_empty_iterable():
    assert filter_type_str([]) == []


def test_filter_type_str_no_strings():
    assert filter_type_str([1, 2, 3, 4.5, True]) == []


def test_filter_type_str_all_strings():
    assert filter_type_str(["a", "b", "c"]) == ["a", "b", "c"]


def test_filter_type_str_ignores_nested_strings():
    data = [1, [2, "hello"], ("world",), {"a"}]
    assert filter_type_str(data) == []


def test_filter_type_str_tuple_input():
    data = ("a", 1, "b")
    assert filter_type_str(data) == ["a", "b"]


def test_filter_type_str_set_input():
    data = {"a", 1, "b"}
    result = filter_type_str(data)
    assert sorted(result) == ["a", "b"]


def test_filter_type_str_generator_input():
    data = (x for x in ["a", 1, "b"])
    assert filter_type_str(data) == ["a", "b"]
