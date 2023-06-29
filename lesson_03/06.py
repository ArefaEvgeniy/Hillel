
my_file = open('python.txt', 'w')
print(123, 445, 'rrt', sep='-', end='   ', file=my_file)
my_file.close()
print('!!!')
print('New line')
