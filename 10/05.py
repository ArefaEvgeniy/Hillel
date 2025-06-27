def decorator(func):
    def wrapper():
        print("The code before a function")
        func()
        print("The code after a function")

    return wrapper


def along_function():
    print("I am along function")


along_function()
my_func = decorator(along_function)

print('-' * 100)
my_func()
