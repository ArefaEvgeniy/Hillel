def func_2(b, c, e=None, **kwargs):
    print('b:', b)
    print('c:', c)
    print('e:', e)
    print('kwargs:', kwargs)
    print('-' * 100)


a = 10
b = 34

func_2(11, 33, x=a, e=b, y=100)
func_2(11, 33)
