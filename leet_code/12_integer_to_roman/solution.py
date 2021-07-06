from __future__ import annotations


def make_map(one: str, five: str, ten: str):
    return {
        "0": "",
        "1": one,
        "2": one+one,
        "3": one+one+one,
        "4": one+five,
        "5": five,
        "6": five+one,
        "7": five+one+one,
        "8": five+one+one+one,
        "9": one+ten,
    }


SETS = [
    ("I", "V", "X"),
    ("X", "L", "C"),
    ("C", "D", "M"),
    ("M", "", ""),
]


def integer_to_roman(num: int) -> str:
    inner_num = num

    roman = []

    set_idx = 0
    while inner_num > 0:
        digit = str(inner_num % 10)
        map = make_map(*SETS[set_idx])
        roman.append(map[digit])

        inner_num //= 10
        set_idx += 1

    roman.reverse()
    return "".join(roman)
