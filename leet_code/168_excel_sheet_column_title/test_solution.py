import unittest
from solution import convert_to_title


class TestSolution(unittest.TestCase):
    def test_case_1(self):
        column_number = 1
        expected_result = "A"

        result = convert_to_title(column_number)

        self.assertEqual(result, expected_result)

    def test_case_2(self):
        column_number = 28
        expected_result = "AB"

        result = convert_to_title(column_number)

        self.assertEqual(result, expected_result)

    def test_case_3(self):
        column_number = 701
        expected_result = "ZY"

        result = convert_to_title(column_number)

        self.assertEqual(result, expected_result)

    def test_case_4(self):
        column_number = 2147483647
        expected_result = "FXSHRXW"

        result = convert_to_title(column_number)

        self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()
