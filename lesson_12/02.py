class Dog:
    def __init__(self, name='Bob', age=2, weight=7.6):
        self.name = name
        self._age = age
        self.__weight = weight

    def prints(self):
        print('name:', self.name)
        print('_age:', self._age)
        print('__weight:', self.__weight)


dog_1 = Dog()
# dog_1.prints()
print('name:', dog_1.name)
print('_age:', dog_1._age)
print('__weight:', dog_1._Dog__weight)
