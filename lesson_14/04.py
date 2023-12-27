class Car:
    TOTAL_OBJECTS = 0

    def __init__(self):
        Car.TOTAL_OBJECTS += 1

    @classmethod
    def total_objects(cls):
        print(f'Total objects: {cls.TOTAL_OBJECTS}')


class Truc(Car):
    TOTAL_OBJECTS = 0

    def __init__(self):
        Truc.TOTAL_OBJECTS += 1


a_1 = Car()
a_2 = Car()
a_3 = Car()
a_4 = Car()

a_1.total_objects()

b_1 = Truc()
b_2 = Truc()
b_2.total_objects()

