import copy


lst1 = [1, 3.6, 9, 100]
lst2 = lst1[:]
lst3 = lst1.copy()
lst4 = copy.copy(lst1)

lst2.append(0)
lst2.insert(1, "0")

lst3.pop()

lst4.append(12)
lst4.append(22)

print(lst1)
print(id(lst1))
print(lst2)
print(id(lst2))
print(lst3)
print(id(lst3))
print(lst4)
print(id(lst4))
