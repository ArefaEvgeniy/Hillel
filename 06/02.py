my_list = [1, "df", "99", 100, "0", "df", 2, "World", "99", 3, 0, 4, 5, 100, "99", 100, "df"]
my_set = {1, "99", 100, "0", 2, "World", 3, 0, 4, 5, 100, 100, (45, 77, 89), "df"}
my_set_2 = set((1, "99", 2, "World", 3, 0, 4, 5, "df"))
my_set_3 = frozenset((1, "99", 2, "World", 3, 0, 4, 5, "df"))


print(my_set)
print(id(my_set))
print(my_set_2)
print(id(my_set_2))

new_list = []
for item in my_list:
    if item not in new_list:
        new_list.append(item)
print(new_list)

new_list_2 = list(set(my_list))
print(new_list_2)

my_set_3 = {"World", 3, 0, 4, 101, 102, 103}

new_set = my_set.union(my_set_3)
print(new_set)

new_set_2 = my_set.intersection(my_set_3)
print(new_set_2)

new_set_3 = my_set.difference(my_set_3)
print(new_set_3)
