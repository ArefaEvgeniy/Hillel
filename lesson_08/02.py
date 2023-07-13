from functools import reduce


numbers = [2, 44, 67, 34, 12]


def my_func(a, b):
    return a * b


result = reduce(my_func, numbers)
print(result)


# [2, 44, 67, 34, 12]
# 1) my_func(2, 44) = 88
# 2) my_func(88, 67) = 5896
# 3) my_func(5896, 34) = 200464
# 4) my_func(200464, 12) = 2405568
