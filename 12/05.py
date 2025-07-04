from lesson_04 import Point


class Circle(Point):

    def __init__(self, x=0, y=0, radius=0):
        super().__init__(x, y)
        self.radius = radius

    def __str__(self):
        return f'Circle(x={self.x}, y={self.y}, radius={self.radius})'


circle = Circle(4, 9, 6)
print(circle)
print(circle.distance_of_origin())
