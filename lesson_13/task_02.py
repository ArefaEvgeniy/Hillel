import math


class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def distance_from_origin(self):
        return math.hypot(self.x, self.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __ne__(self, other):
        return True

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Point(x, y)

    def __str__(self):
        return f'Point({self.x}, {self.y})'


if __name__ == '__main__':
    a = Point(1, 3)
    b = Point(2)
    print(f'a.x: {a.x}')
    print(f'a.y: {a.y}')
    print(f'b.x: {b.x}')
    print(f'b.y: {b.y}')
    print(a == b)
    print(a != b)
    print(f'a: {a}')
    print(f'b: {b}')
    c = a + b
    print(f'c: {c}')
    print(type(c))
    print(f'a: {a}')
