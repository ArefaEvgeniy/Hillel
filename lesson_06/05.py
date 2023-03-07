def my_func(b, r, **kwargs):
    print('b:', b)
    print('r:', r)
    print(kwargs)


x = 10
y = 20
z = my_func(a=y, r=99, c=15, b=x)
print('z:', z)


def my_func_2(*args, **kwargs):
    def func():
        print('Something')
        c = 99

    print('args:', args)
    print('kwargs:', kwargs)
    func()


my_func_2(12, True, None, d=45, y='RTT', c=[1, 2, 3])
