class Animal(object):

    def __init__(self, name, number_of_foot=4, tail=True):
        self.name = name
        self.number_of_foot = number_of_foot
        self.tail = tail

    def go(self):
        for item in range(1, self.number_of_foot+1):
            print(f'Step on {item} foot.', end='')
        print()


class Dog(Animal):
    def say(self):
        print('Woof-Woof')


class Dolphin(Animal):
    def __init__(self, name=None, number_of_foot=0, tail=True, fin=True):
        super().__init__(name, number_of_foot, tail)
        self.fin = fin

    def say(self):
        print('ultrasound')

    def go(self):
        print('swim')


class Monster(Dog, Dolphin):
    ...


a = Monster()
print('name:', a.name)
print('number_of_foot:', a.number_of_foot)
print('tail:', a.tail)
print('fin:', a.fin)
a.say()
a.go()

