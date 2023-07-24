class Animal(object):

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


class Dog(Animal):
    ...


class Cat(Animal):

    def say(self):
        print('Miay')


class Dolphin(Animal):

    def __init__(self, name=None, tail=True, albino=False):
        super().__init__(name, 0, tail)
        del self.number_of_foots
        self.albino = albino

    def say(self):
        print('ultrasound')

    def go(self):
        print('swim')

    def not_breath(self):
        print('Around 2 hours')


dog_1 = Dog('Rem')
cat_1 = Cat('Tom')
dol_1 = Dolphin(tail=False)

dog_1.go()
cat_1.go()
dol_1.go()
print(dol_1.name)
# print(dol_1.number_of_foots)
print(dol_1.tail)
