import unittest
from solution import integer_to_roman


class TestSolution(unittest.TestCase):
    def test_case_1(self):
        num = 3
        expected_result = "III"

        result = integer_to_roman(num)

        self.assertEqual(result, expected_result)

    def test_case_2(self):
        num = 4
        expected_result = "IV"

        result = integer_to_roman(num)

        self.assertEqual(result, expected_result)

    def test_case_3(self):
        num = 9
        expectedResult = "IX"

        result = integer_to_roman(num)

        self.assertEqual(result, expectedResult)

    def test_case_4(self):
        num = 58
        expectedResult = "LVIII"

        result = integer_to_roman(num)

        self.assertEqual(result, expectedResult)

    def test_case_5(self):
        num = 1994
        expectedResult = "MCMXCIV"

        result = integer_to_roman(num)

        self.assertEqual(result, expectedResult)

    def test_case_6(self):
        num = 10
        expectedResult = "X"

        result = integer_to_roman(num)

        self.assertEqual(result, expectedResult)



if __name__ == '__main__':
    unittest.main()
