class Animal:
    foots = 4

    def go(self):
        print(f"step * {self.foots}")


class Dog(Animal):

    def say(self):
        print("Wof-wof")


class Cat(Animal):

    def say(self):
        print("Miay")


class Dolphin:
    fitt = True

    def go(self):
        print("swim")

    def say(self):
        print("Ultrasound")


class Monster(Dog, Dolphin):
    pass


a = Monster()
a.go()
a.say()
