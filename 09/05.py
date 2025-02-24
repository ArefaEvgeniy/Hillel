def func(x):
    if x % 2 == 0:
        res = x ** 2
    else:
        res = x ** 3
    return res


squared_numbers = [func(x) for x in range(1, 9)]
print(squared_numbers)

squared_numbers_2 = [(lambda x: x ** 2 if x % 2 == 0 else x ** 3)(x) for x in range(1, 9)]
print(squared_numbers_2)
