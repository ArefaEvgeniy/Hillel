class Car:
    last_model = None

    def __init__(self, model):
        self.model = model
        Car.last_model = model


print(Car.last_model)

a = Car('BMW')
print(Car.last_model)

b = Car('ZAZ')
print(Car.last_model)

c = Car('Mersedes')
print(Car.last_model)
print('-' * 50)
print(a.last_model)
print(a.model)
print(b.last_model)
print(b.model)
print(c.last_model)
print(c.model)
