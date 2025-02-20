def func(a, b, *args):
    print('a:', a)
    print('b:', b)
    print('args:', args)


a = 30
func(20, 10, a, 40)
print('-' * 50)
func(20, 10, a, 40, 111, 0, 455, 34325, 55)
print('-' * 50)
func(20, 10, a)
print('-' * 50)
func(20, 10)
