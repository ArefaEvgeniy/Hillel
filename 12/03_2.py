class Car(object):
    wheels = 4  # атрибут класу

    def __init__(self, make, model="Zaz"):    # (self=car_1, make=1990, model="BMW-7")
        # атрибути екземпляра
        self.make = make                # car_1.make = make
        self.model = model

    def start_engine(self):
        return f"Engine started! {self.model}"


car_1 = Car(1990, "BMW-7")
car_2 = Car(2000, "Opel Omega")
car_3 = Car(model="BMW-5", make=2010)
car_4 = Car(1985)
print(car_1.__dict__)
print(car_2.__dict__)
print(car_3.__dict__)
print(car_4.__dict__)

print(car_3.make)
print(car_3.model)

print('-' * 100)

print(car_1.make)
print(car_1.model)

print(car_1.start_engine())
print(car_4.start_engine())
