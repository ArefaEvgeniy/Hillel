class Dog:
    def __init__(self, name, age, number_of_foot=4):
        self.name = name
        self.age = age
        self.number_of_foot = number_of_foot

    def say(self, word='woof'):
        print(f'{word.title()}, {word}!')

    def go(self):
        for item in range(1, self.number_of_foot + 1):
            print(f'Step on {item} foot', end='-')
        print()


dog_1 = Dog('Rem', 3)
dog_2 = Dog('John', 1)
dog_3 = Dog(age=2, number_of_foot=5, name='Jerry')
print(f'Name of DOG1: {dog_1.name}')
print(f'Name of DOG2: {dog_2.name}')
print(f'Name of DOG3: {dog_3.name}')
print(f'Age of DOG1: {dog_1.age}')
print(f'Age of DOG2: {dog_2.age}')
print(f'Age of DOG3: {dog_3.age}')
print(f'Number of foot DOG1: {dog_1.number_of_foot}')
print(f'Number of foot DOG2: {dog_2.number_of_foot}')
print(f'Number of foot DOG3: {dog_3.number_of_foot}')

dog_2.say()
dog_2.say('hello')
