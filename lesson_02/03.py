a = [1, 3, '445', 0, 'eef', 345.7, 0, 99, True, None, (1, 2, ('aaa', 'Hello, world!'))]

print(type(a))

print(a)
a.append('rr')
print(a)
c = a.remove(0)
print(a)
print(a[3])
del a[2]
print(a)
print(a[3])
b = a.pop(2)
print(a)
print(b)
print(c)

a_1 = [1, 2, 3]
a_2 = [4, 5, 6]

a_1.extend(a_2)
print(a_1)
