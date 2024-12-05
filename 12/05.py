from task_04 import Point


class Circle(Point):

    def __init__(self, radius, x=0, y=0):
        super().__init__(x, y)
        self.radius = radius

    def __str__(self):
        answer = super().__str__()[7:]
        return f"Circle: radius={self.radius}, {answer}"


a_1 = Circle(3, 5)
print(a_1.radius)
print(a_1.x)
print(a_1.y)

print(a_1)

print(a_1.distance_of_origin())
