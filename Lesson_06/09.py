def my_func(a, b):
    a += 5
    c = a + b ** 2
    return c
    c += 10  # зайва строка, котра ніколи не виконається


def my_func_2():
    ...
    print("Hello, world!")


a = 10
b = 4
c = my_func(a, b)
print(c)
s = my_func_2()
print(s)

...

n = 2
m = 66
res = my_func(n, m)
print(res)

...

e = []
q = 44
a = 5
w = my_func(q, a)
e.append(w)
print(e)
my_func_2()
