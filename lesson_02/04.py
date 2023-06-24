a = (12, 0.55, "dsjhgd sf g", -78)
c = 'Dog'

print(len(a))
print(a[:-1])

b = (c,)
print(b)
print(type(b))

b_2 = tuple((1, 2, 3))
print(b_2)
print(type(b_2))

print(id(a))
print(-78 in a)
