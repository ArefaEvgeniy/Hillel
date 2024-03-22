def func(a, b, *args, c=23, d='RR', **kwargs):
    print('a:', a)
    print('b:', b)
    print('args:', args)
    print('c:', c)
    print('d:', d)
    print('kwargs:', kwargs)

    return a + d


func(b=34, a=12, t=0)
