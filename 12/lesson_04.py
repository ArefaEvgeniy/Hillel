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

    def distance_of_origin(self):
        return round((self.x ** 2 + self.y ** 2) ** 0.5, 2)


if __name__ == "__main__":
    point_1 = Point()
    point_2 = Point(2, 5)
    point_3 = Point(y=0, x=0)
    point_4 = Point(6)
    print(point_2.x)
    print(point_2.y)
    print(point_1)
    print(point_2)

    print(point_1 == point_2)
    print(point_1 == point_3)
    print(point_1 != point_2)
    print(point_1 != point_3)

    print('-' * 100)
    point_5 = point_2 + point_4
    print(point_5)

    print(point_5.distance_of_origin())
