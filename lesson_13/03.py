class Animal:
    def __init__(self, number_of_foot=4, tail=True, name=None):
        self.number_of_foot = number_of_foot
        self.tail = tail
        self.name = name

    def say(self):
        print('Nothing')

    def go(self):
        for item in range(1, self.number_of_foot + 1):
            print(f'Step om {item} foot', end='')
        print()


class Dog(Animal):

    def say(self):
        print('Woow, woow!')


class Dolphin(Animal):

    def __init__(self, tail=True, name=None, fin=True):
        super().__init__(number_of_foot=0, tail=tail, name=name)
        self.fin = fin

    def say(self):
        print('Ultrasound')

    def go(self):
        print('swim')


class Monster(Dog, Dolphin):
    pass


monster = Monster()
monster.go()
monster.say()
