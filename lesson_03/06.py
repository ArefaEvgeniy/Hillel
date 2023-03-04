a = 10
b = 'red'

print(a, b, 'Tree', sep='', end='\t')
print('BBB')
print(12)

source_file = open('test.txt', 'w')
print('It-s cool', 'red?', sep='<<<>>>', file=source_file)
source_file.close()
