a = ['a', 'b', 12, 3, 12]
print(a)
print(len(a))
print('a' in a)
print(a[-2])
print(a[:2])

a.append((1, 2, 3))
print(a)
a.append(55)
print(a)
a.insert(1, 'sss')
print(a)
a[2] = 99
print(a)
a.remove(12)
print(a)
del a[:3]
print(a)
d = a.pop()
print(a)
print(d)
a.pop(2)
print(a)

b = ['z', 'r', 'y']
a.extend(b)
print(a)
