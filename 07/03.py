my_list = [4, 55, 100, 1, 4, '1', 2, 1, 'TTTYE', 2, 4, 0, 'ERRETYER', 1, 4, 3, 1, 0, 11, 100, 1, 4]

new_list = []
for item in my_list:
    if item not in new_list:
        new_list.append(item)

print(new_list)

new_list_2 = list(set(my_list))
print(new_list_2)
