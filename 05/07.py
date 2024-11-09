name = "Alice"
age = 25
height = 1.68

s = "{} is {} years old and {} meters tall. My name is {}"
s_2 = "{0} is {1} years old and {2} meters tall. My name is {0}"
s_3 = "{name} is {age} years old and {height} meters tall. My name is {name}"
s_4 = "{:^7} is {} years old."


print(s.format(name, age, height, name))
print(s_2.format(name, age, height))

print(s_3.format(name=name, age=46, height=height))
print(s_3.format(name='Bob', age=33, height=1.58))

print(s_4.format(name, age + 5))
print(s_4.format("Bob".upper(), 44))
print(s_4.format("Mikle", 23))
print(s_4.format("Jerryss", 15))
