class Dog(object):

    def __init__(self, name, number_of_foot=4, tail=True):
        self.name = name
        self.number_of_foot = number_of_foot
        self.tail = tail

    def say(self, enemy):
        print('Woof-Woof', enemy)
        print(f'I have {self.helth} helth')

    def go(self):
        for item in range(1, self.number_of_foot+1):
            print(f'Step on {item} foot.', end='')
        print()
        self.new_attr = 'Yes'


dog_1 = Dog('Rem')
print('foots:', dog_1.number_of_foot)
print('Name:', dog_1.name)

dog_1.go()
print('new_attr:', dog_1.new_attr)
dog_1.helth = 100
print('helth:', dog_1.helth)
dog_1.say('Tom')

dog_2 = Dog(None, 3, False)
print('name:', dog_2.name)
print('foots:', dog_2.number_of_foot)
print('tail:', dog_2.tail)
dog_2.go()
