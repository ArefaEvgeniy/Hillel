a = tuple('s')

print(a)
print(type(a))

a_1 = ('s', 12, True, None, (5.5, 3.4, 0.0))

print(a_1)
print(type(a_1))

print(len(a))
print(len(a_1))

print(12 in a_1)
print(None in a_1)
print(None in a)
print(3.4 in a_1)

print(a_1[1::2])

print(a_1[10])
