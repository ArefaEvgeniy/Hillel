class Car:
    wheels = 5  # атрибут класу
    name = None

    def start_engine(self):
        return "Engine started!"

    def get_name(self, age):
        return f"{self.name} - {age}"


car_1 = Car()
car_1.name = 'Volvo'
car_2 = Car()
car_2.name = 'BMW'
car_3 = Car()

print(car_1.get_name(45))
print(car_2.get_name(22))
print(car_3.get_name(1))
