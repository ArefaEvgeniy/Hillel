a = 7
b = a

print(id(a))
print(id(b))

print(a == b)
print(a is b)

a = "Liberty"
print(a)
print(b)
print(id(a))
print(id(b))

b += 1
print(b)
print(id(b))

print('-' * 50)

m = 100
n = 100
print(m)
print(n)
print(id(m))
print(id(n))
