def calculate(a, b, c):
    d = ((a + b) * 2) / (c - 50)
    if d > 10:
        d += 10
    elif d < 10:
        d += 100
    return d, 100, "Hello world"


def my_func():
    print("Hello world")


...
a = 34
b = 12
c = 56
d, m, n = calculate(a, b, c)
my_func()
print(d)
print(m)
print(n)
...
result = calculate(23, 12, c)
my_func()
...
z = 10
f = 45
r = 55
w = calculate(z, f, r)
my_func()
my_rez = [d, result, w]
...
print(my_rez)
