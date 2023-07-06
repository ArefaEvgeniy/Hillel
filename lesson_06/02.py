def summa(a, b):
    def xxx(z):
        print(f'value of z: {z}')

    c = a + b
    print(f'Сумма {a} плюс {b} равно {c}')
    xxx(c)
    return a, b, c


x, y, z = summa(10, 12)
print(x)
print(y)
print(z)

x, y, z = (10, 12, 22)
