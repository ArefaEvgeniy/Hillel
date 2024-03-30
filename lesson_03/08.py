a = 1
b = 2.5
c = '2'
a_1 = str(a)
c_1 = int(c)

print(a + b)
print(type(a + b))

print(a + c_1)
print(a_1 + c)

print(str(int(int(a_1 + c) + b) + c_1))
