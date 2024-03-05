class Animal(object):

    def __init__(self, number_of_foot=4, viviparous=True, tail=True, name=None):
        self.number_of_foot = number_of_foot
        self.viviparous = viviparous
        self.tail = tail
        self.name = name

    def go(self):
        for item in range(1, self.number_of_foot + 1):
            print(f'Step on {item} foot', end='-')
        print()


class Dog(Animal):

    def say(self):
        print('Woof, woof!')


class Cat(Animal):

    def say(self):
        print('miay')


class Dolphin(Animal):

    def __init__(self, viviparous=True, tail=True, name=None, albin=False):
        super().__init__(0, viviparous, tail, name)
        self.albin = albin
        del self.number_of_foot

    def say(self):
        print('ultrasound')

    def go(self):
        print('swim')


class Monster(Dog, Dolphin):
    pass


a_1 = Monster()
a_1.go()
a_1.say()
