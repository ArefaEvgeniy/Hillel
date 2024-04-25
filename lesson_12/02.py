class Dog(object):
    viviparous = True

    def __init__(self, number_of_foot=4, tail=True, name=None):
        self.number_of_foot = number_of_foot
        self.tail = tail
        self.name = name

    def say(self):
        print('Woof, woof')

    def go(self):
        for item in range(1, self.number_of_foot + 1):
            print(f'Step on {item} foot', end='-')
        print()


dog_1 = Dog(name='Ram')
dog_2 = Dog(name='Sussy')
dog_3 = Dog(3)

print(dog_1.__dict__)
print(dog_2.__dict__)
print(dog_3.__dict__)
