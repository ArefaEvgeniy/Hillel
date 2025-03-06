class Car(object):
    color = 'white'

    def __init__(self, name=None, year=None, color=None):
        self.name = name
        self.year = year
        self.color = color

    def start_engine(self):
        return "Engine started!"


def honk(self: Car):
    self.year += 1
    print(self.start_engine())
    return "Honk, honk!"


car_1 = Car('Volvo', 2024, 'red')
# car_1.name = 'Volvo'
# car_1.year = 2024
# car_1.color = 'red'

car_2 = Car('BMW')
# car_2.name = 'BMW'
# car_2.year = 2013

car_3 = Car(color='pink')
# car_3.name = 'Zaz'
# car_3.year = 1990
# car_3.color = 'pink'

print(car_1.__dict__)
print(car_2.__dict__)
print(car_3.__dict__)

Car.new_func = honk

print(car_1.new_func())
print(car_1.__dict__)
