def my_func(a):
    a += 1
    b = a ** 2
    print('Something')
    print('Result =', b)
    print('-' * 50)
    return b, 10, True


a = 10
my_func(a)

...

my_func(1)

...

c, x, y = my_func(5)
print('c:', c)
print('x:', x)
print('y:', y)
