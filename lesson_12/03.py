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


class Dog(Animal):
    ...


class Cat(Animal):
    def say(self):
        print('Maya')


dog_1 = Dog('Rem')
dog_1.go()
dog_1.say()
print('-' * 30)

cat_1 = Cat('Sussy', tail=False)
cat_1.go()
cat_1.say()
print('tail:', cat_1.tail)
