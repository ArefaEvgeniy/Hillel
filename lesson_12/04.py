# class Dog(object):
# class Dog():
class Dog:
    def __init__(self, name, age, weight):
        self.name = name
        self._age = age
        self.__weight = weight

    def get_weight(self):
        print('Собака важить:', round(self.__weight, 2))

    def change_weight(self):
        self.__weight += 0.1


dog = Dog('Rem', 5, 5.6)
print(dog.name)
print(dog._age)
# print(dog.__weight)
print(dog._Dog__weight)
dog.get_weight()
dog.change_weight()
dog.change_weight()
dog.change_weight()
dog.change_weight()
dog.get_weight()
