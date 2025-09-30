# class Dog(object):
class Dog:
    legs = 4
    tail = 1
    ears = 2

    def say(self):
        print("Woof!")

    def go(self):
        for _ in range(self.legs):
            print("Step")


dog_1 = Dog()
dog_2 = Dog()

print(dog_1.legs)
dog_1.say()

a = "Hello"
print(a.lower())

dog_1.legs = 3
print('-' * 20)
dog_1.go()
print('-' * 20)
dog_2.go()

dog_1.name = "Bobik"
print(dog_1.name)

print('-' * 20)
print(dog_1.__dict__)
print(dog_2.__dict__)
Dog.legs = 5
print(dog_1.legs)
print(dog_2.legs)
