def decorator(func):
    def wrapper(*args, **kwargs):
        print('Code before func')
        result = func(*args, **kwargs)
        print('Code after func')
        return result

    return wrapper


@decorator
def func():
    print('I am alone function')


@decorator
def func_2(x, y=100):
    print(x + y)


@decorator
def func_3(x, y=100, z=4):
    return (x + y) / z


func()
print('-' * 50)
func_2(1, 4)
print('-' * 50)
print(func_3(10, 2))
