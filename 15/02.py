class Car:
    number = 0

    def __init__(self, make, model):
        self.make = make
        self.model = model
        self.encriment_number()

    @classmethod
    def encriment_number(cls):
        cls.number += 1


class Truck(Car):
    number = 0

    def __init__(self, make, model, capacity):
        super().__init__(make, model)
        self.capacity = capacity


car_1 = Car("Toyota", "Camry")
car_2 = Car("Honda", "Civic")
car_3 = Car("Ford", "Mustang")

print(f"Total number of cars: {Car.number}")

truck_1 = Truck("Ford", "F-150", 1000)
truck_2 = Truck("Chevrolet", "Silverado", 1500)
print(f"Total number of trucks: {Truck.number}")
print(f"Total number of cars: {Car.number}")
