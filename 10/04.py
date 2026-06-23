def my_decorator(func):
    def wrapper():
        print("Before the function is called.")
        func()
        print("After the function is called.")
    return wrapper


@my_decorator  # along_function = my_decorator(along_function)
def along_function():
    print("I am along function!")


@my_decorator
def second_function():
    a = 100
    b = 45
    print(f"Sum of {a} and {b} is: {a + b}")


along_function()

print("------")

second_function()
