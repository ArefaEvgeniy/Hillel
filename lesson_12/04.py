class Woman(object):
    def __init__(self, name, age, weight):
        self.name = name
        self._age = age
        self.__weight = weight

    def get_weight(self):
        return f'Weight is {self.__weight - 10}'


w_1 = Woman('Sussy', 26, 55)
print(w_1.name)
print(w_1._age)
print(w_1._Woman__weight)
print(w_1.get_weight())
