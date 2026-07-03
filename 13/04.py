class Dog(object):

    def __init__(self, name="", age=0, hands=4):
        self.name = name
        self.age = age
        self.hands = hands

    def go(self):
        print("Stepping forward")

    def say(self):
        print("Woof Woof")

    def bite(self):
        print("Biting")


dog_1 = Dog("Rex", 5)
dog_2 = Dog("Buddy", 3)
dog_3 = Dog("Max", 2, 3)
dog_4 = Dog()

for dog in [dog_1, dog_2, dog_3]:
    print(f"Name: {dog.name}, Age: {dog.age}")
    print("-" * 20)

dog_1.go()
