# def summa(a, b, v, n):
#     c = a + b
#     print(f'Сумма {a} плюс {b} равно {c}{v}{n}')
#
#
# summa(10, 33, '?', '44')


def summa(a=1, b=0, v='!'):
    c = a + b
    print(f'Сумма {a} плюс {b} равно {c}{v}')
    return b + a


aa = summa(10, v='?', b=44)
print(aa)
