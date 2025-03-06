# class Car(object):
class Car:
    wheels = 5  # атрибут класу

    def start_engine(self):
        return "Engine started!"


car_1 = Car()
print(car_1.start_engine())
print(car_1.wheels)
print(type(car_1))

car_2 = Car()
car_3 = Car()
# a = 'dfgfdg'
# print(type(a))
# str()
# list()
# a.strip()

car_1.name = 'Volvo'
car_1.is_truck = False
print(car_1.name)

print(car_1.__dict__)
print(car_2.__dict__)
print(car_1.wheels)
print(car_2.wheels)
print(car_3.wheels)

car_1.wheels = 4
print(car_1.__dict__)
print(car_1.wheels)
print(car_2.wheels)
print(car_3.wheels)

Car.wheels = 6
print(car_1.wheels)
print(car_2.wheels)
print(car_3.wheels)
