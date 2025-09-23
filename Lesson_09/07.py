my_list = [1, 2, 0, -3, 66, 4, 5, -100, 754]


def my_func(x):
    if x > 0:
        return True
    else:
        return False


new_list = list(filter(my_func, my_list))
new_list_2 = list(filter(lambda x: True if x > 0 else False, my_list))
new_list_3 = list(filter(lambda x: x > 0, my_list))
# new_list_3 = list(filter(lambda x: x, my_list))
print(new_list)
print(new_list_2)
print(new_list_3)
