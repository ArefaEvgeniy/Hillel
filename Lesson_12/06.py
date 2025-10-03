class Animal:

    def go(self):
        return "running"


class Dog(Animal):

    def say(self):
        return "Woof!"


class Cat(Animal):

    def say(self):
        return "Meow!"


class Dolphin(Animal):

    def say(self):
        return "Click-click"

    def go(self):
        return "swimming"


class Monster(Dog, Dolphin):

    ...


dog = Dog()
print(dog.say())
print(dog.go())

print("-" * 20)
cat = Cat()
print(cat.say())
print(cat.go())

print("-" * 20)
monster = Monster()
print(monster.say())
print(monster.go())
print(Monster.__mro__)
