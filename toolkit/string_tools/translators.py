"""
Translators for various languages and coding systems.
"""

from toolkit.constants.const import MORSE_CODE
from toolkit.errors.Exceptions import MorseCodeError

def string_to_morse_code(string: str) -> str:
    """
        Convert string to Morse code.

        Uses '|' as a separator between characters
        and '/' as a separator between words.
        """
    morse_chars = []
    for char in string.lower():
        if char == " ":
            morse_chars.append("/")
            continue
        code = MORSE_CODE.get(char)
        if code is None:
            raise MorseCodeError(f"Unsupported character: {char}")
        morse_chars.append(code)
    return "|".join(morse_chars)


