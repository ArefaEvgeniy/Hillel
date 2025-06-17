def my_func(a, b):
    if a > 0:
        rez = a + b
    elif a == 0:
        rez = b
    else:
        rez = a - b
    print(rez)
    print('-' * 100)
    my_func_2()
    return rez


def my_func_2():
    print('_' * 100)
    print('Hello world!' * 100)
    print('_' * 100)


a = 11
b = 34

# print = 77

my_func(a, b)
# my_func_2()

c = 0
d = 55

my_func(c, b)

...

r = my_func(d, b)
# my_func_2()

...

print('r:', r + 5)

ss = my_func

ss(44, 55)
