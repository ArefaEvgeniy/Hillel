class MyIterator:
    def __init__(self, *args):
        self.items = args
        self.index = 0

    def __next__(self):
        if self.index < len(self.items):
            item = self.items[self.index]
            self.index += 1
            return item
        else:
            raise StopIteration


class Person:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age

    def __iter__(self):
        return MyIterator(self.name, self.surname, self.age)


people_1 = Person("Alice", "Smith", 30)

for item in people_1:
    print(item)
