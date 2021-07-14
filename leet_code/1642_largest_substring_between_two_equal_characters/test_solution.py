import unittest
from solution import max_length_between_equal_characters


class TestSolution(unittest.TestCase):
    def test_case_1(self):
        s = "aa"
        expected_result = 0

        result = max_length_between_equal_characters(s)

        self.assertEqual(expected_result, result)

    def test_case_2(self):
        s = "abca"
        expected_result = 2

        result = max_length_between_equal_characters(s)

        self.assertEqual(expected_result, result)

    def test_case_3(self):
        s = "cbzxy"
        expected_result = -1

        result = max_length_between_equal_characters(s)

        self.assertEqual(expected_result, result)

    def test_case_2(self):
        s = "cabbac"
        expected_result = 4

        result = max_length_between_equal_characters(s)

        self.assertEqual(expected_result, result)


if __name__ == '__main__':
    unittest.main()
