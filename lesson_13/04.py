class Animal:

    def __init__(self, name, number_of_foots=4, tail=True):
        self.name = name
        self.number_of_foots = number_of_foots
        self.tail = tail

    def __str__(self):
        return "This is an Animal object"

    def say(self):
        print('Uhhhh')

    def go(self):
        for item in range(1, self.number_of_foots + 1):
            print(f'Step on {item} foot', end='-')
        print()

    def super_go(self):
        print('Super GO')
        self.go()


class Dog(Animal):

    def say(self):
        print('Woof, woof')

    def super_say(self):
        print("SUPER")
        super().say()


class Dolphin(Animal):

    def say(self):
        super().say()
        print('ultrasound')

    def go(self):
        print('swim')


class Cat(Animal):

    def say(self):
        print('Miay')

    def jump(self):
        print('jump')


class Monster(Cat, Dog):
    pass


a_1 = Animal(None, 3)
print(a_1)
a_1.super_go()

a_2 = Dog('Ram')
a_2.super_say()
a_2.go()

print('-' * 50)

a_3 = Monster('Bob')
a_3.jump()
a_3.say()
