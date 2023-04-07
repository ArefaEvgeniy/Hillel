x = 10
d = [1, 2, 3]

try:
    c = x - d[5]
    print('RES:', c)
except IndexError:
    print('IndexError')
except LookupError:
    print('LookupError')
except TypeError:
    print('TypeError')
else:
    print('else')
finally:
    print('finally')

print('After')
