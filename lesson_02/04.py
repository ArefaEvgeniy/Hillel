a = ('s', 1, 5, [12, 4, 5, ('a', 'b')])
print(type(a))
print(len(a))
print(a)

print(a[3][3][1])

b = tuple([1, 2, 3, 45])
print(type(b))
print(len(b))
print(b)

print(12 in a)
print(12 in a[3])
print('b' in a[3])
