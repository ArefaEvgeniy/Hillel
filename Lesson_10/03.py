def func():
    """This is a docstring."""
    print("Hello, World!")


print(func)
new_func = func
print(new_func)

new_func()

del func

new_func()

oleksandr = print

oleksandr("Hello, Olexandr!", end="!!!\n\n")
