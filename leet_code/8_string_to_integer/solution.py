from __future__ import annotations


MIN = -2**31
MAX = 2**31 - 1


def is_32_bits_integer(x: int) -> bool:
    return x <= 2**31 - 1 and x >= -2**31


def string_to_integer(s: str) -> int:
    dig_arr = []
    started_digits = False
    is_positive = True

    for char in s:
        if started_digits:
            if char.isnumeric():
                dig_arr.append(char)
            else:
                break
        else:
            if char.isspace():
                pass
            elif char == "+" or char == "-":
                is_positive = char == "+"
                started_digits = True
            elif char.isnumeric():
                started_digits = True
                dig_arr.append(char)
            else:
                break

    if len(dig_arr) == 0:
        return 0

    num = int("".join(dig_arr))
    num = num if is_positive else -num

    if num > MAX:
        return MAX

    if num < MIN:
        return MIN

    return num
