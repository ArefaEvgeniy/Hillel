class Car:
    number_of_objects = 0

    def __init__(self, color='White', model='BMW-7'):
        self.color = color
        self.model = model
        Car.number_of_objects += 1


numbers = 10
list_objects = []
for _ in range(numbers):
    list_objects.append(Car())

print(list_objects)
print(list_objects[-1].number_of_objects)
car_1 = Car('Black', 'Zaz')
print(list_objects[-1].number_of_objects)
print(car_1.number_of_objects)
