class MyClass_1:
    def __init__(self, arg_1, arg_2, arg_3=None, arg_4=0):
        self.arg_1 = arg_1
        self.arg_2 = arg_2
        self.arg_3 = arg_3
        self.arg_4 = arg_4


class MyClass_2(MyClass_1):
    def __init__(self, arg_1, arg_2, arg_5, arg_3=None, arg_4=0):
        super().__init__(arg_1, arg_2, arg_3, arg_4)
        self.arg_5 = arg_5


a_1 = MyClass_1(1, 2, 3, 4)
a_2 = MyClass_2(1, 2, 5, 3, 4)

print(a_1.__dict__)
print(a_2.__dict__)
