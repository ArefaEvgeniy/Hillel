class Cat(object):
    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color

    def __str__(self):
        msg = "Cat [ name = {}, age = {}, color ={}]"
        return msg.format(self.name, self.age, self.color)

    # def __getattr__(self, atr_name):
    #     return None  # pass


cat = Cat('Barsik', 3, 'black')
print(getattr(cat, "name"))  # виведе Barsik
print(getattr(cat, "age"))  # виведе 3
print(getattr(cat, "color", None))  # виведе black
print(getattr(cat, "type", None))  # виведе black
