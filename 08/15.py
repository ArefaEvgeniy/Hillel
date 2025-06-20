def func(a=None):
    if a is None:
        a = ['a', 'b']
    a.append(len(a))
    return a


print(func([1, 'RRR', 'TT']))
print(func(['RRR', 'TT']))
print(func())
print(func([1, 'RRR', 'TT', 3, 2, 'rr']))
print(func())
print(func())
print(func())
