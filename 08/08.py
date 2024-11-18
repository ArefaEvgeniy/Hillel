def func(x, y, b, *args):
    print('x:', x)
    print('y:', y)
    print('b:', b)
    print('args:', args)
    print('-' * 100)


def func_2(*args):
    print('args:', args)
    print('-' * 100)


a = 10
b = 34
func(a, 55, 0, b, 99, 10, 101, 990, 45)
func(a, 55, 0, b)
func(a, 55, 0)

func_2()
func_2(34)
func_2(a, 55, 0)
