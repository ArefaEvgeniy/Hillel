from l04 import Point


class Circle(Point):

    def __init__(self, x=0, y=0, radius=1):
        super().__init__(x, y)
        self.radius = radius
        # print(super().__str__())
        # print(self.__str__())

    def __str__(self):
        return f"Circle({self.x}, {self.y}, r={self.radius})"

    def __eq__(self, other):
        return self.radius == other.radius


c_1 = Circle(11, 15, 5)
c_2 = Circle(0, 4, 5)
print(c_1)
print(c_1.distance_from_origin())
print(c_1 == c_2)
print(c_1 != c_2)
