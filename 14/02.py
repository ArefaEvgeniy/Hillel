from f01 import Point


class Circle(Point):
    def __init__(self, x=0, y=0, radius=1):
        super().__init__(x, y)
        self.radius = radius

    def __str__(self):
        return f"Circle({self.x}, {self.y}, radius={self.radius})"

    def __add__(self, other):
        res = super().__add__(other)
        return Circle(res.x, res.y, self.radius + other.radius)


circle_1 = Circle(3, 4)
circle_2 = Circle(4, 0, 5)

print(circle_1)
print(circle_2)
print(circle_1.distance_from_origin())
print(circle_1 == circle_2)
print(circle_1 + circle_2)
