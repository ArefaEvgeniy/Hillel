def func(x):
    return x ** 3


a = [-1, 2, 0, 4, -7, 9, -100, 99]
new_list = list(filter(func, a))
print(new_list)

new_list_2 = list(filter(lambda x: x > 0, a))
print(new_list_2)
