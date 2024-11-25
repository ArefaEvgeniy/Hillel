def my_decorator(func):
    def wrapper():
        print("Code before function")
        func()
        print("Code after function")

    return wrapper


def my_decorator_2(func):
    def wrapper():
        print("/--------\\")
        func()
        print("\\--------/")

    return wrapper


@my_decorator   # alone_function = my_decorator(alone_function)
def alone_function():
    print("I am alone function")


@my_decorator_2
@my_decorator
def alone_function_2():
    print("I am a second alone function")


alone_function()
print("-" * 50)
alone_function_2()
