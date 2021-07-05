from __future__ import annotations


def is_palindrome(x: int) -> bool:
    if x < 0:
        return False

    rest = x
    arr = []

    # transform in array
    while rest > 0:
        arr.append(rest % 10)
        rest = rest // 10

    start = 0
    end = len(arr)-1

    while start < end:
        if arr[start] != arr[end]:
            return False

        start += 1
        end -= 1

    return True
