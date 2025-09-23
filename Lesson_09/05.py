def add_numbers(x, y):
    if x > 0:
        return x + y
    else:
        return x - y


my_func = lambda x, y: x + y if x > 0 else x - y


print(add_numbers(-3, 5))
print(my_func(-3, 5))
