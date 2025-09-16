a = [1, 4, -5, 6, -10, 8, 6, -7]

b = [x ** 2 for x in a if x % 2 == 0]

print(a)
print(b)

c = {x: 0 if x % 2 == 0 else 1 for x in a if x > 0}
print(c)
