class Car:
    def __init__(self):
        self.__speed = 0  # Приватний атрибут

    def accelerate(self):
        self.__speed += 10

    def get_speed(self):
        return self.__speed


my_car = Car()
my_car.accelerate()
print(my_car.get_speed())  # Вивід: 10
# print(my_car.__speed)  # Помилка: 'Car' object has no attribute '__speed'
