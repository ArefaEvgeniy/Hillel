def my_func(a, b):
    if a > b:
        return (a - b) ** 2
    else:
        return (a + b) ** 2


print(my_func(7, 5))

new_func = lambda a, b: (a - b) ** 2 if a > b else (a + b) ** 2
print(new_func(7, 5))


def my_func_2():
    return "Hello World!"


new_func_2 = lambda: "Hello World!"

print(my_func_2())
print(new_func_2())
