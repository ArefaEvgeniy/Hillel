class Dog:

    def __init__(self, number_of_foot=4, tail=True, name=None):
        self.number_of_foot = number_of_foot
        self.tail = tail
        self.name = name

    def say(self):
        print('Woow, woow!')

    def go(self):
        for item in range(1, self.number_of_foot + 1):
            print(f'Step om {item} foot', end='')
        print()


dog_1 = Dog()
print(dog_1)
dog_1.number_of_foot = 3
dog_1.color = 'Red'
dog_1.father = False
print(dog_1.number_of_foot)
dog_1.say()
dog_1.go()
print(dog_1.__dict__)
print(dog_1.color)
print(dog_1.father)

print('-' * 50)

dog_2 = Dog(name='Lucky')
dog_2.say()
dog_2.go()
print(dog_2.number_of_foot)
print(dog_2.__dict__)
