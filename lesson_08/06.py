def my_func():
    print('I am along function')


print(my_func)
my_func()
print('-' * 50)


def my_decorator(func):
    def wraper():
        print('before func')
        func()
        print('after func')

    return wraper


my_func = my_decorator(my_func)
print(my_func)
my_func()
