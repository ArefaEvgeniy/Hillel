def my_decorator(func):
    def wraper(*args, **kwargs):
        print('Я код до виклику функції')
        result = func(*args, **kwargs)
        print('Я код після виклику функції')
        return result

    return wraper


@my_decorator
def some_func():
    print('Я самотня функція')


@my_decorator
def some_func_2():
    print('Я друга самотня функція')


some_func()
print('-' * 50)
some_func_2()
