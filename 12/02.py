class Car:
    wheels = 4  # атрибут класу

    def start_engine(self):
        return "Engine started!"


car_1 = Car()
car_2 = Car()
car_3 = Car()
print(car_1.wheels)
print(car_2.wheels)
print(car_3.wheels)

print('-' * 100)

print(car_1.wheels)
Car.wheels = 7
print(car_1.wheels)
print(car_2.wheels)
print(car_3.wheels)

print('-' * 100)
car_1.year = 2000
print(car_1.wheels)
print(car_1.year)
print(car_1.__dict__)
print(car_2.__dict__)
car_2.wheels = 3

print('-' * 100)
print(car_1.wheels)
print(car_2.wheels)
print(car_3.wheels)
print(car_1.__dict__)
print(car_2.__dict__)
print(car_3.__dict__)
