def func(*args, a, r):
    print('a:', a)
    print('r:', r)
    print('args:', args)


a = 99
w = 1
func(33, a, 5, 66, 100, r=400, a=0)
