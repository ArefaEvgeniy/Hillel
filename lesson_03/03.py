a = 777

print(id(a))

b = 777
print(id(b))

b += 1
print(a)
print(b)
print(id(a))
print(id(b))

c = 'red'
d = 'red'
print(c)
print(d)
print(id(c))
print(id(d))

e = [12, 11, 10]
f = [12, 11, 10]
print(id(e))
print(id(f))

e.append(9)
print(id(e))
print(id(f))
