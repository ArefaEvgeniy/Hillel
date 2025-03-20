class Car:

    def __init__(self, color='black', model='BMW 5'):
        self.color = color
        self.model = model

    def __getattr__(self, atr_name):
        print(f'Attribute {atr_name} is absent')
        return None


car_2 = Car('white')
print(car_2.model)
print(car_2.year)
