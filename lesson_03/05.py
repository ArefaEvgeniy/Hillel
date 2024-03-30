import copy

a_1 = [1, 2, 4, 556]
# a_2 = a_1[:]
a_2 = copy.copy(a_1)

print(a_1)
print(id(a_1))
print(a_2)
print(id(a_2))

print('-' * 50)
a_1.append('0')
print(a_1)
print(id(a_1))
print(a_2)
print(id(a_2))
