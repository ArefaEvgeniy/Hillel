def my_func(a, b):
    if a > b:
        return (a - b) ** 2
    else:
        return (a + b) ** 2


print(my_func(7, 5))

new_func = lambda a, b: (a - b) ** 2 if a > b else (a + b) ** 2
print(new_func(7, 5))
