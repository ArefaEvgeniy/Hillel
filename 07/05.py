import time


def my_func(x):
    if x > 0:
        result = x + 10
    elif x < 0:
        result = x - 1
    else:
        result = 0

    return result


def func_2():
    print('New func')
    time.sleep(2)
    print('Stop func')


a = 10
s = -55
...
res = my_func(a)
...
new = my_func(s)
...
d = 0
new_2 = my_func(d)
...
print(res)
print(new)
print(new_2)

r = func_2()
print(r)

_ = my_func(100)
