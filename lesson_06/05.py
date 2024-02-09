def my_func(c, **kwargs):
    print('c:', c)
    print('kwargs:', kwargs)


my_func(b=44, c=33, a=66)
my_func(44, b=33, a=66)
my_func(44)
