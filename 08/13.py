def func_1(e, w, a, *args):
    print('e:', e)
    print('w:', w)
    print('a:', a)
    print('args:', args)


a = [5, 3, 2, 5, 3, 22, 2134, 4]
func_1(*a)
