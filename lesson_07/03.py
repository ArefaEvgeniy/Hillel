from datetime import datetime


def factorial_1(n):
    q = 0
    result = 1
    while n > q:
        q += 1
        result *= q
    return result


def factorial_2(n):                  # 1: n=5   5 * 24 = 120
    if n == 0:                       # 2: n=4   4 * 6 = 24
        return 1                     # 3: n=3   3 * 2 = 6
    else:                            # 4: n=2   2 * 1 = 2
        return n * factorial_2(n-1)  # 5: n=1   1 * 1 = 1
                                     # 6: n=0   1


data = int(input('Enter your number: '))

time = datetime.now()
print(factorial_1(data))
print('Time spend for factorial_1:', datetime.now() - time)
print('-' * 50)

# time = datetime.now()
# print(factorial_2(data))
# print('Time spend for factorial_2:', datetime.now() - time)
