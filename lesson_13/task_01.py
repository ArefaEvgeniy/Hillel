# Создать класс Point, который хранит координаты х и у,
# умеет вычислять расстояние от начала координат,
# может сравнивать координаты двух точек
# и при вызове через функцию принт возвращает свои координаты

import math


class Point(object):

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def distance_from_origin(self):
        return math.hypot(self.x, self.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __str__(self):
        return f'Point({self.x}, {self.y})'

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Point(x, y)


if __name__ == '__main__':
    a = Point()
    b = Point(1, 2)
    c = Point(0, 0)
    d = Point(3, 5)
    print(a == b)
    print(b)
    print(a)
    print(a == c)

    print(b + d)
    print(b)

    print('-' * 50)

    f = b + d
    print(f)
