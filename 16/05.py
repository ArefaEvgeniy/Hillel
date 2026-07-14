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
        if attr_name == "type":
            attr_value = attr_value if attr_value in ["Home Cat", "Devil"] else False
            self.__dict__[attr_name] = attr_value
        else:
            self.__dict__[attr_name] = attr_value


cat = Cat('Barsik', 3, 'black')

cat.type = "Devils"
print(cat.type)
print(cat.__dict__)
