name = "Alice"
age = 25
height = 1.68

template = "{} is {} years old and {} meters tall. {} this is good name."
template_2 = "{0} is {2} years old and {1} meters tall. {0} this is good name."
template_3 = "{name} is {age} years old and {height} meters tall. {name} this is good name."
print(template)
print(template.format(name, age, height, name))
print(template_2.format(name, height, age))
print(template_3.format(height=height, age=age, name='Bob'))
# print(template % (name, age, height))
# print(template % ('Bob', age, 4.001))
# print(template % (input('Enter your name: '), age, 4.001))
