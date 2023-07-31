def my_func(a, b):
    try:
        print('START Func')
        c = a / b
        print('END Func')
    except TypeError:
        c = 0
    finally:
        print('finally 1')
    return c


a = 10
b = 0

try:
    print(my_func(a, b))
except ZeroDivisionError:
    print('Global Except')
else:
    print('ELSE')
finally:
    print('finally 2')
print('FINISH')
