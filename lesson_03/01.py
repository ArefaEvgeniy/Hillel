a, b = 10, 25

print(a)
print(b)

a, b = b, a

print('-' * 50)
print(a)
print(b)

a = b = c = 100

print('-' * 50)
print(a)
print(b)
print(c)

a, b = {12: 34, 'red': 'AA'}
print('-' * 50)
print(a)
print(b)

a, b, c, d = 'spam'
print('-' * 50)
print(a)
print(b)
print(c)
print(d)

q = (1, 2, 3, 4, 5, 6, 10, 33, 23)
a, b, *c = q
print('-' * 50)
print(a)
print(b)
print(c)
print(q)

q = [1, 2]
a, b, *c = q
print('-' * 50)
print(a)
print(b)
print(c)
