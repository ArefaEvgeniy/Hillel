def decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Before calling {func.__name__}")
        result = func(*args, **kwargs)
        print(f"After calling {func.__name__}")
        return result
    return wrapper


def summa(*args):
    return sum(args)


@decorator
def func_1():
    print("I am func_1!")


@decorator
def func_2(a=0, b=0):
    return a + b


func_1()
print("-" * 20)
res = func_2(10, 23)
print(f"Result of func_2: {res}")
