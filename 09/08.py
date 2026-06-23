def dn(x):
    return x + 2


my_list = [-5, 0, 3, -2, 7, -1, 4, 100]
print(list(filter(dn, my_list)))
print(list(filter(lambda x: x > 0, my_list)))
