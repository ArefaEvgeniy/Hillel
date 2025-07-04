def decorator_with_args(prefix="DEBUG"):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print(f"{prefix}: Something is happening before the function is called.")
            result = func(*args, **kwargs)
            print(f"{prefix}: Something is happening after the function is called.")
            return result
        return wrapper
    return decorator


@decorator_with_args("LOG")
def say_hello():
    print("Hello!")


@decorator_with_args("INFO")
def greet():
    print("Greetings!")


@decorator_with_args()
def farewell():
    print("Farewell!")


# Виклик функції з декоратором із аргументами
say_hello()
greet()
farewell()
