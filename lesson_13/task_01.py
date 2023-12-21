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

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    # def __ne__(self, other):
    #     return self.x != other.x or self.y != other.y

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Point(x, y)

    def __str__(self):
        return f'Point({self.x}, {self.y})'


if __name__ == '__main__':
    a = Point(1, 5)
    print(a.distance_from_origin())
    b = Point(2, 4)

    print(a)
    print(b)

    print(a == b)
    print(a != b)

    c = a + b
    print(c)
    print(c.x)
    print(c.y)

    print(a.x)
    print(a.y)
