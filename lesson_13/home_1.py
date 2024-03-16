# Для класу Circle, розглянутому на уроці, додати метод віднімання двох кіл.
# Віднімання радіусов зробити по модулю. Якщо два кола з однаковим значенням
# радіуса віднімаються, то результатом віднімання буде об'єкт классу Point.

# Circle(x=1, y=5, radius=1) - Circle(x=2, y=2, radius=3) = Circle(x=-1, y=3, radius=2)
# Circle(x=1, y=5, radius=3) - Circle(x=2, y=2, radius=3) = Point(x=-1, y=3)

import math
from task_01 import Point


class Circle(Point):
    radius = 0

    def __init__(self, radius, x=0, y=0):
        super().__init__(x, y)
        self.radius = radius

    def edge_distance_from_origin(self):
        return abs(self.distance_from_origin() - self.radius)

    def area(self):
        return math.pi * (self.radius ** 2)

    def circumference(self):
        return 2 * math.pi * self.radius

    def __eq__(self, other):
        return self.radius == other.radius

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        radius = self.radius + other.radius
        return Circle(radius, x, y)

    def __sub__(self, other):
        x = self.x - other.x
        y = self.y - other.y
        radius = abs(self.radius - other.radius)
        return Circle(radius, x, y) if radius else Point(x, y)

    def __str__(self):
        return super().__str__()[:-1] + f', radius={self.radius})'
