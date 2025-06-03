first_list = [2, 4, 7]
second_list = [3, 5, 7]
# my_list = first_list + second_list

first_list.extend(second_list)
print(first_list)
print(len(first_list))

third_list = []
third_list.append(first_list.pop())
third_list.append(first_list.pop())
third_list.append(first_list.pop())
print(first_list)
print(third_list)

print(id(first_list))
print(id(second_list))
print(id(third_list))
