# Створити власну версію вбудованої функції sum(). Функція sum()
# повертає суму всіх елементів об'єкта, що ітерується, переданих їй.


from functools import reduce


numbers = [1, 3, 5, 9, 33, 2, 78, 5.7, 3.44, 999]


def custom_sum(first, second):
    res = 0
    res += first if isinstance(first, (int, float)) else 0
    res += second if isinstance(second, (int, float)) else 0
    return res


result = round(reduce(custom_sum, numbers), 10)
print(result)
