a = 20

new_list = []
# for i in range(a):  # 0, 1, 2, 3, ..., 19
# for i in range(1, a + 1):  # 1, 2, 3, ..., 20
for i in range(1, a + 1, 3):  # 1, 4, 7, 10, 13, 16, 19
    new_list.append(i)

print(new_list)
