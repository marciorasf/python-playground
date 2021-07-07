from __future__ import annotations


def longest_common_prefix(strs: list[str]) -> str:
    prefix = ""

    str_min_length = min([len(s) for s in strs])
    finished = False
    for idx in range(str_min_length):
        first_string_letter = strs[0][idx]

        for s in strs:
            if s[idx] != first_string_letter:
                finished = True
                break

        if finished:
            break

        prefix += first_string_letter

    return prefix
