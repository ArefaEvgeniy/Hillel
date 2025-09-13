a = (3, 44, 67, '353', [3, 55, 9, "pp"])
b = (5, 4, 66)

print(353 in a)
print('pp' in a)

d = a[1:4]
print(a[-2])
print(d)

print(a)
print(type(a))
print(id(a))

print('-' * 40)
a += b  # a = a + b
print(a)
print(type(a))
print(id(a))

print('-' * 40)
a[4].append(100)
print(a)
print(id(a))

t = [42,]
m = (42,)
print(m)
print(type(m))

n = ()
v = tuple()
print(n)
print(v)
