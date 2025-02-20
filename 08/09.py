def func(*args, **kwargs):
    print('args:', args)
    print('kwargs:', kwargs)


func(22, 666, 8, u=10, e=44)
