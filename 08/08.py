def func(a, b, c=45, **kwargs):
    print('a:', a)
    print('b:', b)
    print('c:', c)
    print('kwargs:', kwargs)


a = 30
func(10, a, 0)
print('-' * 50)
func(10, b=56)
