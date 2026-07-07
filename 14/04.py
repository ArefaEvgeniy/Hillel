class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say(self):
        return f"{self.name} says Woof!"

    def go(self):
        return f"{self.name} is running!"

    def bite(self):
        return f"{self.name} is biting!"


class Dolphin:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say(self):
        return f"{self.name} says Click!"

    def go(self):
        return f"{self.name} is swimming!"

    def swim(self):
        return f"{self.name} is swimming fast!"


class Monster(Dog, Dolphin):
    pass


m_1 = Monster("Monster", 5)
print(m_1.say())
print(m_1.go())
print(m_1.bite())
print(m_1.swim())
