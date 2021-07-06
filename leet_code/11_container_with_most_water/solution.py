from __future__ import annotations


def calc_area(x_0, y_0, x_1, y_1):
    return abs(x_1 - x_0) * min(y_0, y_1)


def max_area(height: list[int]) -> int:
    n_lines = len(height)

    if n_lines <= 1:
        return 0

    max_area = 0

    for first_line_idx in range(n_lines - 1):
        for second_line_idx in range(first_line_idx + 1, n_lines):
            area = calc_area(
                first_line_idx, height[first_line_idx], second_line_idx, height[second_line_idx])
            max_area = max(max_area, area)

    return max_area
