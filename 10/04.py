def my_decorator(func):
    def wrapper():
        print("Code before function")
        func()
        print("Code after function")

    return wrapper


def alone_function():
    print("I am alone function")


alone_function()
print("-" * 100)
new_func = my_decorator(alone_function)
new_func()
