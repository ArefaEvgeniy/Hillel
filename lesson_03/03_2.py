import copy

a = [1, 2, 3]               # ->  898678687   33345232, 55773446, 98876654
first_copy = copy.copy(a)   # ->  689348734   33345232, 55773446, 98876654
second_copy = copy.copy(a)  # ->  880000325   33345232, 55773446, 98876654
third_copy = a[:]           # ->  233543212   33345232, 55773446, 98876654

print(id(a))
print(id(first_copy))
print(id(second_copy))
print(id(third_copy))

first_copy.append(9)
second_copy.pop(1)
third_copy.extend(first_copy)
print(a)
print(first_copy)
print(second_copy)
print(third_copy)
