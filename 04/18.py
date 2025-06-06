a = 250
lst = []

for item in range(10, a, 10):
    lst.append(item)

lst_2 = [x for x in range(10, a, 10)]

print('lst:', lst)
print('lst:', lst_2)
