class MyClass:
    attr_1 = 'XX'
    attr_2 = 0

    def __init__(self, attr_3, attr_4, attr_5=None):
        self.attr_3 = attr_3
        self.attr_4 = attr_4
        self.attr_5 = attr_5

    def func(self):
        MyClass.attr_1 = self.attr_3


object_1 = MyClass(1, 2)
print(object_1.attr_1)
print(object_1.attr_2)
print(object_1.attr_3)
print(object_1.attr_4)
print(object_1.attr_5)
print(object_1.__dict__)

MyClass.attr_1 = 'RRR'
print('-' * 50)
object_2 = MyClass(3, 3)
print(object_2.attr_1)
print(object_2.attr_2)
print(object_2.attr_3)
print(object_2.attr_4)
print(object_2.attr_5)

print('-' * 50)
print(object_1.attr_1)

print('-' * 50)
object_1.func()
print(object_1.attr_1)
print(object_2.attr_1)

