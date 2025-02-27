def decorator(f):
    def wrapper():
        print('Code before func')
        f()
        print('Code after func')

    return wrapper


@decorator
def func():
    print('I am alone function')


@decorator
def func_2():
    print('I am a second function')


func()
print('-' * 50)
func_2()
# print('-' * 50)
# func = decorator(func)
# func()
