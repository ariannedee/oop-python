import abc  # Abstract Base Class
from math import pi


class Shape(abc.ABC):
    @abc.abstractmethod
    def area(self):
        pass

    @abc.abstractmethod
    def circumference(self):
        pass

    def __str__(self):
        return type(self).__name__


class Circle(Shape):
    def __init__(self, r):
        self.r = r

    def area(self):
        return pi * self.r ** 2

    def circumference(self):
        return 2 * pi * self.r


class Rectangle(Shape):
    def __init__(self, length, width):
        self.l = length
        self.w = width

    def area(self):
        return self.l * self.w

    def circumference(self):
        return 2 * self.l + 2 * self.w


class Square(Rectangle):
    def __init__(self, length):
        super().__init__(length, length)


if __name__ == '__main__':
    shapes = [Square(10), Circle(20), Rectangle(3.4, 1.5)]

    for shape in shapes:
        print(f'{shape} area is {shape.area()}')
