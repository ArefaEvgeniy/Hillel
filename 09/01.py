def func_1(a, s, g, *args, k, w, **kwargs):
    print('FUNC 1')
    print('a:', a)
    print('s:', s)
    print('g:', g)
    print('args:', args)
    print('k:', k)
    print('w:', w)
    print('kwargs:', kwargs)


def func_2(a, s, g, k, w, *args, **kwargs):
    print('FUNC 2')
    print('a:', a)
    print('s:', s)
    print('g:', g)
    print('args:', args)
    print('k:', k)
    print('w:', w)
    print('kwargs:', kwargs)


func_1(1, 2, 3, 4, 5, 6, 7, w=11, k=12, n=13, m=14)
func_2(1, 2, 3, 4, 5, 6, 7, w=11, k=12, n=13, m=14)
