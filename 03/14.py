a = [100, 1, 7, 88, 89, 56, 'a', 'b', 'c']

b = a[2:100]
print(b)
print(a)

print(a[0:-1:3])
print(a[-1::-2])

print(a[-1::-1])
print(a[::-1])
print(a[:])

print(a)
a.reverse()
print(a)

print(a[1:4])
a[1:4] = [-1, -2, -3]
print(a)

a[1:4] = [3]
print(a)

a[-3:] = [3, 4, 5, 6, 7, 8, 9, 0]
print(a)

first_list = [3, 4, 5, 4, 5, 34, 5, 35, -2]
first_list.sort(reverse=True)
print(first_list)

first_list = ['aas', 'rrt', 'qwx', 'qas', 'tty', 'qaa', 'rte', 'ttyiuio', 'nnmk', 'cccccccc', 'b']
first_list.sort()
print(first_list)
