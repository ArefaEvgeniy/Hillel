a = 10

print('Hello')
print(a)
print()
print('Hello', 'world', a)
print('Hello', 'world', a, sep='')
print('Hello', 'world', a, sep='---')
print('Hello', sep=' ', end='')
print('world', sep=' ')
print('!')

with open('test.txt', 'w') as new_file:
    print('Hello', 'world', a, sep='---', file=new_file, end='\n\t?')
