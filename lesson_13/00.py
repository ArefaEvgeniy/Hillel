class Auto_value:

    def __init__(self, brand, age, color, mark, weight=2000):
        self.brand = brand
        self.age = age
        self.color = color
        self.mark = mark
        self.weight = weight

    def move(self):
        print("move")

    def stop(self):
        print("stop")

    def birthday(self):
        self.age += 1


auto_1 = Auto_value("VAZ", 1, "white", "2101", 980)
auto_2 = Auto_value("VAZ", 10, "white", "2101")
auto_3 = Auto_value("VAZ", 5, "red", "2105")

Auto_value.brand = 'DEOWE'
auto_2.brand = 'BMW'
print(auto_1.brand)
print(auto_2.brand)
print(auto_3.brand)

auto_1.move()
auto_1.stop()

auto_1.birthday()
