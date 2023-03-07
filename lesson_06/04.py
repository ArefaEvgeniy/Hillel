def my_func(a, b, c, r=0):
    print('a:', a)
    print('b:', b)
    print('c:', c)
    print('r:', r)
    return a + b + c


x = 10
y = 20
z = my_func(y, 99, c=15)
print('z:', z)
