lst1 = [1, 3.6, 9, 100, None, "Hello", 100, 2, "o", 66, 67, 68, 45, True, 77, 100, 71]

lst2 = lst1[0:5]
print(lst2)

lst3 = lst1[3:9]
print(lst3)
print(lst1)

lst4 = lst1[3:]
print(lst4)

lst4 = lst1[:]  # lst4 = lst1[0:]
print(lst4)

lst5 = lst1[::3]
print(lst5)

lst6 = lst1[7:1]
print(lst6)

lst7 = lst1[7::-1]
print(lst7)

lst8 = lst1[1:5:-1]
print(lst8)

lst1 = [1, 3.6, 9, 100, None, "Hello", 100, 2, "o", 66, 67, 68, 45, True, 77, 100, 71]
lst9 = lst1[::-1]
print(lst9)
