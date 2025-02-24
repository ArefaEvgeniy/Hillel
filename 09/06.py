def func(x):
    return x + 5


a = [1, 2, 3, 4, 7, 9]
new_list = list(map(func, a))
print(new_list)

new_list_2 = list(map(lambda x: x+5, a))
print(new_list_2)


def func_2(x):
    x.pop()
    return x


a_2 = [[1, 5, 6], [2, 6], [3, 0], [4, 9], [7, 99], [9]]
new_list_3 = list(map(func_2, a_2))
print(new_list_3)
