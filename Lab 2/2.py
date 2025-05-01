from abc import ABC, abstractmethod
from math import pi

class Color:
    def __init__(self, name="Black"):
        self._name = name

    def get_color(self):
        return self._name

    def set_color(self, name):
        self._name = name


class Shape(ABC):
    def __init__(self, color: Color):
        self._color = color

    def get_color(self):
        return self._color.get_color()

    @abstractmethod
    def calculate_area(self):
        pass


class Circle(Shape):
    def __init__(self, radius, color: Color):
        super().__init__(color)
        self._radius = radius

    def calculate_area(self):
        return pi * self._radius ** 2

class Rectangle(Shape):
    def __init__(self, width, height, color: Color):
        super().__init__(color)
        self._width = width
        self._height = height

    def calculate_area(self):
        return self._width * self._height

class Triangle(Shape):
    def __init__(self, base, height, color: Color):
        super().__init__(color)
        self._base = base
        self._height = height

    def calculate_area(self):
        return 0.5 * self._base * self._height


shapes = [
    Circle(5, Color("Red")),
    Rectangle(4, 6, Color("Blue")),
    Triangle(3, 7, Color("Green"))
]

for shape in shapes:
    print(f"{shape.__class__.__name__} (колір: {shape.get_color()}) має площу {shape.calculate_area():.2f}")
