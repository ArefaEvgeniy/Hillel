def decorator(func):
    def wrapper():
        print("I am a decorator, before the function.")
        func()
        print("I am a decorator, after the function.")

    return wrapper


@decorator
def along_func():
    print("I am along function!")


# along_func = decorator(along_func)
print(along_func)
along_func()

# along_func()
# print("-" * 20)
# decorated_func = decorator(along_func)
# decorated_func()
