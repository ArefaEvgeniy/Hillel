# Написати програму використовуючи функції input() та print().
# Програма вимагає ввести довільну строку. Потім необхідно створити 2
# строкові змінні, перша з яких складається лише з парних символів введеної
# строки, а друга складається з введеної строки, написаної у зворотній
# послідовності, при цьому всі літери повинні бути написані у верхньому регістрі.
#
# Як результат вивести введену строку та дві нові строки, що вийшли, кожну з нового рядка.


name = input("Введіть стироку для подальшої обробки")
name1 = str(name[1::2])
name2 = str(name[-1::-1]).upper()
print('Введена строка:', name)
print('Перша строка:', name1)
print('Друга строка:', name2)
