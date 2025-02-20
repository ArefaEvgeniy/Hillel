def func(a, b, c=None, d=0):
    print('a:', a)
    print('b:', b)
    print('c:', c)
    print('d:', d)


a = 30
func(20, 10, a, 40)
print('-' * 50)
func(20, 10, a)
print('-' * 50)
func(20, 10)
print('-' * 50)
func(b=20, a=10)
