class Woman:
    def __init__(self, name, age, weight):
        self.name = name
        self._age = age
        self.__weight = weight

    def get_weight(self):
        if self.__weight < 50:
            result = self.__weight + 5
        elif self.__weight > 80:
            result = self.__weight - 10
        else:
            result = self.__weight
        return result

    def _set_data(self, age, weight):
        self._age = age
        self.__weight = weight


woman = Woman("Alice", 30, 60)
print(woman.name)
print(woman._age)
# print(woman.__weight)
# print(woman._Woman__weight)
print(woman.get_weight())
