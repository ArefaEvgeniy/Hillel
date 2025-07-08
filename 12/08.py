class Car(object):
    number = 0

    def __init__(self, model, year):
        self.model = model
        self.year = year
        self.increment_number()

    @classmethod
    def increment_number(cls):
        cls.number += 1


class Truck(Car):
    number = 0


print(Car.number)

car1 = Car("Mersedes", 2001)
car2 = Car("ZAZ", 1995)
print(Car.number)
car3 = Car("Vovo", 2020)
print(Car.number)
print(car2.number)

truck1 = Truck("MAN", 2011)
truck2 = Truck("Vovo", 2021)
print(Car.number)
print(Truck.number)
