def my_decorator(a_func):
    def wraper(*args, **kwargs):
        print('Я код котрий відпрацьовую до функції')
        result = a_func(*args, **kwargs)
        print('Я код котрий відпрацьовую після функції')
        return result

    return wraper


@my_decorator
def some_func(a):
    print('Я самотня функція')
    print(a)
    return a + 1


new_a = some_func(777)
print(new_a)
