a = 10
b = 20
c = [15, 12, None]

try:
    print('before')
    d = a / (b - c[2] - 5)
    print('after')
except (ZeroDivisionError, IndexError):
    d = 0
except LookupError:
    d = -1
# except Exception as err:
#     d = 100
#     print(err)
else:
    print('ELSE')
finally:
    print('finally')

print(d)
