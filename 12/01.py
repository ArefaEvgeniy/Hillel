class Human(object):
    national_leng = {
        "uk": "Привіт",
        "en": "Hello",
        "ru": "Привет"
    }


class Woman(Human):

    def __init__(self, name, weight, age, national):
        self.name = name
        self._weight = weight
        self.__age = age
        self.national = national

    def get_age(self):
        return self.__age - 5

    def say_hi(self):
        print(f"{self.national_leng.get(self.national)}")


woman_1 = Woman('Susy', 56.45, 32, "en")
print(woman_1.name)
print(woman_1._weight)
print(woman_1._Woman__age)
print(woman_1.get_age())

woman_2 = Woman('Tetiana', 56.45, 24, "uk")

woman_1.say_hi()
woman_2.say_hi()
