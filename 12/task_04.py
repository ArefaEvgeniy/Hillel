import math


class Point(object):

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Point: x={self.x}, y={self.y}"

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Point(x, y)

    def distance_of_origin(self):
        return round(math.hypot(self.x, self.y), 2)


class Square:

    def __init__(self, *args):
        self.figures = []
        if args:
            for item in args:
                self.figures.append(item)

    def add_objects(self, obj: Point):
        self.figures.append(obj)

    def number_of_figures(self):
        return len(self.figures)


if __name__ == '__main__':

    obj_1 = Point()
    obj_2 = Point(5)
    obj_3 = Point(3, 6)
    obj_4 = Point(0, 0)

    print(obj_1)
    print(obj_2)
    print(obj_3)

    print(obj_3.distance_of_origin())
    print(obj_2.distance_of_origin())

    a = Square()
    a.add_objects(obj_1)
    a.add_objects(obj_2)

    print(a.figures)
    print(a.number_of_figures())

    b = Square(obj_3, obj_2, obj_1)
    print(b.figures)
    print(b.number_of_figures())

    print('-' * 100)

    print(obj_1 == obj_4)
    print(obj_1 == obj_2)
    print(obj_1 != obj_4)

    c = obj_2 + obj_3
    print(c)
    print(c.x)
    print(c.y)
