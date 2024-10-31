first_list = [2, 4, 7, 11, 0, 999, 8]

# second_list = first_list.copy()
# second_list = first_list[:]
import copy
second_list = copy.copy(first_list)


print(id(first_list))
print(id(second_list))

first_list.append('TTR')
print(first_list)
print(second_list)
