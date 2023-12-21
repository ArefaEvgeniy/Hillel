class MyClass_1(object):
    def my_method(self):
        print('111')


class MyClass_2(MyClass_1):
    def my_method(self):
        print('222')


class MyClass_3(MyClass_2):
    def __init__(self):
        print('INIT')


item = MyClass_3()
item.my_method()

a = 10
b = 20

if a > b:
    ...
