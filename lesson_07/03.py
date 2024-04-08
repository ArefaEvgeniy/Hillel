n = 5


def ractorial_1(x):
    q = 0
    result = 1
    while x > q:
        q += 1
        result *= q
    return result


print(ractorial_1(n))


def factorial_2(x):
    if x <= 1:
        return 1
    return x * factorial_2(x - 1)


print(factorial_2(n))
