print(12)
print()
print(13)

print('Hello', 'world', 12, 0, sep='---')
print('Hello', sep='---', end='...')
print('world', end='')
print('apple')
print('red')

source_file = open('test.txt', 'w')
print('Save', 'to', 'file', sep='...', file=source_file, end='')
source_file.close()
