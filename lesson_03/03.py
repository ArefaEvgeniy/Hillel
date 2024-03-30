a_1 = 5
a_2 = 5

print(a_1)
print(id(a_1))
print(a_2)
print(id(a_2))

a_1 = a_1 + 1

print('-' * 50)
print(a_1)
print(id(a_1))
print(a_2)
print(id(a_2))

print('-' * 50)
a_1 = 'aaa'
a_2 = 'aaa'

print(a_1 == a_2)

print(a_1)
print(id(a_1))
print(a_2)
print(id(a_2))

print('-' * 50)
a_1 = a_1 + 'ee'
print(a_1)
print(id(a_1))
print(a_2)
print(id(a_2))
