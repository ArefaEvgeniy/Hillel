a = 3
b = 5
c = a + b

print(a + b)

a = a - 2
print(a)

a -= 2
print(a)

b *= 7
print(b)

c /= 2
print(c)

print('-' * 100)

print(a)
print(b)

a, b = b, a

print(a)
print(b)

print('-' * 100)

d = [1, 4, 77, 'rt']

a, b, c, e = d
print(a)
print(b)
print(c)
print(e)

z, v, x = 444, 34, 0
print(z)
print(v)
print(x)

print('-' * 100)

a = b = c = 101
print(a)
print(b)
print(c)

print('-' * 100)

d = [1, 4, 77, 'rt', 56, 99]
# d = [1, 4, 77, 'rt']
# d = [1, 4, 77]
a, b, c, *e = d
print(a)
print(b)
print(c)
print(e)
