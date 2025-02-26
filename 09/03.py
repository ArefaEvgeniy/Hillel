def factorial(n):
    """
    Обчислює факторіал числа n.

    :param n: Ціле число.
    :return: Факторіал числа n.
    """
    # Базовий випадок: 0! та 1! рівні 1
    if n == 0 or n == 1:
        return 1
    else:
        # Рекурсивний виклик: n! = n * (n-1)!
        return n * factorial(n - 1)


# 5! = 1*2*3*4*5
print(factorial(5))
# 7! = 1*2*3*4*5*6*7
