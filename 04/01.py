# кількість елементів збігається
first_list = [2, 4, 7, 11, 0, 999, 8]
first_list[1:4] = [12, 13, 14]
print(first_list)  # [2, 12, 13, 14, 0, 999, 8]

# кількість елементів, які змінюємо, більше
first_list = [2, 4, 7, 11, 0, 999, 8]
first_list[1:4] = [23]
print(first_list)  # [2, 23, 0, 999, 8]

# кількість елементів, які змінюємо, менша
first_list = [2, 4, 7, 11, 0, 999, 8]
first_list[1:3] = [33, 34, 35]
print(first_list)  # [2, 33, 34, 35, 11, 0, 999, 8]

# кількість елементів, які змінюємо, більше
first_list = [2, 4, 7, 11, 0, 999, 8]
first_list[1:4] = []
print(first_list)  # [2, 0, 999, 8]

if 7 in first_list:
    first_list.remove(7)
print(first_list)
