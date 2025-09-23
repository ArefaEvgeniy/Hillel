my_list = [1, 2, 0, -3, 66, 4, 5, -100, 754]


def my_func(x):
    if x > 0:
        return x ** 2
    else:
        return abs(x)


new_list = list(map(my_func, my_list))
new_list_2 = list(map(lambda x: x ** 2 if x > 0 else abs(x), my_list))
print(new_list)
print(new_list_2)
