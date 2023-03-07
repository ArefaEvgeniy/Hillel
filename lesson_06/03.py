def my_func(a, b, *args):
    sum = 0
    print('a:', a)
    print('b:', b)
    print('args:', args)
    for item in args:
        sum += item
    print(sum)
    return sum


z = my_func(56, 66, 678)
print('z:', z)
