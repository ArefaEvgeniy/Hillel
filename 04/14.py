my_list = [1, 2, 1000, 3, 10000, -88767, 5, 99, -100, 0, 10001]

new_list = []
for item in my_list:
    if item > 0:
        if item % 2 == 0:
            new_list.append(item * 2)
        else:
            new_list.append(item * 3)
print(new_list)


# new_list_2 = [stas * 3 for stas in my_list if stas > 0]
new_list_2 = [(stas * 2 if stas % 2 == 0 else stas * 3) for stas in my_list if stas > 0]
print(new_list_2)
