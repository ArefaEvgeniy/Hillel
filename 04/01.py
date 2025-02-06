import copy


first_list = [56, 6, 8, ['a', 't', 'rr'], 7]
second_list = first_list.copy()
third_list = first_list[:]
new_list = copy.deepcopy(first_list)

third_list.insert(1, 11)
second_list.pop()
new_list[3].append('RR')

print(first_list)
print(second_list)
print(third_list)
print(new_list)
