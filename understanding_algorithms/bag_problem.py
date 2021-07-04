from typing import TypedDict


class Item(TypedDict):
    price: float
    weight: int


Items = dict[str, Item]


def bag_problem_solver(items: Items, capacity: int):
    def calc_value_by_items(chosen_items: list[str]):
        sum = 0

        for item in chosen_items:
            sum += items[item]["price"]

        return sum

    matrix = [[None]*capacity for item in items]

    for row_idx, current_item in enumerate(items):
        for col_idx in range(capacity):
            current_capacity = col_idx + 1
            current_item_props = items[current_item]

            old_best_choice = matrix[row_idx-1][col_idx] or []

            current_attempt = []
            if current_item_props["weight"] <= current_capacity:
                left_space = current_capacity - current_item_props["weight"]
                items_for_left_space = matrix[row_idx -
                                              1][left_space-1] if left_space > 0 else []
                current_attempt = [current_item] + (items_for_left_space or [])

            price_for_old_best_choice = calc_value_by_items(old_best_choice)
            price_for_current_attempt = calc_value_by_items(current_attempt)

            if price_for_current_attempt > price_for_old_best_choice:
                matrix[row_idx][col_idx] = current_attempt
            else:
                matrix[row_idx][col_idx] = old_best_choice

    return set(matrix[-1][-1])
