c = [4, 6, 'rtre', [6, 6], False, 66, 445, 0, 999, 6]

print(c.count(6))
c.append([1, 2, 3])
c.append(777)
print(c)

c.insert(1, 'ttt')
print(c)

c[2] = 99
print(c)

a_1 = c.pop()
a_2 = c.pop()
c.pop()
print(c)
print(a_1)
print(a_2)

del c[2]
print(c)

a_4 = c.pop(0)
print(c)
print(a_4)

# c.pop(c.index('rtre'))
# print(c)

c.remove('rtre')
print(c)
