class Car:
    weels = 4
    motor = "Gas"

    def go(self):
        print("go")


car_1 = Car()
car_2 = Car()
car_3 = Car()

print(car_1.weels)
car_2.color = "Black"
print(car_2.color)

print(car_1.weels)
print(car_2.weels)
print(car_3.weels)

car_1.weels = 3
print('-' * 100)
print(car_1.weels)
print(car_2.weels)
print(car_3.weels)

Car.weels = 5
print('-' * 100)
print(car_1.weels)
print(car_2.weels)
print(car_3.weels)

print('-' * 100)
print(car_1.__dict__)
print(car_2.__dict__)
print(car_3.__dict__)
