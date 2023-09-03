import copy

a = [1, 2, 3, ['q', 'r']]                   # ->  898678687   33345232, 55773446, 98876654, 93999546
first_copy = copy.deepcopy(a)               # ->  689348734   33345232, 55773446, 98876654, 33456355
second_copy = copy.deepcopy(a)              # ->  880000325   33345232, 55773446, 98876654, 56787543
third_copy = a[:]                           # ->  233543212   33345232, 55773446, 98876654, 93999546

print(id(a))
print(id(first_copy))
print(id(second_copy))
print(id(third_copy))

first_copy.append(9)
second_copy.pop(1)
third_copy.extend(first_copy)
third_copy[3].append(99)
print(a)
print(first_copy)
print(second_copy)
print(third_copy)
