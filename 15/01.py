class Car:
    number_of_cars = 0
    info = ''

    def __init__(self, color='black', model='BMW 5'):
        self.color = color
        self.model = model
        self.add_car()

    @classmethod
    def add_car(cls):
        cls.number_of_cars += 1

    @classmethod
    def get_info(cls):
        return cls.info

    @classmethod
    def set_info(cls, info):
        cls.info = info


class Truck(Car):
    number_of_cars = 0

    def __init__(self, color='white', model='MAN', weight=20000):
        super().__init__(color, model)
        self.weight = weight


car_1 = Car()
car_2 = Car('white')
car_3 = Car('red', 'opel')
print(Car.number_of_cars)
print(car_1.number_of_cars)
car_4 = Car()
print(car_1.number_of_cars)

print('=' * 50)
car_5 = Truck()
car_6 = Truck(weight=30000)
print(Car.number_of_cars)
print(Truck.number_of_cars)

print(car_3.get_info())
car_1.set_info(f"I'am a first object. I have {car_1.color} color")
print(car_3.get_info())
