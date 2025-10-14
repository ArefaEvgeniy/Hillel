class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    @full_name.setter
    def full_name(self, new_full_name):
        if len(new_full_name.split(" ")) == 2:
            self.first_name, self.last_name = new_full_name.split(" ")

    @full_name.deleter
    def full_name(self):
        print("Deleting full_name...")
        self.first_name = ""
        self.last_name = ""


person = Person("John", "Doe")
print(person.first_name)
print(person.last_name)
print(person.full_name)

print("-" * 20)
person.last_name = "Smith"
print(person.first_name)
print(person.last_name)
print(person.full_name)

print("-" * 20)
person.full_name = "Jane Austen"
print(person.first_name)
print(person.last_name)
print(person.full_name)

print("-" * 20)
person.full_name = "Peter"
print(person.first_name)
print(person.last_name)
print(person.full_name)

del person.full_name
print(person.__dict__)
