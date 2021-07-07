import unittest
from solution import roman_to_integer


class TestSolution(unittest.TestCase):
    def test_case_1(self):
        s = "III"
        expected_result = 3

        result = roman_to_integer(s)

        self.assertEqual(result, expected_result)

    def test_case_2(self):
        s = "IV"
        expected_result = 4

        result = roman_to_integer(s)

        self.assertEqual(result, expected_result)

    def test_case_3(self):
        s = "IX"
        expected_result = 9

        result = roman_to_integer(s)

        self.assertEqual(result, expected_result)

    def test_case_4(self):
        s = "LVIII"
        expected_result = 58

        result = roman_to_integer(s)

        self.assertEqual(result, expected_result)

    def test_case_5(self):
        s = "MCMXCIV"
        expected_result = 1994

        result = roman_to_integer(s)

        self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()
