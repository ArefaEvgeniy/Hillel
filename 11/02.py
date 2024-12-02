class Car:
    color = "Black"
    _year = 2000
    __speed = "200 km/h"


my_car = Car()
print(my_car.color)
print(my_car._year)
print(my_car._Car__speed)
