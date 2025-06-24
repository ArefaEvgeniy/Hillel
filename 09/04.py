def factorial(n):
    """
    Обчислює факторіал числа n.

    :param n: Ціле число.
    :return: Факторіал числа n.
    """
    # Базовий випадок: 0! та 1! рівні 1
    if n <= 1:
        return 1
    else:
        # Рекурсивний виклик: n! = n * (n-1)!
        return n * factorial(n - 1)


n = 1500
# print(factorial(n))

res = 1
while True:
    res *= n
    n -= 1
    if n <= 1:
        break
print(res)
