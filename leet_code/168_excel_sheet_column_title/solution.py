from __future__ import annotations
import math


def number_to_letter(n: int) -> str:
    return chr(ord("A") + n)


def convert_to_title(column_number: int) -> str:
    title = []
    n_left = column_number

    while n_left >= 1:
        rest = ((n_left - 1) % 26) + 1
        title.append(number_to_letter(math.floor(rest- 1 )))

        n_left = (n_left - rest) / 26

    title.reverse()

    return "".join(title)
