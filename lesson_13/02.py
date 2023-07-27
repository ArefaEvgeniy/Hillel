# Класс должен поддерживать все методы родительского класса, а так же:
# минимальное расстояние от окружности до центра координат;
# площадь окружности и длину окружности.


import math
from task_01 import Point


class Circle(Point):

    def __init__(self, radius, x=0, y=0):
        super().__init__(x, y)
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

    def circle_dline(self):
        return 2 * math.pi * self.radius

    def __eq__(self, other):
        return self.radius == other.radius

    def __str__(self):
        return f'Circle({self.x}, {self.y}, radius={self.radius})'

    def __add__(self, other):
        new = super().__add__(other)
        radius = self.radius + other.radius
        return Circle(radius, new.x, new.y)


a = Circle(5, x=7, y=3)
print(a)
print(a.area())
print(a.radius)
print(a.distance_from_origin())

b = Circle(2)

c = a + b
print(c)
