class Person:

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    @property
    def fullname(self):
        return f"{self.name} {self.surname}"

    @fullname.setter
    def fullname(self, evgen: str):
        self.name, self.surname = evgen.split()

    @fullname.deleter
    def fullname(self):
        print('Delete!')


people = Person("Bob", "Red")
print(people.name)
print(people.surname)
print(people.fullname)

print("-" * 50)
people.surname = "White"
print(people.name)
print(people.surname)
print(people.fullname)

print("-" * 50)
people.fullname = "Tetiana Black"
print(people.name)
print(people.surname)
print(people.fullname)
