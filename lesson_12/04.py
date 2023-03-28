class Animal(object):

    def __init__(self, name, number_of_foot=4, tail=True):
        self.name = name
        self.number_of_foot = number_of_foot
        self.tail = tail

    def say(self):
        print('Woof-Woof')

    def go(self):
        for item in range(1, self.number_of_foot+1):
            print(f'Step on {item} foot.', end='')
        print()


class Dolphin(Animal):
    def __init__(self, name=None, number_of_foot=0, tail=True, fin=True):
        super().__init__(name, number_of_foot, tail)
        self.fin = fin

    def say(self):
        print('ultrasound')
        super().go()

    def go(self):
        print('swim')


dolphin_1 = Dolphin(tail=False)
dolphin_1.go()
dolphin_1.say()
print('name:', dolphin_1.name)
print('number_of_foot:', dolphin_1.number_of_foot)
print('tail:', dolphin_1.tail)
print('fin:', dolphin_1.fin)

