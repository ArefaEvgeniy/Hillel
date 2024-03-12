def func(a):
    b = 20
    c = [15, 12, None]

    try:
        print('before')
        d = a / (b - c[0] - 5)
        print('after')
    except IndexError:
        d = 0
    else:
        print('ELSE')
    finally:
        print('finally')

    print(d)


print('START')
try:
    func(10)
except ZeroDivisionError:
    print('Yes!')
else:
    print('main else')
print('END')
