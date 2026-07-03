class Animal:
    name = ""
    hands = 4
    age = 0

    def go(self):
        print("Stepping forward")


class Dog(Animal):

    def say(self):
        print("Woof Woof")

    def bite(self):
        print("Biting")


class Cat(Animal):

    def say(self):
        print("Meow Meow")

    def claim(self):
        print("Claiming territory")


dog_1 = Dog()
cat_1 = Cat()
cat_2 = Cat()
print(cat_1.hands)
cat_1.say()
dog_1.say()

dog_1.name = "Rex"
dog_1.age = 5
cat_1.name = "Mittens"
cat_1.age = 3
cat_2.name = "Whiskers"
cat_2.age = 2
