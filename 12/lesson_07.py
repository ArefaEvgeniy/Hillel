from math import hypot


class Point(object):

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return f'Point(x={self.x}, y={self.y})'

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def distance_from_origin(self):
        return round(hypot(self.x, self.y), 2)


if __name__ == '__main__':
    point_1 = Point(3)
    point_2 = Point(2, 4)
    point_4 = Point(5, 4)

    print(point_1.distance_from_origin())
    print(point_2.distance_from_origin())

    print(point_1)
    print(point_2)

    point_3 = point_1 + point_2
    print(point_3)
    print(point_3.distance_from_origin())
    print(point_1)
    print(point_2)

    print(point_1 != point_3)
    print(point_4 != point_3)

    print(point_1 - point_4)
