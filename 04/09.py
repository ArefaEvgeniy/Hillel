import copy


a = [1, 4, 5, ['d', 'ee'], 6, 7]
b = copy.deepcopy(a)

print(a)
print(b)

b[3].append(44)
print('-' * 100)
print(a)
print(b)
