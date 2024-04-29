class Animal(object):
    viviparous = True

    def __init__(self, number_of_foot=4, tail=True):
        self.number_of_foot = number_of_foot
        self.tail = tail

    def say(self):
        print('Nothing')

    def go(self):
        for item in range(1, self.number_of_foot + 1):
            print(f'Step on {item} foot', end='-')
        print()


class Cat(Animal):

    def __init__(self, number_of_foot=4, tail=True, name=None):
        super().__init__(number_of_foot, tail)
        self.name = name

    def say(self):
        print('Myai')


class Dog(Animal):

    def __init__(self, number_of_foot=4, tail=True, name=None):
        super().__init__(number_of_foot, tail)
        self.name = name

    def say(self):
        print('Woof, woof')


class Dolphin(Animal):

    def __init__(self, number_of_foot=0, tail=True, albino=True):
        super().__init__(number_of_foot, tail)
        self.albino = albino

    def say(self):
        print('ultrasound')

    def go(self):
        print('swim')


class Monster(Dog, Dolphin):
    pass


a_1 = Monster()
a_1.go()
a_1.say()
print(a_1.__dict__)
