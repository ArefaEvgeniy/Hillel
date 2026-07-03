# class Dog(object):
class Dog:
    name = ""
    hands = 4
    age = 0

    def go(self):
        print("Stepping forward")

    def say(self):
        print("Woof Woof")

    def bite(self):
        print("Biting")


dog_1 = Dog()
dog_2 = Dog()
dog_3 = Dog()

dog_1.say()
print(dog_1.hands)
print(dog_2.hands)
print(dog_3.hands)
print("-" * 20)

dog_2.hands = 3
print(dog_1.hands)
print(dog_2.hands)
print(dog_3.hands)
print("-" * 20)
Dog.hands = 5
print(dog_1.hands)
print(dog_2.hands)
print(dog_3.hands)
print("-" * 20)
print(dog_1.__dict__)
print(dog_2.__dict__)
print(dog_3.__dict__)
