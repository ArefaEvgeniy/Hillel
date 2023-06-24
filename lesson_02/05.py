a = [12, 0.55, "dsjhgd sf g", -78, 'RRR', None]
print(a)
print(id(a))
print(type(a))

a.append('p')
print(a)
print(id(a))

print(a[-1])
a.insert(1, 'RRR')
print(a)
print(id(a))

s = [1, 2, 3, [0, 99, (33, 56), 88], 97]
print(len(s))
print(s[3][2][0])

a.remove('RRR')
print(a)

del a[1]
print(a[1])
print(a)

a[1] = True
print(a)

n = a.pop(3)
print(a)
print(n)
