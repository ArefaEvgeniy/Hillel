class Pets:
    legs = 4

    def go(self):
        print('step-step')


class Dog(Pets):
    swim = True

    def say(self):
        print('Woof-Woof')


class Cat(Pets):
    swim = False

    def say(self):
        print('Miay')


class Dolphin(Pets):
    swim = True

    def say(self):
        print('ultrasound')

    def go(self):
        print('swim')

    def hunter(self):
        print('fish')


class Monster(Cat, Dolphin):
    ...

# class Cat:
#     legs = 4
#     swim = False
#
#     def go(self):
#         print('step-step')
#
#     def say(self):
#         print('Miay')


obj_1 = Dog()
print(obj_1.legs)
obj_1.say()
obj_1.go()

print('-' * 50)

obj_2 = Cat()
print(obj_2.legs)
obj_2.say()
obj_2.go()

print('-' * 50)

obj_3 = Monster()
obj_3.say()
obj_3.hunter()
