class Car(object):
    weels = 4
    doors = 4
    seats = 5
    color = "white"
    mark = "BMW"

    def __init__(self, mark, color, doors=None, seats=None):
        self.mark = mark
        self.color = color
        self.doors = doors
        self.seats = seats

    def go(self):
        print("The car is moving")


car_1 = Car("Audi", "red")
car_2 = Car("Mercedes", "black")
car_3 = Car("Toyota", "blue", 2, 4)

print(car_1.mark)
print(car_3.mark)
print(Car.mark)

car_2.go()
print("-" * 20)
print(car_1.__dict__)
print("-" * 20)
print(car_2.__dict__)
print("-" * 20)
print(car_3.__dict__)
