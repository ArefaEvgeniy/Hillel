# Напишіть функцію, яка приймає на вхід список чисел та повертає суму
# квадратів тільки парних чисел зі списку, використовуючи функціональні 
# підходи (наприклад, map, filter та reduce).
#
# Приклад:
# Введіть числа: 4, 6, 3, 4, 2, 3, 9, 0, 7
# Результат: 72


from functools import reduce


def sq_sum(s):
    filt = filter(lambda x: x % 2 == 0, s)
    sqmap = map(lambda x: x * x, filt)
    sumsq = reduce(lambda x, y: x + y, sqmap)
    return sumsq


i = map(int, input("Введіть числа: ").split(", "))
print("Результат:", sq_sum(i))
