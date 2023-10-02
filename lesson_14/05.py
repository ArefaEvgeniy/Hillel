class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    @property
    def full_name(self):
        return self.name + ' ' + self.surname

    @full_name.setter
    def full_name(self, new):
        self.name, self.surname = new.split(' ')

    @full_name.deleter
    def full_name(self):
        print('Name and surname deleted')
        self.name, self.surname = None, None


person = Person('Don', 'Joe')
print(person.name)
print(person.surname)
print(person.full_name)

print('-' * 50)

person.name = 'Jack'
print(person.name)
print(person.surname)
print(person.full_name)

print('-' * 50)

person.full_name = 'Bob White'
print(person.name)
print(person.surname)
print(person.full_name)

print(person)
