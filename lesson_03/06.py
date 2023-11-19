a = 1
b = 2.5
c = '2'
a_2 = str(a)
c_2 = int(c)

print(a + b)  # 1.0 + 2.5 = 3.5
print(a + c_2)
print(type(a + c_2))
print(a_2 + c)
print(type(a_2 + c))

print(int(a_2 + c) + a)
print(type(int(a_2 + c) + a))

d = [1, 2, 3, 4]
print(str(d))
print(str(d)[:3])

print(bool(45))
print(bool(-445))
print(bool(0))

print(int(True))
print(int(False))

print(bool('sdghdf,cnzvbd'))
print(bool(''))

print(bool([1, 2]))
print(bool({}))
