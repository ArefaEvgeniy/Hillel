def my_decorator(a_func):   # 8888556565, a_func=5757573453
    def wraper():   # 33334455
        print('Я код котрий відпрацьовую до функції')
        a_func()    # 5757573453
        print('Я код котрий відпрацьовую після функції')

    return wraper


def my_decorator_2(a_func):   # 8888556565, a_func=5757573453
    def wraper():   # 33334455
        print('----')
        a_func()    # 5757573453
        print('||||||')

    return wraper


@my_decorator
@my_decorator_2
def some_func():    # 5757573453
    print('Я самотня функція')


@my_decorator
def some_func_2():    # 5757573453
    print('Я самотня функція 2')


# some_func()
# print('-' * 50)
# some_func = my_decorator(some_func)     # 33334455
some_func()
print('-' * 50)
some_func_2()
