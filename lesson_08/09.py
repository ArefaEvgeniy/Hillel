def decorator(func):
    def wrapper(*args, **kwargs):
        print('Before')
        res = func(*args, **kwargs)
        print('After')
        return res

    return wrapper


@decorator
def function(a, b):
    print('I am aline function:', a + b)
    return a + b


@decorator
def func_2():
    print('I am a new function')


print(function(34, 55))
print('-' * 50)
func_2()
