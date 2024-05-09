numbers = [1, 2, 3, 4, 5, 6, 7]

print(sum(numbers))
print(min(numbers))
print(max(numbers))
print(len(numbers))

values_1 = [True, False, False, False, True]
values_2 = [True, 1, True, 'esfef', [1, 1, 2, 3]]
values_3 = [False, '', (), False, 0]

print(any(values_1))
print(any(values_2))
print(any(values_3))
print('-' * 50)
print(all(values_1))
print(all(values_2))
print(all(values_3))
