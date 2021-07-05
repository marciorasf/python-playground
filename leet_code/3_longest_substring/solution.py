from __future__ import annotations


def length_of_longest_substring(s: str) -> int:
    def calc_new_map(char_map, start_idx):
        new_map = dict()
        for char, char_idx in char_map.items():
            if char_idx >= start_idx:
                new_map[char] = char_idx

        return new_map

    char_map = dict()
    start_idx = 0
    max_length = 0

    for idx, char in enumerate(s):
        if char in char_map:
            max_length = max(len(char_map), max_length)
            start_idx = char_map[char] + 1
            char_map = calc_new_map(char_map, start_idx)

        char_map[char] = idx

    max_length = max(len(char_map), max_length)

    return max_length
