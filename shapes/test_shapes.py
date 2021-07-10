import unittest
from shapes import Square, Circle, calc_area
import math


class TestShapes(unittest.TestCase):
    def test_square_area(self):
        square = Square(2)
        expected_area = 4

        area = square.area()

        self.assertEqual(area, expected_area)

    def test_circle_area(self):
        circle = Circle(2)
        expected_area = math.pi * (2**2)

        area = circle.area()

        self.assertEqual(area, expected_area)

    def test_calc_area(self):
        square = Square(2)
        circle = Circle(2)
        expected_area = (2**2) + (math.pi * (2**2))

        area = calc_area([square, circle])

        self.assertEqual(area, expected_area)


if __name__ == '__main__':
    unittest.main()
