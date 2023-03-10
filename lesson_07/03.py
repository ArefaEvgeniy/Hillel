# Вычисления факториала

from datetime import datetime

n = 900


def factorial_1(n):
    q = 1
    result = 1
    while n >= q:
        result *= q
        q += 1
    return result


def factorial_2(n):  # 5
    if n == 1:
        return 1
    else:
        return n * factorial_2(n-1)   # 5 * 4 * 3 * 2 * 1


now = datetime.now()
print(factorial_1(n))
print(datetime.now() - now)
now = datetime.now()
print(factorial_2(n))
print(datetime.now() - now)
