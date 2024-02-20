def my_decorator(func):
    def wraper(*args, **kwargs):
        print('before func')
        res = func(*args, **kwargs)
        print('after func')
        return res

    return wraper


# my_func = my_decorator(my_func)

@my_decorator
def my_func(a, b):
    print('I am along function')
    d = a + b
    print('d:', d)
    return d + 1


res = my_func(12, 13)
print('res:', res)
