my_set = {3, 0, 'red', 'black', 99, -8, (45, 66, 77, 'rt'), 'ert'}

print(len(my_set))
print('rt' in my_set)

print('-' * 100)
for item in my_set:
    print(item)

print(my_set)

input_list = [12, 'etr', 56, 77, 0, 12, 'etr', 56, 12, 0, 100, 'tt', 56]

exit_list = []
for item in input_list:
    if item not in exit_list:
        exit_list.append(item)

print(exit_list)

exit_list_2 = list(set(input_list))
print(exit_list_2)
