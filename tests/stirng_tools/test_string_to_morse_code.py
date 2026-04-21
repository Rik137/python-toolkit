import pytest
from toolkit.errors.Exceptions import MorseCodeError
from toolkit.string_tools.translators import string_to_morse_code

def test_string_to_morse_code_base():
    assert string_to_morse_code("hello world") == ".... . .-.. .-.. ---   .-- --- .-. .-.. -.."

def test_string_to_morse_code_if_empty():
    assert string_to_morse_code("") == ""

def test_string_to_morse_code_if_morse_code_error():
    with pytest.raises(MorseCodeError, match="Unsupported character"):
        string_to_morse_code("%")

def test_string_to_morse_code_if_no_string_type():
    with pytest.raises(TypeError, match= "Input must be a string"):
        string_to_morse_code(23343)
