def decorator(func):
    def wrapper():
        print("The code before a function")
        func()
        print("The code after a function")

    return wrapper


@decorator
def along_function():
    print("I am along function")


# along_function = decorator(along_function)
along_function()
