lst = [4, 6, 8, 7]
for i, el in enumerate(lst):
    if el > 6:
        print(i, "->", el)

print('-' * 100)

for item in enumerate(lst):
    if item[1] > 6:
        print(item[0], "->", item[1])

# lst = [4, 6, 8, 7]
# i = 0
# for el in lst:
#     if el > 6:
#         print(i, "->", el)
#     i += 1
