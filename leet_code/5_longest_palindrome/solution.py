from __future__ import annotations


def longest_palindrome(s: str) -> int:
    s_with_divider = "|" + "|".join([char for char in s]) + "|"
    s_size = len(s_with_divider)

    max_radius = 0
    center_for_max_radius = 0

    for idx in range(len(s_with_divider)):
        radius = 1

        while idx-radius >= 0 and idx+radius < s_size and s_with_divider[idx-radius] == s_with_divider[idx+radius]:
            radius += 1

        if(radius-1 > max_radius):
            max_radius = radius-1
            center_for_max_radius = idx

    response = s_with_divider[center_for_max_radius -
                              max_radius: center_for_max_radius+max_radius+1]
    response_without_dividers = response.replace("|", "")

    return response_without_dividers
