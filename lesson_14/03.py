class Person:

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    @property
    def fullname(self):
        return f'{self.name} {self.surname}'

    @fullname.setter
    def fullname(self, new):
        self.name, self.surname = new.split()

    @fullname.deleter
    def fullname(self):
        print('Attention! Name ane Surname were deleted')
        self.name, self.surname = '', ''


p_1 = Person('Bob', 'Red')
print(p_1.name)
print(p_1.surname)
print(p_1.fullname)

print('-' * 50)

p_1.surname = 'Smith'
print(p_1.name)
print(p_1.surname)
print(p_1.fullname)

print('-' * 50)
p_1.fullname = 'Adam Foks'
print(p_1.name)
print(p_1.surname)
print(p_1.fullname)

print('-' * 50)
del(p_1.fullname)
print(p_1.name)
print(p_1.surname)
print(p_1.fullname)
