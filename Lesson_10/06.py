def decorator(func):
    def wrapper(*args, **kwargs):
        print("I am a decorator, before the function.")
        res = func(*args, **kwargs)
        return res

    return wrapper


@decorator
def along_func():
    print("I am along function!")


@decorator
def along_func_2():
    print("I am along second function!")


@decorator
def summa(a, b):
    return a + b


along_func()
print("-" * 20)
along_func_2()
print("-" * 20)
print(summa(3, 6))

