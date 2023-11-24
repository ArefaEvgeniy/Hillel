def my_func(*args, b=44, c='RRR'):
    res = 0
    print('b:', b)
    print('c:', c)
    print('args:', args)
    for item in args:
        res += item
    return res


z = my_func(1, 2, 66, 55, 223, 888, 455, c=0)
print(z)
