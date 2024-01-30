a = 100
print(a, 'werwe', 'RRR', 98, sep='---', end='!')
# print()
print(a)
print('TTT', sep='///', end='')
print('AAA')

my_file = open('test.txt', 'w')
print(a, 'werwe', 'RRR', 98, sep='---', file=my_file)
my_file.close()
