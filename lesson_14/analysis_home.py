# class MyTest:
#
#     def __init__(self, x):
#         self.x = x
#
#     def __add__(self, other):
#         return MyTest(self.x + other.x)
#
#     def __mul__(self, other):
#         return MyTest(self.x * other.x)
#
#     def __str__(self):
#         return str(self.x)
#
#
# num_1 = MyTest(2)
# num_2 = MyTest(3)
# num_3 = MyTest(4)
# print(num_1 + num_2)
# print(num_2 * num_3)
# print(num_1 + num_2 * num_3)
# # как сделать сразу три действия (метода) ?
# # "+", "*" и т.д. вызывают соответствующие методы.
# # почему в терминале можно, и как определить очерёдность вызова метода?




# ВОПРОС 2   _____________________________________________________________________________

class Point:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return f'({self.x}, {self.y})'


class Circle(Point):

    def __init__(self, radius, x=0, y=0):
        super().__init__(x, y)
        self.radius = radius

    def __str__(self):
        return super().__str__()[:-1] + f' ,{self.radius})'

    def __sub__(self, other):
        radius = abs(self.radius - other.radius)
        x = self.x - other.x
        y = self.y - other.y
        return Circle(x=x, y=y, radius=radius) if radius != 0 else Point(x, y)
# почему возращает (y, radius, x), а не как записано в методе (x, y, radius) ?
# если записать в методе (radius, x, y), то выводит опять не так (x, y, radius)


c_1 = Circle(40)
c_2 = Circle(30, 2, 3)
print("c_1: ", c_1)
print("c_2: ", c_2)
print("c_1 - c_2: ", c_1 - c_2)
