spam = 'Spam'
print(spam)
spam = spam2 = 'Spam'
print(spam)
print(spam2)

a, b = 3, 5
# a = 3
# b = 5
print(a)
print(b)

a, b, c, d = spam
print(a)
print(b)
print(c)
print(d)

print('-' * 100)
a, b, c, *d = (4, 'ff', 'red')
print(a)
print(b)
print(c)
print(d)

a = 10
a = a + 1
a += 1

q = 10
w = 20
print('q =', q)
print('w =', w)
q, w = w, q
print('q =', q)
print('w =', w)
