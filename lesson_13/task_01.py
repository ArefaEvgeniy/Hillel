# Создать класс Point, который хранит координаты х и у,
# умеет вычислять расстояние от начала координат,
# может сравнивать координаты двух точек
# и при вызове через функцию принт возвращает свои координаты

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
        return self.x != other.x or self.y != other.y

    def __str__(self):
        return f'Point({self.x}, {self.y})'

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Point(x, y)


if __name__ == '__main__':
    a = Point()
    print(a)
    print(a.distance_from_origin())

    b = Point(3, 4)
    print(b)
    print(b.distance_from_origin())

    print(a == b)
    print(a != b)

    c = Point(1, 2)
    print(c == a)

    print('-' * 30)
    d = b + c
    print(d)
    print(type(d))
    print(b)
    print(type(b))
    print(c)
    print(type(c))

    print(c.x)
    print(c.y)
