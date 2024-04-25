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

    def double_say(self):
        self.say()
        super().say()
        self.say()
        print(self.name)


dog_1 = Dog(name='Ram')
cat_1 = Cat(name='Sussy')


dog_1.go()
dog_1.say()
cat_1.go()
cat_1.say()

print('-' * 50)
dog_1.double_say()
