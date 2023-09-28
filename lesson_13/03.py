import math
from task_02 import Point


class Circle(Point):
    def __init__(self, radius, x=0, y=0):
        super().__init__(x, y)
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

    def __eq__(self, other):
        return self.radius == other.radius

    def __str__(self):
        return 'Circle' + super().__str__()[5:-1] + f', radius={self.radius})'

    def __add__(self, other):
        new = super().__add__(other)
        return Circle(self.radius + other.radius, new.x, new.y)


a = Circle(5, 4, 7)
b = Circle(6, 1)
print(f'a.radius: {a.radius}')
print(f'a.x: {a.x}')
print(f'a.y: {a.y}')
print(a.area())
print(a == b)
print(a)
c = a + b
print(c)
