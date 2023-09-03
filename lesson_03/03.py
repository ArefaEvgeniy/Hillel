a = [1, 2, 3]
first_copy = a
second_copy = a

print(id(a))
print(id(first_copy))
print(id(second_copy))

first_copy.append(9)
second_copy.pop(1)
print(a)
print(first_copy)
print(second_copy)
