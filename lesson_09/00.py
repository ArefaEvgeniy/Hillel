def my_decorator(a_func):
    def wrapper(*args, **kwargs):
        print('Я код который отработает до вызова функции')
        res = a_func(*args, **kwargs)
        print('Я код который отработает после вызова функции')
        return res

    return wrapper


@my_decorator
def alone_function(a=10, b=50):
    print(f'{a} плюс {b} равно: {a + b}')
    return a + b


# alone_function = my_decorator(alone_function)

print(alone_function(2, 3))
