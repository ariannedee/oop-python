from math import pi


class Shape(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def area(self):
        raise NotImplemented

    def circumference(self):
        raise NotImplemented

    def __str__(self):
        return f'{type(self).__name__} at ({self.x}, {self.y})'


class Circle(Shape):
    def __init__(self, r, *args, **kwargs):
        self.r = r
        super().__init__(*args, **kwargs)

    def area(self):
        return pi * self.r ** 2

    def circumference(self):
        return 2 * pi * self.r


class Rectangle(Shape):
    def __init__(self, length, width, *args, **kwargs):
        self.l = length
        self.w = width
        super().__init__(*args, **kwargs)

    def area(self):
        return self.l * self.w

    def circumference(self):
        return 2 * self.l + 2 * self.w


class Square(Rectangle):
    def __init__(self, length, *args, **kwargs):
        super().__init__(length, length, *args, **kwargs)


if __name__ == '__main__':
    shapes = [Square(10, x=0, y=0), Circle(20, -1, 1), Rectangle(3.4, 1.5, 20, y=5)]

    for shape in shapes:
        print(f'{shape} area is {shape.area()}')
