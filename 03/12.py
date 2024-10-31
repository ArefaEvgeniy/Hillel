a_1 = [34, 67.334, True, ['a', 'b', 34], 'Hello']
a_3 = [2, 3, ['a', 'b', 'c'], 4]

print(id(a_1))
print(len(a_1))

a_1.append(0)

print(a_1)
print(len(a_1))
print(id(a_1))

a_2 = 90
print(id(a_2))

a_2 = a_2 + 1
print(id(a_2))

a_1.append(a_3)
print(a_1)
print(len(a_1))

a_1.extend(a_3)
print(a_1)
print(len(a_1))
