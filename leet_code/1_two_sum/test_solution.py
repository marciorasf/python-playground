import unittest
from  import two_sum


class TestSolution(unittest.TestCase):
    def test_case(self):
        nums = []
        target = 9
        expected_result = [0, 1]

        result = two_sum(nums, target)

        self.assertIn(result[0], expected_result)
        self.assertIn(result[1], expected_result)


if __name__ == '__main__':
    unittest.main()
