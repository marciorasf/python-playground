import unittest
from solution import letter_combinations


class TestSolution(unittest.TestCase):
    def test_case_1(self):
        digits = ""
        expected_result = []

        result = letter_combinations(digits)

        self.assertEqual(result, expected_result)

    def test_case_2(self):
        digits = "2"
        expected_result = ["a", "b", "c"]

        result = letter_combinations(digits)

        self.assertEqual(result, expected_result)

    def test_case_3(self):
        digits = "23"
        expected_result = ["ad", "ae", "af",
                           "bd", "be", "bf", "cd", "ce", "cf"]

        result = letter_combinations(digits)

        self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()
