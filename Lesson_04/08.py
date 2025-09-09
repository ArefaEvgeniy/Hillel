a = 15
out_list = []

for i in range(a):
    if i % 2 != 0:
        out_list.append(i ** 3)

print(out_list)


out_list_2 = [x ** 3 for x in range(a) if x % 2 != 0]
print(out_list_2)
