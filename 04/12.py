a = 'RRR'

with open('test.txt', 'w') as f:
    print(1, 4, 5, a, end=' ', sep='---', file=f)
print(555, sep='???', end=' ')
print('a', 'b', 'c')
