def summa(a, b):
    print('a:', a)
    print('b:', b)
    res = a + b
    res += 1
    res /= 3
    res = round(res)
    return res   # 10   A3344FF00


a = 10
b = 20

c = summa(a, b)   # c = A3344FF00
print(c)

c_1 = summa(2, 66)
print(c_1)

c_2 = summa(c, c_1)
print(c_2)
