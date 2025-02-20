def func(a, b, c, d):
    print('a:', a)
    print('b:', b)
    print('c:', c)
    print('d:', d)


def func_2(**kwargs):
    print('kwargs:', kwargs)


a = {'d': 10, 'a': 'red', 'c': True, 'b': 0}
# func(d=10, a='red', c=True, b=0)
func(**a)
