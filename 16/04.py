class Truck:
    def __init__(self, make, model, year, capacity):
        self.make = make
        self.model = model
        self.year = year
        self.__capacity = capacity

    def __getattribute__(self, name):
        if name == "name":
            return None
        else:
            return object.__getattribute__(self, name)

    @property
    def capacity(self):
        return self.__capacity

    @capacity.setter
    def capacity(self, new_capacity):
        if isinstance(new_capacity, (int, float)) and (0 < new_capacity <= 20):
            self.__capacity = new_capacity
        else:
            raise ValueError("Capacity cannot be negative")

    def display_info(self):
        print(f"Truck Make: {self.make}")
        print(f"Truck Model: {self.model}")
        print(f"Truck Year: {self.year}")
        print(f"Truck Capacity: {self.capacity} tons")


truck1 = Truck("Ford", "F-150", 2020, 15)
truck1.display_info()

print("-" * 20)

truck1.capacity = 11
truck1.display_info()

print(truck1.name)
