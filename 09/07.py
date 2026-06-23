def dn(x):
    if x < 0:
        return x + 10
    elif x == 0:
        return x + 100


my_list = [-5, 0, 3, -2, 7, -1, 4, 100]
print(list(map(dn, my_list)))
dn_new = lambda x: x + 10 if x < 0 else x * 2
print(list(map(lambda x: x + 10 if x < 0 else x * 2, my_list)))
print(list(map(dn_new, my_list)))

print(list(map(lambda x: x > 0, my_list)))
