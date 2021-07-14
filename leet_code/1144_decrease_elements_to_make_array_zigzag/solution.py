from __future__ import annotations

MAX = 1000


def moves_to_make_zigzag(nums: list[int]) -> int:
    decreasing = [0]*2

    for idx, num in enumerate(nums):
        left = nums[idx - 1] if idx > 0 else MAX + 1
        right = nums[idx + 1] if idx + 1 < len(nums) else MAX + 1
        decreasing[idx % 2] += max(0, num - min(left, right) + 1)

    return min(decreasing)
