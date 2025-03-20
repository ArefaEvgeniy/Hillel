class Car:

    def __init__(self, color='black', model='BMW 5'):
        self.color = color
        self.model = model


car_2 = Car('white')
print(getattr(car_2, "model", "none"))
print(getattr(car_2, "year", "none"))
print(car_2.__dict__)
