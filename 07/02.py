def calculate(a, b, c):
    d = ((a + b) * 2) / (c - 50)
    if d > 10:
        d += 10
    elif d < 10:
        d += 100
    print(d)


...
a = 34
b = 12
c = 56
calculate(a, b, c)
...
calculate(23, 12, c)
...
z = 10
f = 45
r = 55
calculate(z, f, r)
...
