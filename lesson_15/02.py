print('START')
c = 1 + 1 - 2
d = {'a': 1, 'b': 2, 3: 'rt'}

try:
    x = 10 / c
    x = x - d['b']
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
else:
    print('ELSE')
finally:
    print('FINALLY')

print('x:', x)
print('END')

try:
    f = open('ere.txt')
    ...
finally:
    f.close()
