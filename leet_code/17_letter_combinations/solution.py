from __future__ import annotations

DIGIT_TO_LETTER = {
    "2": "abc",
    "3": "def",
    "4": "ghi",
    "5": "jkl",
    "6": "mno",
    "7": "pqrs",
    "8": "tuv",
    "9": "wxyz",
}


def letter_combinations(digits: str) -> list[str]:
    if len(digits) == 0:
        return []

    n_combinations = 1
    for digit in digits:
        n_combinations *= len(DIGIT_TO_LETTER[digit])

    combinations = [""] * n_combinations

    repeat_size = n_combinations
    for dig in digits:
        letters = DIGIT_TO_LETTER[dig]

        repeat_size = repeat_size // len(letters)

        combinations = [s + letters[(idx // repeat_size) % len(letters)]
                        for idx, s in enumerate(combinations)]

    return combinations
