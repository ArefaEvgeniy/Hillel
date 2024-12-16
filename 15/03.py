class Cat:
    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color

    def __str__(self):
        msg = "Cat [ name = {}, age = {}, color ={}]"
        return msg.format(self.name, self.age, self.color)

    def __getattr__(self, atr_name):
        if atr_name == "type":
                return "Home Cat"
        print(atr_name)
        return "11"

    def __getattribute__(self, atr_name):
        return object.__getattribute__(self, atr_name)

    def __setattr__(self, attr_name, attr_value):
        if attr_name == "age":
            if not 0 <= attr_value <= 15:
                attr_value = 0
        self.__dict__[attr_name] = attr_value

    def __delattr__(self, attr_name):
        if attr_name != "home":
            del self.__dict__[attr_name]


cat = Cat('Barsik', 3, 'black')

cat.type = "Devil"
print(cat.type)   # виведе Devil
cat.age = -34
print(cat.__dict__)


dct = {"gender": "M", "home": True}
# cat.'gender' = dct['gender']

for key, val in dct.items():
    setattr(cat, key, val)
print(cat.__dict__)
print(cat.gender)
print(cat.home)
del cat.home
del cat.gender
print(cat.__dict__)
