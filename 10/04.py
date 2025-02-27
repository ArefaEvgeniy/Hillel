def decorator(f):
    def wrapper():
        print('Code before func')
        f()
        print('Code after func')

    return wrapper


@decorator
def func():
    print('I am alone function')


func()
# print('-' * 50)
# func = decorator(func)
# func()
