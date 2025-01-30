a = 9
...

if a == 0:
    c = 0
    print('a - None')
    ...
elif a < -100:
    if a > 50:
        print('a > 50')
        c = 50
    else:
        print('a < -100')
        c = -100
elif a > 100:
    print('a > 100')
    c = 100
elif a > 10:
    print('a > 10')
    c = 10
elif a > 0:
    print('It is a positive')
    c = 1
else:
    print('It is a negative')
    c = -1
    ...

print('c =', c)
