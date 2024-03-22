# def func(a=None):
#     if a is None:
#         a = [0, 4, 5]
#     a.append(len(a))
#     return a


def func(a=[0, 4, 5]):
    a = a[:]
    a.append(len(a))
    return a


b = func([1, 2, 3, 4, 99])
print(b)

c = func([99, 101])
print(c)

d = func()
print(d)

e = func([])
print(e)

f = func()
print(f)

h = func()
print(h)
