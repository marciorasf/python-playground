from abc import ABC, abstractmethod
import math


class Shape(ABC):
    @abstractmethod
    def area(self) -> float:
        pass


class Square(Shape):
    def __init__(self, side: float) -> None:
        self._side = side

    def area(self) -> float:
        return self._side**2


class Circle(Shape):
    def __init__(self, radius: float) -> None:
        self._radius = radius

    def area(self) -> float:
        return math.pi * (self._radius**2)


def calc_area(shapes: list[Shape]) -> float:
    total_area = 0

    for shape in shapes:
        total_area += shape.area()

    return total_area
