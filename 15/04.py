class Cat:
    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color

    def __str__(self):
        msg = "Cat [ name = {}, age = {}, color ={}]"
        return msg.format(self.name, self.age, self.color)

    def __getattr__(self, atr_name):
        self.__dict__[atr_name] = 'New'
        return self.__dict__[atr_name]


cat = Cat('Barsik', 3, 'black')
print(cat.name)  # виведе Barsik

# Звернення до поля, якого немає
print(cat.tetiana)  # виведе  None

print(cat.__dict__)

if hasattr(cat, "name"):
    print(cat.name)
