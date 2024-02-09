def my_func(*args):
    print('args:', args)
    return 111, 222, 333


res = my_func(44, 33)
print('res:', res)
my_func(44)

# res1, res2, res3 = my_func('', d=44, b=55)
# print('res1:', res1)
# print('res2:', res2)
# print('res3:', res3)
my_func()
