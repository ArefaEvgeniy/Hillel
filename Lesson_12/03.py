class Woman:

    def __init__(self, name, age, weight):
        self.name = name
        self._age = age
        self.__weight = weight

    def get_weight(self):
        if self.__weight < 40:
            return self.__weight * 1.1
        elif 40 <= self.__weight <= 60:
            return self.__weight
        else:
            return self.__weight / 1.2


w_1 = Woman("Anna", 25, 35)
w_2 = Woman("Elena", 30, 55)
w_3 = Woman("Elena", 55, 85)

print(w_1.get_weight())
print(w_2.get_weight())
print(w_3.get_weight())
