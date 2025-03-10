from lesson_07 import Point
# import lesson_07


class Circle(Point):
# class Circle(lesson_07.Point):

    def __init__(self, radius, x=0, y=0):
        super().__init__(x, y)
        self.radius = radius

    def __str__(self):
        return f'Circle(radius={self.radius}, x={self.x}, y={self.y})'


circle_1 = Circle(1, x=0, y=10)
print(type(circle_1))
print(circle_1)
print(circle_1.distance_from_origin())
