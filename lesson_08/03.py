# Створити власну версію вбудованої функції sum(). Функція sum()
# повертає суму всіх елементів об'єкта, що ітерується, переданих їй.

from functools import reduce

numbers = [1, 0, 34, 66, 45, 89, 123, 41]
liters = ['1', 'F', 'A', 'Y', 'W', 'O', 'q', 'z']

result = reduce(lambda x, y: x + y, numbers)
print(result)


def func(x, y):
    return x + y


result2 = reduce(func, liters, '->')
print(result2)
