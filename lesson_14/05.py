class Auto:
    TOTAL_OBJECTS = 0

    def __init__(self, mark):
        self.mark = mark
        self.calc_objects()

    @classmethod
    def calc_objects(cls):
        cls.TOTAL_OBJECTS += 1


class Truck(Auto):
    TOTAL_OBJECTS = 0


a_1 = Auto('BMW-3')
a_2 = Auto('BMW-5')
a_3 = Auto('ZAZ')
print(Auto.TOTAL_OBJECTS)
print(a_2.TOTAL_OBJECTS)
print('-' * 50)

b_1 = Truck('Volvo-50')
b_2 = Truck('Volvo-505')
b_3 = Truck('Volvo-100')
b_4 = Truck('MAN')

print(Auto.TOTAL_OBJECTS)
print(Truck.TOTAL_OBJECTS)

Truck.calc_objects()
print(Truck.TOTAL_OBJECTS)
