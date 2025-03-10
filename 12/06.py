class Person:

    def __init__(self, name, age, weight):
        self.name = name
        self._age = age
        self.__weight = weight

    def get_weight(self):
        return round(self.__weight * 0.9, 2)


obj_1 = Person('Sysi', 23, 48.32)
print(obj_1.__dict__)
print(obj_1.name)
print(obj_1._age)
# print(obj_1.__weight)
print(obj_1.get_weight())
print(obj_1._Person__weight)
