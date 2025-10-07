class Auto(object):
    numbers = 0

    def __init__(self, model, color):
        self.model = model
        self.color = color
        self.increment_numbers()

    @classmethod
    def increment_numbers(cls):
        cls.numbers += 1


class Truck(Auto):
    numbers = 0

    def __init__(self, model, color, weight):
        super().__init__(model, color)
        self.weight = weight


auto_1 = Auto("BMW", "Red")
auto_2 = Auto("Audi", "Black")
print(auto_2.numbers)
auto_3 = Auto("Mercedes", "White")
print(Auto.numbers)  # 3
print(auto_2.numbers)

print("--- Truck ---")
truck_1 = Truck("Kamaz", "Blue", 10000)
truck_2 = Truck("ZIL", "Green", 8000)
truck_3 = Truck("MAZ", "Yellow", 12000)
truck_4 = Truck("Scania", "Black", 9000)
print(truck_1.numbers)  # 4
print(auto_2.numbers)
