def func(a=None):
    if a is None:
        a = []
    a.append(len(a))
    return a


print(func([1, 2, 6]))
print(func([]))
print(func([2, 3]))
print(func())
print(func(['t', 't', 't']))
print(func())
print(func(['a', 'b']))
print(func())
