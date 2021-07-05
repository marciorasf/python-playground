import unittest
from solution import longest_palindrome


class TestSolution(unittest.TestCase):
    def test_case(self):
        s = "ababac"
        expected_result = "ababa"

        result = longest_palindrome(s)

        self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()
