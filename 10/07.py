def decorator(func):
    def wrapper(*args, **kwargs):  # args = (100, 78) {"x": 56, "y":10}
        print("The code before a function")
        result = func(*args, **kwargs)  # 100, 78 x=56, y=10
        print("The code after a function")
        return result

    return wrapper


@decorator
def summa(x, y=0):
    return x + y


@decorator
def along_function():
    print("I am along function")


print(summa(y=10, x=56))
print('-' * 100)
along_function()
