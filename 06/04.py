lst = ['a', 'b']
my_tuple = (1, 2, lst, 4, 5)
print(my_tuple)  # виведе: (1, 2, ['a', 'b'], 4, 5)


my_tuple[2][1] = 999  # змінюємо елемент списка
# print(my_tuple)  # виведе: (1, 2, ['a', 999], 4, 5)

print(2 in my_tuple)
print('a' in my_tuple)
print(['a', 999] is my_tuple)
print(lst in my_tuple)

lst_2 = ['a', 'b']
lst_3 = ['a', 'b']
lst_4 = ['a', 'b']

print(id(lst_2))
print(id(lst_3))
print(id(lst_4))

print(len(my_tuple))
