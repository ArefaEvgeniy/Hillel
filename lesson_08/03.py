# Створити власну версію вбудованої функції sum(). Функція sum()
# повертає суму всіх елементів об'єкта, що ітерується, переданих їй.


from functools import reduce

numbers = [1, 0, 66, 45, -99, 23, 6]


def custom_sum(first, second):
    return first + second


result_1 = reduce(custom_sum, numbers, 0)
print(result_1)

result_2 = reduce(lambda a, b: a + b, numbers)  # 36 + 6 = 42
print(result_2)
