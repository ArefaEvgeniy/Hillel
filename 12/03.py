class Car(object):

    def __init__(self, weels, color, year, name):
        self.weels = weels
        self.color = color
        self.year = year
        self.name = name

    def go(self):
        print(f"go '{self.name}'")


car_1 = Car(4, "White", 2015, "BMW X5")
car_2 = Car(4, "Red", 2025, "ВАЗ-2101")

# car_1 = Car()
# car_1.weels = 4
# car_1.color = "White"
# car_1.year = 2015
# car_2 = Car()
# car_2.weels = 4
# car_2.color = "Red"
# car_2.year = 2025
# car_3 = Car()
# car_3.weels = 5
# car_3.color = "White"
# car_3.year = 2020
car_1.go()
car_2.go()
