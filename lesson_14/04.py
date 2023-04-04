class Car:
    last_model = None

    def __init__(self, model):
        self.model = model
        Car.last_model = model


print('last_model:', Car.last_model)
car_1 = Car('BMW')
print('last_model:', Car.last_model)
print('last_model:', car_1.last_model)

car_2 = Car('ZAZ')
car_3 = Car('VOLVO')

print('model:', car_2.model)
print('last_model:', car_2.last_model)
