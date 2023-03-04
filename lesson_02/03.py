a = [1, 2, '33', 'rrg']
print(id(a))

a.append('p')
print(a)
print(id(a))

a.append([1, 2, 3])
print(a)
print(len(a))
print(id(a))

a.insert(0, 99)
print(a)
print(len(a))
print(id(a))

a[1] = 100
print(a)

a[-1] = 99
print(len(a))
print(a)

c_2 = a.remove(99)
print(len(a))
print(a)

del a[1]
print(len(a))
print(a)

c_1 = a.pop(1)
print(len(a))
print(a)
print(c_1)
print(c_2)

b = [1, 2, 3]

a.extend(b)
print(len(a))
print(a)
