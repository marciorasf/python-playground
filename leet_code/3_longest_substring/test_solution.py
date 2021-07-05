import unittest
from solution import length_of_longest_substring


class TestSolution(unittest.TestCase):
    def test_case(self):
        s = "jxdlnaaij"
        expected_result = 6

        result = length_of_longest_substring(s)

        self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()
