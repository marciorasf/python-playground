from __future__ import annotations


def calc_area(x_0, y_0, x_1, y_1):
    return abs(x_1 - x_0) * min(y_0, y_1)


def max_area(height: list[int]) -> int:
    n_lines = len(height)

    if n_lines <= 1:
        return 0

    front = 0
    back = n_lines-1
    max_area = 0

    while front < back:
        area = calc_area(
            front, height[front], back, height[back])
        max_area = max(max_area, area)

        if height[front] < height[back]:
            front += 1
        else:
            back -= 1

    return max_area
