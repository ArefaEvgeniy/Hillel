class Car:
    wheels = 4  # атрибут класу

    def start_engine(self):
        return "Engine started!"


car_1 = Car()
car_1.make = 1990
car_1.model = "BMW-7"
car_2 = Car()
car_2.make = 2000
car_2.model = "Opel Omega"
car_3 = Car()
car_3.make = 2010
car_3.model = "BMW-5"
print(car_1.__dict__)
print(car_2.__dict__)
print(car_3.__dict__)

print(car_3.make)
print(car_3.model)

print('-' * 100)

print(car_1.make)
print(car_1.model)
