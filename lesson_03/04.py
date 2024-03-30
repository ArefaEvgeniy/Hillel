a_1 = [1, 2, 4]
a_2 = [1, 2, 4]

print(a_1 == a_2)
print(a_1 is a_2)

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
