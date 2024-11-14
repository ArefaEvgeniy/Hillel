my_set = {3, 0, 'red', 'black', 99, -8, (45, 66, 77, 'rt'), 'ert'}
my_set_2 = frozenset((3, 0, 'red', 'black', 99, -8, (45, 66, 77, 'rt'), 'ert'))

print(my_set)
print(my_set_2)

my_set.pop()
my_set.pop()
my_set.pop()

print(my_set)

new_set = {5, 66, 567}
my_set_3 = {3, 0, 'red', 'black', 99, -8, (45, 66, 77, 'rt'), 'ert', frozenset(new_set)}
print(my_set_3)
