import unittest
from solution import string_to_integer


class TestSolution(unittest.TestCase):
    def test_case_1(self):
        s = "042"
        expected_result = 42

        result = string_to_integer(s)

        self.assertEqual(result, expected_result)

    def test_case_2(self):
        s = "       -42"
        expected_result = -42

        result = string_to_integer(s)

        self.assertEqual(result, expected_result)

    def test_case_3(self):
        s = "4193 with words"
        expected_result = 4193

        result = string_to_integer(s)

        self.assertEqual(result, expected_result)

    def test_case_4(self):
        s = "words and 987"
        expected_result = 0

        result = string_to_integer(s)

        self.assertEqual(result, expected_result)

    def test_case_5(self):
        s = "-91283472332"
        expected_result = -2147483648

        result = string_to_integer(s)

        self.assertEqual(result, expected_result)

    def test_case_6(self):
        s = "+-12"
        expected_result = 0

        result = string_to_integer(s)

        self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()
