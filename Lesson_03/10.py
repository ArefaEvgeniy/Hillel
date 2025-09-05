my_list = [1, '66', 'ER', 66, 79, 66, [1, 2, 3], 12, 11, 1, 0, 5]

list_copy = my_list.copy()
list_copy_2 = my_list[:]

print(id(my_list))
print(id(list_copy))
print(id(list_copy_2))

my_list.append('TTT')
print(my_list)
print(id(my_list))
b = my_list.append(99)
my_list.append(101)
print(my_list)
my_list.insert(2, 'AA')
print(my_list)
my_list[3] = 'BB'
print(my_list)
my_list.remove(66)
print(my_list)
a = my_list[6].pop(0)
print(my_list)
# my_list.pop(6)
print(my_list)
print(a)
print(b)

print('ER' in my_list)
print(5 in my_list)
print(3 in my_list)
print([2, 3] in my_list)
