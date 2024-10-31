first_list = [2, 4, 7, 11, 0, [44, 'eert', 'world'], 999, 8]


import copy
second_list = copy.deepcopy(first_list)


print(id(first_list))
print(id(second_list))

first_list[5].append('TTR')
print(first_list)
print(second_list)
