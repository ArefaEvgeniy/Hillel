import copy

first = [1, 2, 'f']
second = first[:]
third = copy.copy(first)
print(first)
print(id(first))
print(second)
print(id(second))
print(third)
print(id(third))

print(second == first)
print(second is first)

print('-' * 50)
second.append(5)
third.append(15)
print(first)
print(id(first))
print(second)
print(id(second))
print(third)
print(id(third))
