lst = ['a', 'b']
my_tuple = (1, 2, lst, 4, 5)
print(my_tuple)  # виведе: (1, 2, ['a', 'b'], 4, 5)
print(id(my_tuple))

my_tuple[2][1] = 999  # змінюємо елемент списка
print(my_tuple)  # виведе: (1, 2, ['a', 999], 4, 5)
print(id(my_tuple))
