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


dog_1 = Dog(4, True, True, "Rem")
cat_1 = Cat(3, tail=False, name='Boby')
dolphin_1 = Dolphin(albin=True)

dog_1.go()
cat_1.go()
dolphin_1.go()

dog_1.say()
cat_1.say()
dolphin_1.say()

print(dolphin_1.albin)
print(dolphin_1.__dict__)
