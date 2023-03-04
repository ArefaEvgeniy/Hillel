a = 56
b = tuple((a,))

print(type(a))
print(type(b))
print(b)

x = 1
y = 2.5
z = '2'
m = '345t'

x_1 = str(x)
z_1 = int(z)

print(x + y)
print(x + z_1)
print(x_1 + z)

print(int(x_1 + z) + x)

m.isdigit()
print(int(m))
