from __future__ import annotations


def three_sum(nums: list[int]) -> list[list[int]]:
    if len(nums) < 3:
        return []

    sorted_nums = nums.sort()
    num_set = set(sorted_nums)

    cur_num = None
    for first_num_idx, first_num in enumerate(sorted_nums):
        if first_num == cur_num:
            continue

        cur_num = first_num
        num_set.discard(cur_num)

        for sec_num_idx, sec_num in sorted_nums[first_num_idx+1:]:
            pass

    triplets = []
    return triplets
