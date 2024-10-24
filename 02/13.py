a = "Test"
c = "Test"
b = 3334

d_1 = [1, 2, 3]
d_2 = [1, 2, 3]
d_3 = d_1

print(id(a))
print(id(c))
print(id(b))

print(id(d_1))
print(id(d_2))
print(id(d_3))

d_1.append(0)
print(d_1)
print(d_2)
print(d_3)
