import copy

my_list = [1, 'f', 'aas', None, [1, 2, 3, 4]]    # 234324532, 23554643, 7876643, 24326546, 546777743

first_copy = copy.deepcopy(my_list)
second_copy = copy.deepcopy(my_list)

print('my_list:', my_list, ' id:', id(my_list))
print('first_copy:', first_copy, ' id:', id(first_copy))
print('second_copy:', second_copy, ' id:', id(second_copy))

first_copy[4].append('555')
first_copy.pop(1)
print('-' * 50)
print('my_list:', my_list, ' id:', id(my_list))
print('first_copy:', first_copy, ' id:', id(first_copy))
print('second_copy:', second_copy, ' id:', id(second_copy))

