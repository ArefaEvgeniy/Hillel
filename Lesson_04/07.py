a = 15
out_list = []

for i in range(3, a + 1, 2):
    out_list.append(i ** 3)

print(out_list)


a = 7
out_list = []

symbol = 'A'
for _ in range(a):
    out_list.append(symbol)
    symbol += 'A'

print(out_list)
