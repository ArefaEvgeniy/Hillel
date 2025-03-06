class Car(object):
    color = 'white'

    def __init__(self, name=None, year=None, color=None):
        self.name = name
        self.year = year
        self.color = color

    @staticmethod
    def start_engine(a, b):
        print(a + b)
        return "Engine started!"

    def get_data(self):
        return f"{self.name} - {self.year}"


car_1 = Car('Volvo', 2024, 'red')
print(car_1.start_engine(4, 56))
print(car_1.get_data())
print(Car.start_engine(0, 8))
