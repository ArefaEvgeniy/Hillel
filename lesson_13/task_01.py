# Створіть точковий клас, який зберігає координати X і У,
# знає, як обчислити відстань від початку координат,
# може порівняти координати двох об'єктів
# і під час виклику через функцію print() повертає свої координати

import math


class Point(object):

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def distance_from_origin(self):
        return math.hypot(self.x, self.y)

    def __str__(self):
        return f'Point(x={self.x}, y={self.y})'

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Point(x, y)

    def __sub__(self, other):
        x = self.x - other.x
        y = self.y - other.y
        return Point(x, y)


if __name__ == '__main__':
    a = Point()
    b = Point(1, 3)
    c = Point(1, 3)

    print(b.distance_from_origin())
    print(a)
    print(b)

    print(a == b)
    print(b == c)

    d = b + c
    print(d)

    e = d - c
    print(e)
