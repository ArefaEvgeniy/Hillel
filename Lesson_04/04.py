a = 1
print(a)
print('Hello')
print('Hello', a, 11, 'RR')
print()
print(1 * 20 + 44)

print('Hello', a, 11, 'RR', sep='')
with open('file.txt', 'w') as f:
    print('Hello', a, 22, 'EE\n\nTT\tRR', sep='-', file=f)
print('Hello', a, 11, 'RR', sep='-', end=' ')
...
print('After something important')
print('Continue...', sep='-')


a = [1, 2, 76, 0, 4, 3, 5]
len_list = len(a)
i = 0
while i < len_list:
    a[i]
    i += 1

