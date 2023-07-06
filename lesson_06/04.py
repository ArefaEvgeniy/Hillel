def summa(a, b, c, d, *args, r=55, e='yes'):
    print(a)
    print(b)
    print(c)
    print(d)
    print(args)
    print(r)
    print(e)
    z = sum(args)
    return args


b = 33
aa = summa(10, 20, 30, b, 55, 33, e=777)
print(aa)

# a, b, *e, t = (1, 2, 4, 3, 8)
# print(a)
# print(b)
# print(e)
