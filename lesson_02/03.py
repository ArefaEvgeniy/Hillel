a = (1, 4, 0, 33, 2, '45', 9.99)

print(len(a))
print(45 in a)

print(a[3])
print(a[-2])
print(type(a[-2]))

b = a[1:-1]
print(b)
print(a)

c = (3,)
print(c)
print(type(c))

d = tuple([3])
print(d)
print(type(d))

a = (1, 4, (0, 33, 4, (2, 4, '45')), 4, 9.99, 4)

print(a)
print(len(a))
print(33 in a)

print(a[2][3][-1])

print(a.count(4))
