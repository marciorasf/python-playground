import unittest
from solution import max_area


class TestSolution(unittest.TestCase):
    def test_case_1(self):
        height = [1, 1]
        expected_result = 1

        result = max_area(height)

        self.assertEqual(result, expected_result)

    def test_case_2(self):
        height = [4, 3, 2, 1, 4]
        expected_result = 16

        result = max_area(height)

        self.assertEqual(result, expected_result)

    def test_case_3(self):
        height = [1, 2, 1]
        expected_result = 2

        result = max_area(height)

        self.assertEqual(result, expected_result)

    def test_case_4(self):
        height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
        expected_result = 49

        result = max_area(height)

        self.assertEqual(result, expected_result)

    def test_case_5(self):
        height = [1, 2, 4, 3]
        expected_result = 4

        result = max_area(height)

        self.assertEqual(result, expected_result)

    def test_case_6(self):
        height = [1, 3, 2, 5, 25, 24, 5]
        expected_result = 24

        result = max_area(height)

        self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()
