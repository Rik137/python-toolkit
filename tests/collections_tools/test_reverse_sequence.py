import pytest
from toolkit.collections_tools.collections_tools import reverse_sequence

def test_reverse_sequence_list():
    assert reverse_sequence([1, 2, 3, 4]) == [4, 3, 2, 1]

def test_reverse_sequence_tuple():
    assert reverse_sequence((1, 2, 3, 4)) == (4, 3, 2, 1)

def test_reverse_sequence_str():
    assert reverse_sequence("Hello World") == "dlroW olleH"

def test_reverse_sequence_none():
    with pytest.raises(TypeError):
        reverse_sequence(None)

def test_reverse_sequence_empty():
    assert reverse_sequence([]) == []

def test_reverse_sequence_set():
    with pytest.raises(TypeError):
        reverse_sequence(set())

def test_reverse_sequence_dict():
    with pytest.raises(KeyError):
        reverse_sequence(dict())


