a = [1, 7, 88, 89, 56]
b = ['a', 'b', 'c']

print(id(a))
a.append(99)
print(a)

a.append(b)
print(a)

a.extend(b)
print(a)
print(id(a))

a.insert(2, 100)
print(a)

a[3] = 99
print(a)
print(id(a))

if 99 in a:
    a.remove(99)
    print(a)

del a[-1]
print(a)

e = a.pop()
print(a)
print(e)

d = a.pop(2)
print(a)
print(d)
