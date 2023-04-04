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

    @fullname.deleter
    def fullname(self):
        self.name, self.surname = None, None


pers_1 = Person('Mark', 'Frizen')

print(pers_1.name)
print(pers_1.surname)
print(pers_1.fullname)

print('-' * 50)
pers_1.name = 'Jack'
print(pers_1.name)
print(pers_1.surname)
print(pers_1.fullname)

print('-' * 50)
pers_1.fullname = 'Stive Jobs'
print(pers_1.name)
print(pers_1.surname)
print(pers_1.fullname)

print('-' * 50)
del pers_1.fullname
print(pers_1.name)
print(pers_1.surname)
# print(pers_1.fullname)
