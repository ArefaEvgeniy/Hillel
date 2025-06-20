def func(r, e=10, a=10, *args, **kwargs):
    print('Work!')
    print('r:', r)
    print('args:', args)
    print('e:', e)
    print('a:', a)
    print('kwargs:', kwargs)


# func()
# func(67)
# func(67, 66, 34, 23, 77)
func(67, 23, 77, 99, 55, b=66, c=34)
