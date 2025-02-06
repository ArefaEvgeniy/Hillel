a = 66
print()
print(a, end=':')
print(100, end='')
with open('text.txt', 'w') as f:
    print(100, a, '123sadas', 'yyyy:', end='', file=f, sep='---')
