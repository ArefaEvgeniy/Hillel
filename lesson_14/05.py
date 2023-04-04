class Car(object):
    LAST_MODEL = None
    TOTAL_CARS = 0

    def __init__(self, model):
        self.model = model
        Car.LAST_MODEL = model
        Car.TOTAL_CARS += 1

    @classmethod
    def total_objects(cls):
        print('Total cars:', cls.TOTAL_CARS)


car_1 = Car('BMW')
car_2 = Car('ZAZ')
car_3 = Car('VOLVO')

print('model:', car_1.model)
print('last_model:', car_1.LAST_MODEL)
Car.total_objects()
