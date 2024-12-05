class My_class:

    def __init__(self, a):
        self.a = a

    def general_method(self):
        return self.a

    @staticmethod
    def static_method(a, b, c):
        print("a:", a)
        print("b:", b)
        print("c:", c)
        return "Hello, world"


obj_1 = My_class(10)
print(obj_1.general_method())
print(obj_1.static_method(34, 2, 6))

print(My_class.static_method(0, 45, 33))
