def func(a=None):
    if a is None:
        a = [1, 2, 3]
    a.append(len(a))
    return a


print(func([2, 3, 4, 5]))
print(func())
print(func([]))
print(func())
print(func())
print(func())
print(func([2, 3, 4, 5, 6, 7, 8, 9]))
print(func())
