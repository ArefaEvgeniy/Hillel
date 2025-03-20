class MyClass:

    def __init__(self, param_1=1, param_2=50, param_3=100, acces=False):
        self.param_1 = param_1
        self.param_2 = param_2
        self.param_3 = param_3
        self.acces = acces

    def __getattr__(self, atr_name):
        return 0

    def __getattribute__(self, atr_name):
        if atr_name == 'param_3' and self.acces is False:
            return None
        return object.__getattribute__(self, atr_name)

    def __setattr__(self, attr_name, attr_value):
        # self.acces = True
        if attr_name == 'param_1':
            attr_value = abs(attr_value)
        self.__dict__[attr_name] = attr_value


obj_1 = MyClass()
obj_2 = MyClass(acces=True)

print(obj_1.param_1)
print(obj_2.param_1)
print(obj_1.param_3)
print(obj_2.param_3)
print(obj_1.param_4)
print(obj_2.param_4)

obj_1.param_1 = -3
obj_1.param_2 = -5
print(obj_1.__dict__)
