import unittest
from unittest.case import expectedFailure
from solution import longest_common_prefix


class TestSolution(unittest.TestCase):
    def test_case_1(self):
        strs = ["flower", "flow", "flight"]
        expected_result = "fl"

        result = longest_common_prefix(strs)

        self.assertEqual(result, expected_result)

    def test_case_2(self):
        strs = ["dog", "racecar", "car"]
        expected_result = ""

        result = longest_common_prefix(strs)

        self.assertEqual(result, expected_result)

    def test_case_3(self):
        strs = [""]
        expected_result = ""

        result = longest_common_prefix(strs)

        self.assertEqual(result, expected_result)

    def test_case_4(self):
        strs = ["dog"]
        expected_result = "dog"

        result = longest_common_prefix(strs)

        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()
