import unittest
from unittest.case import expectedFailure
from solution import three_sum


class TestSolution(unittest.TestCase):
    def test_case_1(self):
        nums = []
        expected_result = []

        result = three_sum(nums)

        self.assertEqual(result, expected_result)

    def test_case_2(self):
        nums = [-1, 0, 1, 2, -1, -4]
        expected_result = [[-1, -1, 2],  [-1, 0, 1]]

        result = three_sum(nums)

        self.assertEqual(result, expected_result)

    def test_case_3(self):
        nums = [0]
        expected_result = []

        result = three_sum(nums)

        self.assertEqual(result, expected_result)

    def test_case_4(self):
        nums = [1, 0, 0, 0, 1]
        expected_result = [0, 0, 0]

        result = three_sum(nums)

        self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()
