class Animal:

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


dog_1 = Dog('Rem')
cat_1 = Cat('Tom')

dog_1.say()
cat_1.say()
