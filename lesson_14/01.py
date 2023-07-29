class MyClass():

    @staticmethod
    def first_method(a, b):
        print("This is statis method")
        print(a + b)

    def second_method(self):
        print("This is general method")


MyClass.first_method(2, 3)
a_1 = MyClass()
a_1.second_method()
a_1.first_method(4, 5)
