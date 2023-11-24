a = 40

b = []
for item in range(5, a + 1):
    b.append(item ** 2)

print(b)

b_1 = [i ** 2 for i in range(5, a + 1)]
print(b_1)

q = [1, -5, 55, 0, 100, 334]
q_new = [i ** 3 for i in q]
print(q_new)

q = [1, -5, 55, 0, 100, -2, 334]
q_new = [i ** 3 for i in q if i >= 0]
print(q_new)

q = [1, -5, 55, 0, 100, -2, 334]
q_new = [i ** 3 for i in q if 2 == 3]
print(q_new)

a = 'iud3FfdnAjk4t.yhofn,mck5yQ:u00734kg356'
b = [int(i) for i in a if i.isdigit()]
print(b)
b_1 = [int(i) for i in a if '0' <= i <= '9']
print(b_1)

b_2 = [i for i in a if 'a' <= i <= 'z' or 'A' <= i <= 'Z']
print(b_2)
