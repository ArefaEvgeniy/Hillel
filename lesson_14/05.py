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
        pass


a = Person('Bob', 'Red')
print(a.name)
print(a.surname)
print(a.fullname)

print('-' * 50)
a.name = 'Nick'
print(a.name)
print(a.surname)
print(a.fullname)

print('-' * 50)
a.fullname = 'Tom Kruz'
print(a.name)
print(a.surname)
print(a.fullname)
