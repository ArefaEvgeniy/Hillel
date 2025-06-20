def func(*args):
    print('args:', args)
    res = 0
    for item in args:
        res += item

    print('res:', res)


a = 99
w = 1
func(33, a)