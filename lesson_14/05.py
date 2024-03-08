class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    @property
    def fullname(self):
        return self.name + ' ' + self.surname

    @fullname.setter
    def fullname(self, new):
        self.name, self.surname = new.split()

    @fullname.deleter
    def fullname(self):
        self.name = None
        self.surname = None


person_1 = Person('Bob', 'Kruz')
print(person_1.name)
print(person_1.surname)
print(person_1.fullname)

print('-' * 50)
person_1.surname = 'Red'
print(person_1.name)
print(person_1.surname)
print(person_1.fullname)

print('-' * 50)
person_1.fullname = 'Tom Lucky'
print(person_1.name)
print(person_1.surname)
print(person_1.fullname)

print('-' * 50)
del person_1.fullname
print(person_1.name)
print(person_1.surname)
