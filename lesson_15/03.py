def func(a, b):
    try:
        res = 10 / a
        res = res - b['c']
        print('next')
    except KeyError:
        res = 100
    except ZeroDivisionError:
        res = 0
    else:
        print('ELSE')
    finally:
        print('FINALLY')

    res += 11

    return res


print('START')
c = 1 + 1 - 3
d = {'a': 1, 'b': 2, 3: 'rt'}

try:
    x = func(c, d)
    print('next 2')
except KeyError:
    x = None

print('x:', x)
print('END')
