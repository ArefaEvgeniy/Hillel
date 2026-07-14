class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.age = 33
        # self.full_name = f"{self.name} {self.surname}"

    @property
    def full_name(self):
        return f"{self.name} {self.surname}"

    @full_name.setter
    def full_name(self, value):
        self.name, self.surname = value.split(" ")

    @full_name.deleter
    def full_name(self):
        self.name = None
        self.surname = None


a_1 = Person("Alice", "Smith")
print(a_1.name)
print(a_1.surname)
print(a_1.full_name)
print("-" * 20)

a_1.surname = "Johnson"
print(a_1.name)
print(a_1.surname)
print(a_1.full_name)
print("-" * 20)

a_1.full_name = "Irina Petrova"
print(a_1.name)
print(a_1.surname)
print(a_1.full_name)
print("-" * 20)

del a_1.full_name
print(a_1.name)
print(a_1.surname)

print(a_1.age)
print(a_1.__dict__)
del a_1.age
print(a_1.__dict__)
