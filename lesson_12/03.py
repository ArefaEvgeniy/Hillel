class Dog(object):

    def __init__(self, number_of_foot=4, viviparous=True, tail=True, name=None):
        self.number_of_foot = number_of_foot
        self.viviparous = viviparous
        self.tail = tail
        self.name = name

    def say(self):
        print('Woof, woof!')

    def go(self):
        for item in range(1, self.number_of_foot + 1):
            print(f'Step on {item} foot', end='-')
        print()


dog_1 = Dog(4, True, True, "Rem")
dog_2 = Dog(3, tail=False, name='Boby')

print(dog_1.__dict__)
print(dog_2.__dict__)

print(dog_1.name)
print(dog_2.name)
