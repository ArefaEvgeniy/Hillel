class Human:

    def __init__(self, name, age, surname, gender):
        self.name = name
        self.__age = age
        self.surname = surname
        self.gender = gender

    @property
    def age(self):
        if self.gender == 'F':
            res = round(self.__age * 0.9)
        else:
            res = self.__age
        return res

    @age.setter
    def age(self, new_value):
        if not 0 <= new_value <= 100:
            new_value = 18
        self.__age = new_value


a_1 = Human('Bob', 34, 'Kalm', 'M')
a_2 = Human('Helene', 25, 'Kruz', 'F')

print(a_1.age)
print(a_2.age)

a_1.age = 45
print(a_1.age)

a_1.age = 145
print(a_1.age)
