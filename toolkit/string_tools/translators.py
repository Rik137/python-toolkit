"""
Translators for various languages and coding systems.
"""

from toolkit.constants.const import MORSE_CODE
from toolkit.errors.Exceptions import MorseCodeError

def string_to_morse_code(string: str) -> str:
    """
        Convert string to Morse code.

        Uses ' ' as a separator between characters
        and '   ' as a separator between words.
        """
    if not isinstance(string, str):
        raise TypeError("Input must be a string")

    words = []

    for word in string.lower().split(" "):
        letters = []
        for char in word:
            code = MORSE_CODE.get(char)
            if code is None:
                raise MorseCodeError(f"Unsupported character: {char}")
            letters.append(code)

        words.append(" ".join(letters))  # 1 пробел между буквами

    return "   ".join(words)


