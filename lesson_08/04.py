# Создать собственную версию встроенной функции sum().
# Функция sum() возвращает сумму всех элементов итерируемого объекта,
# переданных ей.

from functools import reduce

numbers = [3, 4, 6, 9, 34, 12]


def func(first, second):
    return str(first) + str(second)


result = reduce(func, numbers, 100)
print('result:', result)

result_2 = reduce(lambda x, y: x * y, numbers)
print('result_2:', result_2)
