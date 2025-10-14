class Cat:
    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color

    def __str__(self):
        msg = "Cat [ name = {}, age = {}, color ={}]"
        return msg.format(self.name, self.age, self.color)

    def __getattr__(self, atr_name):
        return "No such attribute"

    def __getattribute__(self, atr_name):
        if atr_name == 'age' and object.__getattribute__(self, atr_name) < 0:
            return "I don't know my age"
        return object.__getattribute__(self, atr_name)
        # return self.__dict__[atr_name]


cat = Cat('Barsik', 3, 'black')
cat_2 = Cat('Barsik', -1, 'black')

print(cat.name)  # виведе Barsik
print(cat.age)
print(cat.__dict__)
print(cat.__dict__['age'])
print(cat_2.age)

#
# Звернення до поля, якого немає
print(cat.type)  # виведе  None
