def func_2(*args, **kwargs):
    print('args:', args)
    print('kwargs:', kwargs)
    print('-' * 100)


a = 10
b = 34

func_2()
func_2(11, 33, x=a, e=b, y=100)
func_2(11, 33)
func_2(x=a, e=b, y=100)
func_2(33)
