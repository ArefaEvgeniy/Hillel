class Dog(object):

    def __init__(self, name, age, weight):
        self._name = name
        self.age = age
        self.__weight = weight

    def fix(self):
        self.__weight += 0.1

    def print_weight(self):
        print(f'Weight of dog a: {self.__weight}')
        self.fix()


dog_1 = Dog('Lucky', 7, 4.5)
print(dog_1.age)
print(dog_1._name)
print(dog_1._Dog__weight)
print(dog_1.__dict__)
dog_1.fix()
dog_1.fix()
dog_1.fix()
dog_1.print_weight()
print(dog_1._Dog__weight)
