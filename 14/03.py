class MyClass:

    def __init__(self, name: str, age: int, weight: float):
        self.name = name
        self.age = age
        self.__weight = weight

    def func(self, b):
        ...
        a = b * self.__weight
        return a

    def get_weight(self):
        return self.__weight


obj_1 = MyClass('Bob', 23, 76.56)
obj_2 = MyClass('Kate', 33, 66.00)

print(obj_1.get_weight())
print(obj_2.get_weight())
