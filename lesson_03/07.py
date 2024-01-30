a = 1
b = 2.5
c = '2'

print(a + b)
print(str(a) + c)
print(type(str(a) + c))
print(a + int(c))
print(type(a + int(c)))
print(a + float('2.7'))

print(int((str(a) + c) + c) + b)
