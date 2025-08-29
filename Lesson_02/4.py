a = 14  # 140719014696136
b = 14
c = a

print(id(a))
print(id(b))
print(id(c))

d = 8845    # 2859102419952
e = 8845

print(id(d))
print(id(e))

if d is e:
    print("Variables d and e point to the same memory location.")
if id(d) == id(e):
    print("Variables d and e point to the same memory location.")

a = 1235 ** 404
print(a)
