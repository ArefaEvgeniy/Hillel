import copy

a = [1, 4, 5, 6, 7]
# b = a[:]
# b = a.copy()
b = copy.copy(a)

print(a)
print(b)

b.append(44)
print('-' * 100)
print(a)
print(b)
