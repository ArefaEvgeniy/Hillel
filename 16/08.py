class Person:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age
        self.args = (name, surname, age)
        self.index = 0

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index < len(self.args):
            item = self.args[self.index]
            self.index += 1
            # if self.index >= 3:
            #     self.index = 0
            return item
        else:
            # self.index = 0
            raise StopIteration


people_1 = Person("Alice", "Smith", 30)

for item in people_1:
    print(item)

print("*" * 20)

for item in people_1:
    print(item)
