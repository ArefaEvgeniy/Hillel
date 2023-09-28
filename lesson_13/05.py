class Animal:
    def __init__(self, name, age, number_of_foot=4):
        self.name = name
        self.age = age
        self.number_of_foot = number_of_foot

    def say(self):
        print('Nothing')

    def go(self):
        for item in range(1, self.number_of_foot + 1):
            print(f'Step on {item} foot', end='-')
        print()


class Dog(Animal):
    def say(self, word='woof'):
        print(f'{word.title()}, {word}!')

    def play(self):
        print('Jump')


class Cat(Animal):
    def say(self, word='Myu'):
        print(f'{word}!')


class Dolphin(Animal):
    def __init__(self, name, age, fin=True):
        super().__init__(name, age, 0)
        self.fin = fin

    def say(self):
        print('Ultrasound')

    def go(self):
        print('Swim')

    def eat(self):
        print('Fish, fish, fish!')


class Monster(Dolphin, Dog):
    pass


s = Monster('Bob', 45)
s.eat()
s.play()
s.say()
