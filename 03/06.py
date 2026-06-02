lst1 = [1, 3.6, 9, 100, None, "Hello", 100, [2, "o", [66, 67, 68], 45, True], 77, 100, 71]

print(lst1[5])
print(lst1[-1])

print(lst1[5][2][-1])

if len(lst1) > 8:
    print(lst1[8])

print(100 in lst1)
print(2 in lst1)
print(2 in lst1[7])

print(lst1.count(100))
