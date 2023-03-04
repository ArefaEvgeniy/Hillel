a = 'Liberty'
print(id(a))

b = 17
print(id(b))

c = 17
print(id(c))

print(b == c)
print(b is True)

c += 1  # c = 18
print(id(c))

print('b:', b)
print('c:', c)

x = 'bbb'
y = 'bbb'
print('x:', x)
print('id(x):', id(x))
print('y:', y)
print('id(y):', id(y))

y = y.upper()   # y = 'BBB'
print('y:', y)
print('id(y):', id(y))
