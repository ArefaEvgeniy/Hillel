lst1 = [1, 3.6, 9, 100, None, "Hello", 100, 2, "o", 66, 67, 68, 45, True, 77, 100, 71]

print(id(lst1))
lst1.append(0)
print(lst1)
print(id(lst1))

lst1.insert(1, "0")
print(lst1)
print(id(lst1))

lst1.pop(2)
lst1.insert(2, "NEW")
print(lst1)
print(id(lst1))

lst1[2] = "OLD"
print(lst1)
