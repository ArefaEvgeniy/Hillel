set1 = {1, 2, 3, 7}
set2 = {3, 4, 5, 7, 8}
union_set = set1.union(set2)
union_set_2 = set1 | set2

print(set1)
print(set2)
print(union_set)
print(union_set_2)

print("-" * 20)
intersection_set = set1.intersection(set2)
intersection_set_2 = set1 & set2

print(set1)
print(set2)
print(intersection_set)
print(intersection_set_2)

print("-" * 20)
difference_set = set1.difference(set2)
difference_set_2 = set1 - set2

print(set1)
print(set2)
print(difference_set)
print(difference_set_2)
