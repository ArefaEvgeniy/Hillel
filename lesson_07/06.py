def func(d=None):
    if d is None:
        d = [1, 2, 3]
    d.append(len(d))
    return d


print(func([1, 2, 3, 4, 5]))
print(func([0, 3, 4, 1]))
print(func())
print(func([]))
print(func())
print(func())
print(func())
print(func([1, 1]))
print(func())
