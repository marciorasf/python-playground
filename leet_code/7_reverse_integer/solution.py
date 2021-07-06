from __future__ import annotations


def is_32_bits_integer(x: int) -> bool:
    return x <= 2**31 - 1 and x >= -2**31


def reverse_integer(x: int) -> int:
    if not is_32_bits_integer(x):
        return 0

    is_negative = x < 0
    x_str = str(abs(x))

    new_int = []

    for idx in range(len(x_str)-1, -1, -1):
        new_int.append(x_str[idx])

    new_int = "".join(new_int)

    new_int = int(new_int)

    if not is_32_bits_integer(new_int):
        return 0

    return -new_int if is_negative else new_int
