class Point(object):

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def distance_from_origin(self):
        return (self.x**2 + self.y**2)**0.5

    def __str__(self):
        return f"Point({self.x}, {self.y})"

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Point(x, y)


if __name__ == "__main__":
    p_1 = Point(3, 4)
    p_2 = Point()
    p_3 = Point(6, 8)
    p_4 = Point(0, 0)

    print(p_1.distance_from_origin())
    print(p_1)
    print(p_2)
    print(p_3)
    print(p_4)

    print(p_2 == p_4)
    print(p_2 == p_3)

    p_5 = p_1 + p_3
    print(p_5)
