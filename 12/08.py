class Animal:
    def breath(self):
        return 'breath'


class Dog(Animal):
    def say(self):
        return 'Woof, woof'

    def go(self):
        return 'run'


class Dolphin(Animal):
    def say(self):
        return 'ultrasound'

    def go(self):
        return 'swim'


class Monster(Dog, Dolphin):
    pass


a = Monster()
print(a.breath())
print(a.say())
print(a.go())
