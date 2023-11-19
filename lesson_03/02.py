a = 7           # a = 122ff540
b = a           # a = 122ff540  b = 122ff540
print(id(a))
print(id(b))
a = 'Liberty'   # a = 64873af3  b = 122ff540
print('-' * 50)
print(id(a))
print(id(b))
b = 1           # a = 64873af3  b = 40003452

print('-' * 50)
d_1 = True
d_2 = 44 == 44
print(d_1)
print(d_2)
print(id(d_1))
print(id(d_2))

print('-' * 50)
f_1 = 10
f_2 = 80 // 8
print(f_1)
print(f_2)
print(id(f_1))
print(id(f_2))

f_1 = f_1 + 1
print(f_1)
print(f_2)
print(id(f_1))
print(id(f_2))
