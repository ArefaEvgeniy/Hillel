import copy

a_1 = [1, 2, 4, 556, ['a', 'r', 'b'], 0]
a_2 = copy.deepcopy(a_1)

print(a_1)
print(id(a_1))
print(a_2)
print(id(a_2))

print('-' * 50)
print(id(a_1[3]))
print(id(a_2[3]))

print('-' * 50)
a_2[4].append('c')
print(a_1)
print(id(a_1))
print(a_2)
print(id(a_2))
