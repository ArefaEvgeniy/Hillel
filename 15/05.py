class Human:

    def __init__(self, name, age, surname, gender):
        self.name = name
        self.age = age
        self.surname = surname
        self.gender = gender

    def __setattr__(self, attr_name, attr_value):
        if attr_name == 'age' and not 0 <= attr_value <= 100:
            attr_value = 18
        self.__dict__[attr_name] = attr_value

    def __getattribute__(self, atr_name):
        if atr_name == 'age' and self.gender == 'F':
            res = round(object.__getattribute__(self, atr_name) * 0.9)
        else:
            res = object.__getattribute__(self, atr_name)
        return res


a_1 = Human('Bob', 34, 'Kalm', 'M')
a_2 = Human('Helene', 25, 'Kruz', 'F')

print(a_1.age)
print(a_2.age)

a_1.age = 45
print(a_1.age)

a_1.age = 145
print(a_1.age)
