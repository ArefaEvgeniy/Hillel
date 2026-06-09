template = "{} is {} years old and {} meters tall. {} - it is a name."
template_2 = "{0} is {1} years old and {2} meters tall. {0} - it is a name."
template_3 = "{name} is {age} years old and {height:.4f} meters tall. {name} - it is a name."


name = "Alice"
age = 25
height = 1.68


print(template)
print(template.format(name, age, height, "Alice"))
print(template_2.format(name, age, height))
print(template_3.format(age=age, name="Alice", height=height))

import math
print(math.pi)  # виведе: 3.141592653589793
print(template_3.format(age=age, name="Alice", height=math.pi))
