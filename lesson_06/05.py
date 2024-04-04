def func(a, f, *args):
    print(a)
    print(f)
    print(args)
    sum = 0
    for item in args:
        sum += item
    return sum


print(func(3, f=99))
