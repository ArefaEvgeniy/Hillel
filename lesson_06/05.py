def summa(*args, **kwargs):
    print(args)
    print(kwargs)
    return kwargs


b = 33
aa = summa(0, 1, 2, a=10, d=20, b=30, c=b, m=22, n=66, v=999)
print(aa)
