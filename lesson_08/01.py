result1 = map(lambda x: x**2, [1, 2, 3, 4, 5, 6])

print(list(result1))


def func(x):
    return x ** 2


result2 = map(func, [1, 2, 3, 4, 5, 6])

print(list(result2))


result3 = filter(lambda x: x % 2 == 0, [1, 2, 3, 4, 5, 6])
print(list(result3))


from functools import reduce

result4 = reduce(lambda a, x: a + x**2, [1, 2, 3], 0)
print(result4)
