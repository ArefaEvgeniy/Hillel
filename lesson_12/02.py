class Dog:
    number_of_foot = 4
    viviparous = True
    tail = True
    name = None

    def say(self):
        print('Woof, woof!')

    def go(self):
        for item in range(1, self.number_of_foot + 1):
            print(f'Step on {item} foot', end='-')
        print()


dog_1 = Dog()
print(dog_1.number_of_foot)
dog_1.say()
dog_1.go()
print(type(dog_1))

print('Dog 2')
dog_2 = Dog()
dog_2.number_of_foot = 3
dog_2.name = 'Boby'
dog_2.color = 'red'
print(dog_2.number_of_foot)
dog_2.go()
dog_1.go()
print(dog_1.name)
print(dog_2.name)
print(dog_2.color)

print(dog_1.__dict__)
print(dog_2.__dict__)
print(dog_2.tail)

Dog.name = 'NoName'
print(dog_1.name)
print(dog_2.name)
