class MyClass:

    def __init__(self):
        self.c = 0

    def first_method(self, a, b):
        print('This is general method')
        return a * b + self.c

    @staticmethod
    def second_method(a, b):
        print('This is static method')
        return a * b


a_1 = MyClass()
print(a_1.first_method(3, 4))

print(MyClass.second_method(3, 4))
print(a_1.second_method(3, 4))
