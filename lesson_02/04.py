# a = tuple()
a = (1, 2, 'rtr', '00', 0, 2, 2, [1, 2, 3], (3, 33, 333), True)
print(a)
print(type(a))
print(len(a))

print('-' * 100)

b = (99,)
print(b)
print(type(b))
print(len(b))

print(a[2])
print(a[-1])
print(type(a[-1]))

print(2 in a)
print(3 in a)
print((3, 33, 333) in a)

print(a[-2][0])

print(a.count(2))
