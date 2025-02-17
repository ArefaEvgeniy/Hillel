my_set = {4, '1', 2, 4, 'TTTYE', False, 4.1, 0, 'ERRETYER', 4, (45, 33, 45)}
my_list = ['1', 2, 'TTTYE', False, 4, 0, 'ERRETYER']

print(my_set)
my_set.discard(5)
print(my_set)
# my_set.clear()
# print(my_set)

new_set_2 = {44, 65456, 2134, 789}

my_set.add(frozenset(new_set_2))
print(my_set)
