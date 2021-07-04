import unittest
from bag_problem import bag_problem_solver, Items


class TestSolution(unittest.TestCase):
    def test_case_1(self):
        items: Items = {
            "guitar": {
                "price": 1000,
                "weight": 1
            },
            "radio": {
                "price": 3000,
                "weight": 4
            },
            "laptop": {
                "price": 2500,
                "weight": 3
            },
        }
        capacity = 4
        expected_result = {"laptop", "guitar"}

        result = bag_problem_solver(items, capacity)

        self.assertSetEqual(result, expected_result)

    def test_case_2(self):
        items: Items = {
            "guitar": {
                "price": 1000,
                "weight": 1
            },
            "radio": {
                "price": 3000,
                "weight": 4
            },
            "laptop": {
                "price": 2500,
                "weight": 3
            },
            "iphone": {
                "price": 2000,
                "weight": 1
            },
        }
        capacity = 4
        expected_result = {"laptop", "iphone"}

        result = bag_problem_solver(items, capacity)

        self.assertSetEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()
