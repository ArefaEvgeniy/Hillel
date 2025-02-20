def func(a, b, c, d):
    print('a:', a)
    print('b:', b)
    print('c:', c)
    print('d:', d)


def func_2(*args):
    print('args:', args)


a = [44, None, 're', True]
z, x, c, v = a
func(z, x, c, v)
print('-' * 50)
# func(44, None, 're', True)
func(*a)
print('-' * 50)
func_2(*a)
