a = '32jkdfvnijfdh8754yhnf56dkcnwoe;rgui9098763'

b = [i for i in a if i.isdigit()]
b_2 = [i for i in a if 'a' <= i <= 'k']

print(b)
print(b_2)
print(''.join(b))
