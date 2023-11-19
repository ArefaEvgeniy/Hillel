a = 45
b = 'spam'

c_1, c_2 = 34, 66
print(c_1)
print(c_2)

z = [343, 665]
d_1, d_2 = z
print(d_1)
print(d_2)

e_1, e_2, e_3, e_4 = b
print(e_1)
print(e_2)
print(e_3)
print(e_4)

x_1, *x_2 = b
print(x_1)
print(x_2)

t = (1, 2)
f_1, f_2, *f = t
print(f_1)
print(f_2)
print(f)

w_1 = w_2 = 77
print(w_1)
print(w_2)

print('-' * 50)
print(d_1)
print(d_2)
d_1, d_2 = d_2, d_1
print(d_1)
print(d_2)
