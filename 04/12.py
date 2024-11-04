lst = [4, 6, 1, 8, 7, 4, 99]
for item in lst:
    if item % 2 == 0:
        if item == 8:
            break
        continue
    print(item + 1)
else:
    print('ELSE')
