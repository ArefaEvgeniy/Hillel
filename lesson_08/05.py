def my_decorator(a_func):
    def wrapper():
        print('Я код который отработает до вызова функции')
        a_func()
        print('Я код который отработает после вызова функции')

    return wrapper


def my_decorator_2(a_func):
    def wrapper():
        print('-----------')
        a_func()
        print(r'\___________/')

    return wrapper


@my_decorator
@my_decorator_2
def alone_function():
    print('Я обычная функция, мой код нельзя менять')


@my_decorator
def other_function():
    print(2 + 3)


# alone_function = my_decorator(alone_function)

...

alone_function()
# print('-' * 50)
# other_function()

import time

time.sleep(1)
time.sleep(2)
time.sleep(3)

