
a = 'Bob'
name = "Bob"
full_name = "Bob Black"
print(full_name)
# print = 'rrr'
# print(full_name)

print(id(a))
print(id(name))
print(id(full_name))

name = name + "_1"  # > "Bob_1"
print('-' * 100)

print(id(a))
print(id(name))
print(id(full_name))

number_1 = 67
number_2 = 102000
number_3 = 3

print('-' * 100)
print(id(number_1))
print(id(number_2))
print(id(number_3))

# 140722018148296
# 2855307754480
