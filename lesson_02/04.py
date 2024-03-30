a = [1, 4, 0, [33, 2, '45'], 9.99]

print(a)
print(type(a))
print(len(a))
print(45 in a)

print(a[3])
print(a[-2])
b = a[1:-1]
print(b)

print(a[3][1:])  # [1, 4, 0, [33, 2, '45'], 9.99]

a.append((1, 2, 3))
print(a)
a.insert(1, ['a', 'b', 'c'])
print(a)
a.append(0)
print(a)
c = a.remove(0)
print(a)
a.pop()
print(a)
a.pop()
print(a)
b = a.pop(1)
print(a)
print(b)
print(c)

del a[1]
print(a)

print('-' * 100)
print(a)
print(b)
a.extend(b)
print(a)
