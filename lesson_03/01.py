a = 'df'
v = 45
b, f, t = 1, 2, 3
a_1 = a_2 = a_3 = None
c = [1, 2, 3]
b_1, b_2, b_3 = c
d_1, d_2, d_3 = [1, 2, 3]

# print(b_1)
# print(b_2)
# print(b_3)

c_2 = [1, 2]
e_1, e_2, *e_3 = c_2
print(e_1)
print(e_2)
print(e_3)

v /= 9
# v = v / 9
print(v)

a, v = v, a
print(a)
print(v)
