class Person:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_value):
        res = ''
        for item in new_value:
            if item.isalpha():
                res += item
        self.__name = res


a_1 = Person('Bob')
a_2 = Person('Jack.3')
a_3 = Person('Bob Nick')

print(a_1.name)
print(a_2.name)
print(a_3.name)

a_1.name = 'Jack.3'
print(a_1.name)
