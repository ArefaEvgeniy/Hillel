lst = [4, 6, 8, 7, [5, 66, 77], False]

for item in enumerate(lst):
    print("item:", item[1], " index:", item[0])

print('-' * 100)

for index, value in enumerate(lst):
    print("item:", value, " index:", index)


for _ in lst:
    a = 100
    b = a / 12
