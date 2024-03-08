class MyClass:
    attr = 111

    def first_method(self):
        print('This is general method', self.attr)

    @staticmethod
    def second_method(a, b):
        print('This is static method', a ** b)


a = MyClass()
a.first_method()
MyClass.second_method(2, 3)
a.second_method(2, 4)
