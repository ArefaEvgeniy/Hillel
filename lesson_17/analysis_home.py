class Car:
    FUEL_TYPES = ['бензин', 'дизель', 'електрика', 'гібрид']
    COLORS = []
    NUMBER_OF_CARS = 0

    def __init__(self, model, year, fuel_type, color_car):
        self.color = color_car
        self.model = model
        Car.NUMBER_OF_CARS += 1
        # Car.COLORS = Car.COLORS + [self.color] if Car.COLORS.count(self.color) == 0 else Car.COLORS
        Car.COLORS.append(self.color) if self.color not in Car.COLORS else ...
        self.year = year
        self.fuel_type = self.isvalid_fuel_type(fuel_type, Car.FUEL_TYPES)
        self.number = Car.NUMBER_OF_CARS

    @staticmethod
    def isvalid_fuel_type(fuel_type, types):
        if fuel_type not in types:
            fuel_type = types[0]
        else:
            fuel_type = fuel_type
        return fuel_type

    @classmethod
    def get_used_colors(cls):
        return len(cls.COLORS)

    @classmethod
    def get_number_of_cars(cls):
        return cls.NUMBER_OF_CARS

    @property
    def numbers(self):
        return f'{self.number} з {Car.NUMBER_OF_CARS}'

    def __str__(self):
        return f'{self.model} – {self.year} – {self.fuel_type} - {self.color} .'


car_1 = Car('Zaz', 1979, 'дизель', 'black')
car_2 = Car('BMW', 2000, 'бензин', 'red')
car_3 = Car('VOLVO', 2012, 'газ', 'white')
car_4 = Car('Mersedes', 2012, 'гібрид', 'red')
print('COLORS:', Car.get_used_colors(Car))
print('NUMBER_OF_CARS:', Car.get_number_of_cars(Car))
for item in (car_1, car_2, car_3, car_4):
    print('item:', item)
    print('numbers:', item.numbers)
