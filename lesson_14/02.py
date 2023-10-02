class MyClass:
    def first_method(self):
        print('This is general method')

    @staticmethod
    def second_method():
        print('This is class method')


a = MyClass()
a.first_method()
a.second_method()

MyClass.second_method()
