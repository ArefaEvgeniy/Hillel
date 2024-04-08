def func(a=None):
    if a is None:
        a = [1, 2, 3]
    a.append(len(a))
    return a


print(func([1, 6, 7, 89, 0]))
print(func([]))
print(func(['tt', 'we']))
print(func())
print(func([77, 56, 34]))
print(func())
print(func())
