class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    @property
    def fullname(self):
        return self.name + ' ' + self.surname

    @fullname.setter
    def fullname(self, new):
        self.name, self.surname = new.split(' ')


a_1 = Person('Bob', 'Red')
print(a_1.name)
print(a_1.surname)
print(a_1.fullname)

print('-' * 50)
a_1.name = 'Brad'
print(a_1.name)
print(a_1.surname)
print(a_1.fullname)

print('-' * 50)
a_1.fullname = 'Nick White'
print(a_1.name)
print(a_1.surname)
print(a_1.fullname)
