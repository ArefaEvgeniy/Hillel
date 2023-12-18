class Animal:
    def __init__(self, number_of_foot=4, tail=True, name=None):
        self.number_of_foot = number_of_foot
        self.tail = tail
        self.name = name

    def go(self):
        for item in range(1, self.number_of_foot + 1):
            print(f'Step om {item} foot', end='')
        print()


class Dog(Animal):

    def say(self):
        print('Woow, woow!')


class Cat(Animal):

    def say(self):
        print('Myau!')


cat_1 = Cat(name='Kati')
print(cat_1.__dict__)
cat_1.go()
cat_1.say()

dog_1 = Dog(name='Rem')
dog_1.say()
