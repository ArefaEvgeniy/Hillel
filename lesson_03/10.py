a = 10
b = 'RRR'

print(a, b, 45)
print(a, b, 45, sep='---')
print(a, b, 45, sep='')
print()
print(a, sep='---')
print(a, b, 45, end='   ')
print(77, 55, sep='!')
print(444)

my_file = open('test.txt', 'w')
print(a, b, 45, sep='---', end='\n\n', file=my_file)
print(a, sep='!!!', file=my_file, end='???')
my_file.close()
