def my_decorator(func):
    def wrapper(*args, **kwargs):
        print('before')
        result = func(*args, **kwargs)
        print('after')
        return result
    return wrapper


@my_decorator
def func(d=1):
    print('d:', d)
    return d + 1


res = func(15)
print('res:', res)
