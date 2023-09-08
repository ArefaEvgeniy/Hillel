from datetime import datetime


def factorial_1(n):
    q = 0
    result = 1
    while n > q:
        q += 1
        result *= q
    return result


def factorial_2(n):  # 3                                      2                         1
    if n <= 1:
        return 1
    else:
        return n * factorial_2(n - 1)  # 3 * factorial_2(2)    2 *  factorial_2(1)      1


number = int(input())

start_time_1 = datetime.now()
print(factorial_1(number))
print(f'Time_1: {datetime.now() - start_time_1}')
start_time_2 = datetime.now()
print(factorial_2(number))
print(f'Time_2: {datetime.now() - start_time_2}')
