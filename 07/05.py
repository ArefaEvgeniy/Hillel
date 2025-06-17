my_set = {55, 'TT', 0, 'er', '1', 1, 0, 'RR', (1, 2, 3), 55, 443, 55}
my_set_2 = {456, 1, 0, 5555, (1, 2, 3), 55, 'WWW', 0}
my_set_3 = set((456, 1, 0, 5555, (1, 2, 3), 55, 'WWW', 0))

print(my_set)
print(my_set_2)
print(my_set_3)

# {0, 1, 'RR', '1', 'er', 55, 443, 'TT'}
# {0, 'TT', 1, 'RR', 'er', '1', 55, 443}
# {0, 1, '1', 'TT', 'RR', 'er', 55, 443}

print(my_set.union(my_set_2))
print(my_set)
print(my_set.intersection(my_set_2))
print(my_set.difference(my_set_2))

my_list = [55, 'TT', (1, 2, 3), 0, 'er', '1', 1, 0, 'RR', (1, 2, 3), 55, 443, 55, 'TT', 999, 0]
my_list_new = list(set(my_list))
print(my_list_new)
