first_list = [2, 4, 7]
second_list = [3, 5, 7]
my_list = first_list + second_list
print(my_list)
print(first_list)
print(second_list)

first_list = [2, 4, 7]
my_list = first_list * 3
print(my_list)

first_list.append(11)
print(first_list)
print(my_list)

new_list = []
new_list.append(first_list)
new_list.append(first_list)
print(new_list)

first_list.append(0)
print(new_list)
