import math


class Point(object):
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return f'Point(x={self.x}, y={self.y})'

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Point(x, y)

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    def distance_from_origin(self):
        return math.hypot(self.x, self.y)


if __name__ == '__main__':
    a_1 = Point()
    a_2 = Point(4, 5)
    a_3 = Point(4, 5)

    print(a_2.distance_from_origin())
    print(a_1)
    print(a_2)

    print(a_1 == a_2)
    print(a_2 == a_3)

    a_4 = a_2 + a_3
    print(a_4)

    a_5 = a_2 - a_3
    print(a_5)
