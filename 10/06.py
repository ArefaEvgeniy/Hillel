def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Code before function")
        result = func(*args, **kwargs)
        print("Code after function")
        return result

    return wrapper


@my_decorator   # alone_function = my_decorator(alone_function)
def alone_function():
    print("I am alone function")
    return "Happy New Year!"


@my_decorator
def alone_function_2(name):
    print(f"I am a second alone function. Hello {name}")


answer = alone_function()
print(answer)
print("-" * 50)
alone_function_2('Bob')
