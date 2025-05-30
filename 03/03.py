a = 101

if a > 100:
    print('a > 100')
    a -= 35
    c = True
else:
    if a < 0:
        print('a < 0')
        a = abs(a)
    else:
        print('0 <= a <= 100')
    print('ELSE')

print("a:", a)
print('END')
