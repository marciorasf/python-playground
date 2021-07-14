import unittest
from solution import moves_to_make_zigzag


class TestSolution(unittest.TestCase):
    def test_case_1(self):
        nums = [1, 2, 3]
        expected_result = 2

        result = moves_to_make_zigzag(nums)

        self.assertEqual(result, expected_result)

    def test_case_2(self):
        nums = [9, 6, 1, 6, 2]
        expected_result = 4

        result = moves_to_make_zigzag(nums)

        self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()
