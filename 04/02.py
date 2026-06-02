import copy


lst1 = [1, 3.6, 9, ['w', '66', 99], 100]
lst2 = copy.deepcopy(lst1)

lst2[3].append("Hello")

print(lst1)
print(id(lst1))
print(lst2)
print(id(lst2))

