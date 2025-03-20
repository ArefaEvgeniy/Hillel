class Person:

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    @property
    def fullname(self):
        return f"{self.name} {self.surname}"

    @fullname.setter
    def fullname(self, new_value):
        self.name, self.surname = new_value.split()


obj_1 = Person('Bob', 'White')
print(obj_1.name)
print(obj_1.surname)
print(obj_1.fullname)

print("=" * 100)
obj_1.name = 'Rick'
obj_1.surname = 'Black'
print(obj_1.name)
print(obj_1.surname)
print(obj_1.fullname)

print("=" * 100)
obj_1.fullname = 'Tom Crouse'
print(obj_1.name)
print(obj_1.surname)
print(obj_1.fullname)
