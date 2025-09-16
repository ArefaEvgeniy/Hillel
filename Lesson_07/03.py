import copy

a = [1, 4, ['a', 'f', 'd'], 5, 6, 7]
b = a.copy()
c = a[:]
d = copy.copy(a)
e = copy.deepcopy(a)

b.append(8)
c.pop()
e[2].append('RRR')
d.extend(b)

print(a)
print(b)
print(c)
print(d)
print(e)
