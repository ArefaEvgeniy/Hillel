class Dog:

    def __init__(self, name, number_of_foots=4, tail=True):
        self.name = name
        self.number_of_foots = number_of_foots
        self.tail = tail

    def say(self):
        print('Woof, woof')

    def go(self):
        for item in range(1, self.number_of_foots + 1):
            print(f'Step on {item} foot', end='-')
        print()


dog_1 = Dog('Rem')
print(dog_1.name)
dog_1.go()

dog_2 = Dog('Lucky', 3)
dog_2.color = 'RED'
print(dog_2.name)

print(f'dog 1: {dog_1.__dict__}')
print(f'dog 2: {dog_2.__dict__}')

print(dog_2.color)


dog_2.go()
#
# dog_1.go()
