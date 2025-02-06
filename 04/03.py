n = 1
summa = 0

n -= 1
while n < -100:
    n = n + 1
    print('n:', n)
    if summa > 1500:
        break
    if n % 2 == 0:
        if n % 10 == 0:
            continue
        summa += n
else:
    print('else')

print('summa:', summa)
print('End')
