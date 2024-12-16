class Cat(object):
    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color

    def __str__(self):
        msg = "Cat [ name = {}, age = {}, color ={}]"
        return msg.format(self.name, self.age, self.color)

    def __getattr__(self, atr_name):
        return None  # pass


cat = Cat('Barsik', 3, 'black')
print(cat.name)  # Barsik
print(cat.type)  # AttributeError Звернення до поля, якого немає
print(cat.__dict__)
