def func(*args):
    print(args)
    sum = 0
    for item in args:
        sum += item
    return sum


# print(func(33, 44))
# print(func(33, 44, 55))
# print(func(33, 44, 55, 77))
# print(func(33, 44, 55, 77, 9))
# s = [33, 44, 55, 77, 9, 66, 34, 0, 100, -34]
# print(func(s))
print(func(33, 44, 55, 77, 9, 66, 34, 0, 100, -34))
print(func(33, 44))
print(func(33))
print(func())
