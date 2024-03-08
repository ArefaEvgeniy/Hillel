class Person:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value.isalpha():
            self.__name = value
        else:
            self.__name = None


person_1 = Person('Bob')
print(person_1.name)

person_2 = Person('Bob2')
print(person_2.name)

person_1.name = '34457'
print(person_1.name)
