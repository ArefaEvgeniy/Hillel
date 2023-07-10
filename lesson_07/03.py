from datetime import datetime


n = 995


def factorial_1(n):
    q = 0
    result = 1
    while n > q:
        q += 1
        result *= q
    return result


def factorial_2(n):     # n = 3, n = 2, n = 1, n = 0
    if n == 0:
        return 1
    else:
        return n * factorial_2(n-1)     # 3 * factorial_2(2)  # 2 * factorial_2(1)  # 1 * factorial_2(0)


time = datetime.now()
print(f'factorial_1: {factorial_1(n)}')
print(f'Time: {datetime.now() - time}')
print('-' * 50)
time = datetime.now()
print(f'factorial_2: {factorial_2(n)}')
print(f'Time: {datetime.now() - time}')
