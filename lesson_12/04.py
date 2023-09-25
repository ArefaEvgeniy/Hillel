class Dog(object):
    def __init__(self, name, age, weight):
        self.name = name
        self._age = age
        self.__weight = weight

    def get_age(self):
        return self._age

    def get_weight(self):
        return self.__weight

    def lanch(self):
        self.__weight += 0.1


dog = Dog('Bob', 4, 7.8)
print(dog.name)
print(dog._age)
print(dog.get_weight())
print(dog._Dog__weight)
dog.lanch()
dog.lanch()
dog.lanch()
print(dog.get_weight())
