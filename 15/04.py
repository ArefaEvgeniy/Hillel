class Human:

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    @property
    def fullname(self):
        return f'{self.name} {self.surname}'

    @fullname.setter
    def fullname(self, new_value: str):
        self.name, self.surname = new_value.split()

    @fullname.deleter
    def fullname(self):
        self.name, self.surname = None, None


a = Human('Bob', 'White')
print(a.name)
print(a.surname)
print(a.fullname)

print('-' * 100)
a.surname = 'Red'
print(a.name)
print(a.surname)
print(a.fullname)

a.fullname = 'Tom Hanks'

print('-' * 100)
print(a.name)
print(a.surname)
print(a.fullname)
print(a.__dict__)

del a.fullname
print(a.name)
print(a.surname)
print(a.fullname)
print(a.__dict__)
