class MyClass:

    @staticmethod
    def func_1(a, b):
        print(a + b)

    @staticmethod
    def func_2(a, b):
        print(a - b)


obj_1 = MyClass()
obj_1.func_2(45, 8)
MyClass.func_1(45, 8)
obj_1.func_1(45, 8)
MyClass.func_2(45, 8)
