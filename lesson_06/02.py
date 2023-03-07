def my_func(a, b, c=0):
    print('a:', a)
    print('b:', b)
    print('c:', c)
    return a + b + c


a = 10
b = 20
c = 30
z = my_func(56, 66, 77)
print('z:', z)
print('a global:', a)
print('b global:', b)
print('c global:', c)
