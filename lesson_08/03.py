# Створити власну версію вбудованої функції sum(). Функція sum()
# повертає суму всіх елементів об'єкта, що ітерується, переданих їй.

from functools import reduce

numbers = [1, 0, 66, 45, -99, 23, 6]

print(reduce(lambda a, x: a + x, numbers))
print(sum(numbers))
