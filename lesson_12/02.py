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
dog_2 = Dog()
dog_3 = Dog()

print(f'Number of foot DOG1: {dog_1.number_of_foot}')
dog_1.say()
dog_2.number_of_foot = 3
dog_2.go()
dog_3.go()
print(f'Name of DOG1: {dog_1.name}')
dog_1.name = 'Rem'
print(f'Name of DOG1: {dog_1.name}')
dog_1.age = 5
print(f'age of DOG1: {dog_1.age}')
# print(f'age of DOG2: {dog_2.age}')
dog_1.name = 'Jhon'
print(f'Name of DOG1: {dog_1.name}')
