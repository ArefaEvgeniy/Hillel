print('START')
c = 1 + 1 - 2
d = {'a': 1, 'b': 2, 3: 'rt'}

try:
    x = 10 / c
    x = x - d[3]
    print('next')
except IndexError:
    x = None
except KeyError:
    x = 100
except LookupError:
    x = -100
except ZeroDivisionError:
    x = 0
except Exception as irina:
    print(irina)
    x = 0

print('x:', x)
print('END')
