from __future__ import annotations

LETTERS_VALUES = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000
}


def roman_to_integer(s: str) -> int:
    reversed_s = s[::-1]

    cur_max = 1

    result = 0
    for letter in reversed_s:
        letter_value = LETTERS_VALUES[letter]

        if letter_value > cur_max:
            result += letter_value
            cur_max = letter_value
        elif letter_value == cur_max:
            result += letter_value
        else:
            result -= letter_value

    return result
