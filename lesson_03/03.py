my_list = [1, 'f', 'aas', None]

first_copy = my_list
second_copy = my_list

print('my_list:', my_list, ' id:', id(my_list))
print('first_copy:', first_copy, ' id:', id(first_copy))
print('second_copy:', second_copy, ' id:', id(second_copy))

first_copy.append('555')
print('-' * 50)
print('my_list:', my_list, ' id:', id(my_list))
print('first_copy:', first_copy, ' id:', id(first_copy))
print('second_copy:', second_copy, ' id:', id(second_copy))
