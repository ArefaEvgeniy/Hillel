a = []
for item in range(1, 16):
    a.append(item ** 2)

print(a)

a_2 = [i**2 for i in range(1, 16)]

print(a_2)

b = {1: 10, 2: 20, 3: 30}
b_2 = [key * b[key] for key in b]
b_3 = [key[0] * key[1] for key in b.items()]
b_4 = [key * values for key, values in b.items()]
print(b_2)
print(b_3)
print(b_4)


a = 'dsj435wefds;l6pq34hbmnl78o0re  g laekj340684'

c = [int(i) for i in a if '0' <= i <= '9']

print(c)