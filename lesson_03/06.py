a = 45
b = float(a)
c = list((a,))
d = tuple(c)
e = bool(d)

print(a)
print(b)
print(c)
print(d)
print(e)

print('-' * 50)

a = 1
b = 2.5
c = "2"
print(a + b)

a_1 = str(a)
c_1 = int(c)

print(a + c_1)
print(type(a + c_1))
print(a_1 + c)
print(type(a_1 + c))

print(int(a_1 + c) + a)
print(type(int(a_1 + c) + a))
