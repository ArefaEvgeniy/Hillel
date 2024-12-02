class Animal:
    def speak(self):
        return "Nothing"


class Dog(Animal):
    def speak(self):
        return "Woof!"

    def go(self):
        return "run"


class Cat(Animal):
    ...


a_1 = Animal()
print(a_1.speak())

a_2 = Dog()
print(a_2.speak())

a_3 = Cat()
print(a_3.speak())
