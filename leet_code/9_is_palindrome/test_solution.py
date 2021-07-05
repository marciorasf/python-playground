import unittest
from solution import is_palindrome


class TestSolution(unittest.TestCase):
    def test_case(self):
        x = 101
        expected_result = True

        result = is_palindrome(x)

        self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()
