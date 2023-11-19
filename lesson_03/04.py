import copy

my_list = [1, 'f', 'aas', None]    # 234324532, 23554643, 7876643, 24326546

first_copy = copy.copy(my_list)    # 234324532, 23554643, 7876643, 24326546
second_copy = my_list[:]           # 234324532, 23554643, 7876643, 24326546

print('my_list:', my_list, ' id:', id(my_list))
print('first_copy:', first_copy, ' id:', id(first_copy))
print('second_copy:', second_copy, ' id:', id(second_copy))

first_copy.append('555')
print('-' * 50)
print('my_list:', my_list, ' id:', id(my_list))
print('first_copy:', first_copy, ' id:', id(first_copy))
print('second_copy:', second_copy, ' id:', id(second_copy))

my_list.pop()
print('-' * 50)
print('my_list:', my_list, ' id:', id(my_list))
print('first_copy:', first_copy, ' id:', id(first_copy))
print('second_copy:', second_copy, ' id:', id(second_copy))
