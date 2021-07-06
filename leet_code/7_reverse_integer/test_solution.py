import unittest
from solution import reverse_integer


class TestSolution(unittest.TestCase):
    def test_case_1(self):
        x = 123
        expected_result = 321

        result = reverse_integer(x)

        self.assertEqual(result, expected_result)

    def test_case_2(self):
        x = -123
        expected_result = -321

        result = reverse_integer(x)

        self.assertEqual(result, expected_result)

    def test_case_3(self):
        x = 2**31
        expected_result = 0

        result = reverse_integer(x)

        self.assertEqual(result, expected_result)

    def test_case_4(self):
        x = -2**31 - 1
        expected_result = 0

        result = reverse_integer(x)

        self.assertEqual(result, expected_result)

    def test_case_5(self):
        x = 1534236469
        expected_result = 0

        result = reverse_integer(x)

        self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()
