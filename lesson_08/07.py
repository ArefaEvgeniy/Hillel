def my_decorator(func):
    def wrapper():
        print('Я делаю что-то до вызова функции')
        func()
        print('Я делаю что-то после вызова функции')

    return wrapper


@my_decorator
def alone_func():
    print('I am alone func')


@my_decorator
def func_2():
    print('Function 2')


alone_func()
print('-' * 100)
func_2()
#
# alone_func = my_decorator(alone_func)
# alone_func()
