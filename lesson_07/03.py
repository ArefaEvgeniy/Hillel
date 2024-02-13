from datetime import datetime


def factorial(n):
    q = 0
    result = 1
    while n > q:
        q += 1
        result *= q
    return result


def factorial2(n):                              # 5    4  3  2  1  0
    if n == 0:
        return 1
    else:
        return n * factorial2(n - 1)            # 5 * 24 = 120
                                                # 4 * 6 = 24
                                                # 3 * 2 = 6
                                                # 2 * 1 = 2
                                                # 1 * 1 = 1
                                                # 1

n = 900

now = datetime.now()
print(factorial(n))
print('time of factorial1:', datetime.now() - now)

now = datetime.now()
print(factorial2(n))
print('time of factorial2:', datetime.now() - now)
