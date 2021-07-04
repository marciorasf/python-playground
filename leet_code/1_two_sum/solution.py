from __future__ import annotations


def two_sum(nums: List[int], target: int) -> List[int]:
    passed_values = {}

    for index, value in enumerate(nums):
        value_needed_to_target = target - value

        complementary_index = passed_values.get(value_needed_to_target)

        if complementary_index != None:
            return [index, complementary_index]

        passed_values.update({value: index})
