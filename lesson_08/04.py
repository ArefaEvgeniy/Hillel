a = 5


def func():
    print('This is a function')


func()
b = func
b()
del func
b()
