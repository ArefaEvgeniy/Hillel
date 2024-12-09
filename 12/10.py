class Car:
    number_of_objects = 0

    def __init__(self, color='White', model='BMW-7'):
        self.color = color
        self.model = model
        self.add_car()

    @classmethod
    def add_car(cls):
        cls.number_of_objects += 1


class Track(Car):
    number_of_objects = 0

    def __init__(self, color='Black', model='MAN', weight=20000):
        super().__init__(color, model)
        self.weight = weight


car_1 = Car('Black', 'Zaz')
car_2 = Car()
car_3 = Car('Red')

print('number_of_objects for Car:', car_1.number_of_objects)

truck_1 = Track()
truck_2 = Track(weight=30000)
print('number_of_objects for Track:', truck_2.number_of_objects)
print('number_of_objects for Car:', car_1.number_of_objects)
