class Dog:
    number_of_foot = 4
    tail = True
    name = None

    def say(self):
        print('Woof, woof')

    def go(self):
        for item in range(1, self.number_of_foot + 1):
            print(f'Step on {item} foot', end='-')
        print()


dog_1 = Dog()
dog_2 = Dog()
dog_3 = Dog()

print(dog_1.number_of_foot)
dog_1.say()
dog_3.say()
dog_1.go()
dog_3.number_of_foot = 3
dog_3.go()
dog_3.name = 'Rem'
dog_3.age = 8

print('-' * 100)

print(dog_3.number_of_foot)
print(dog_3.name)
print(dog_3.age)
print(dog_2.number_of_foot)
print(dog_2.name)

print('-' * 100)
print(dog_1.number_of_foot)
print(dog_2.number_of_foot)
print(dog_3.number_of_foot)

print('-' * 100)
Dog.number_of_foot = 2
print(dog_1.number_of_foot)
print(dog_2.number_of_foot)
print(dog_3.number_of_foot)

print('-' * 100)
print(dog_1.__dict__)
print(dog_2.__dict__)
print(dog_3.__dict__)
