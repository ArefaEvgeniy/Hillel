def func(y, x=None, b=None, a='RED'):
    print('x:', x)
    print('y:', y)
    print('b:', b)
    print('a:', a)
    print('-' * 100)


a = 10
c = 34
func(a, 55, 0, 'RR')
func(True)
func(44, 67, a='Black', b=10)
func(44, a='Black', b=10)
