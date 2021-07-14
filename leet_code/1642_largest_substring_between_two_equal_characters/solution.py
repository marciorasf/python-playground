from __future__ import annotations


def max_length_between_equal_characters(s: str) -> int:
    first_occurrences = {}

    largest = -1

    for idx, letter in enumerate(s):
        if letter in first_occurrences:
            distance = idx - first_occurrences[letter] - 1 
            largest = max(largest, distance)
        else:
            first_occurrences[letter] = idx

    return largest
