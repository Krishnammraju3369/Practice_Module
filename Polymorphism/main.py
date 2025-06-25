from abc import ABC, abstractmethod
import math


class Shape(ABC):

    @abstractmethod
    def area(self):
        pass


class Rectangle(Shape):

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius**2


shapes = [Rectangle(width=9, height=10), Circle(radius=4), Rectangle(width=8, height=14)]


for shape in shapes:
    print(f"The are area is: {shape.area()}")
