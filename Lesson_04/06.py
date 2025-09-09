my_list = [1, 4, 7.5, -9, '6ghjgf', 0, 3, 5, 6, 'exit', 8, 2, 11, 15, -4, 0.5]

list_int = []
list_float = []
list_negative = []

i = 0
while i < len(my_list):
    if isinstance(my_list[i], (int, float)) and my_list[i] < 0:
        list_negative.append(my_list[i])
    elif isinstance(my_list[i], int):
        list_int.append(my_list[i])
    elif isinstance(my_list[i], float):  # type(my_list[i]) == float
        list_float.append(my_list[i])
    i += 1

print('list_int:', list_int)
print('list_float:', list_float)
print('list_negative:', list_negative)


print('-' * 50)
list_int = []
list_float = []
list_negative = []

for index, item in enumerate(my_list):
    print('index:', index, 'item:', item)
    if isinstance(item, (int, float)) and item < 0:
        list_negative.append(item)
    elif isinstance(item, int):
        list_int.append(item)
    elif isinstance(item, float):  # type(my_list[i]) == float
        list_float.append(item)
    elif str(item) == 'exit':
        print('BREAK', 'index:', index)
        break
else:
    print('FOR ELSE')

print('list_int:', list_int)
print('list_float:', list_float)
print('list_negative:', list_negative)
