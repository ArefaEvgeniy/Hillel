def my_decorator(func):
    def wraper():
        print('before func')
        func()
        print('after func')

    return wraper


def my_decorator2(func):
    def wraper():
        print('------------')
        func()
        print('///////////////')

    return wraper


@my_decorator
@my_decorator2
def my_func():
    print('I am along function')


@my_decorator
def my_func2():
    print('I am function 2')


@my_decorator
def my_func3():
    print('I am function 3')


my_func()
print('-' * 50)
my_func2()
print('-' * 50)
my_func3()
