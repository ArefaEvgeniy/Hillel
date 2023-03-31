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

    def circumference(self):
        return math.pi * self.radius

    def __eq__(self, other):
        return self.radius == other.radius

    def __ne__(self, other):
        return self.radius != other.radius

    def __str__(self):
        temp = super().__str__().split('Point')[-1]
        return f'Circle{temp[:-1]}, radius={self.radius})'

    def __add__(self, other):
        point = super().__add__(other)
        radius = self.radius + other.radius
        return Circle(radius, point.x, point.y)


c_1 = Circle(7, 1)
print(c_1)

c_2 = Circle(7, 5, 3)
print(c_2)

print(c_1 == c_2)
print(c_1 != c_2)

print(c_1 + c_2)
