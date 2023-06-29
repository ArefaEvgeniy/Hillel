a_1 = (1, 2, 3)
a_2 = a_1

print(a_1)
print(id(a_1))
print(a_2)
print(id(a_2))
a_2 = (1, 2, 3, 4)

print('-' * 50)
print(a_1)
print(id(a_1))
print(a_2)
print(id(a_2))

print('-' * 50)

first = [1, 2, 'f']
second = first
print(first)
print(id(first))
print(second)
print(id(second))

print(second == first)
print(second is first)

print('-' * 50)
second.append(5)
print(first)
print(id(first))
print(second)
print(id(second))
