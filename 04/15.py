lst = []
for item in range(21, 5, -2):
    if item > 10:
        lst.append(item ** 2)
print(lst)


lst_2 = [i**2 for i in range(21, 5, -2) if i > 10]
print(lst_2)


input_lst = [4, 66, 234, 87, -56, 0, 556, 12, 34, 8]
lst_3 = [i+2 for i in input_lst if i > 10]
print(lst_3)
