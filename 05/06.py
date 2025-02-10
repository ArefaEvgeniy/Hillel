name = "Alice"
age = 25
height = 1.68

template = "%s is %d years old and %f meters tall"
print(template % (name, age, height))
print(template % ('Bob', age, 4.001))
print(template % (input('Enter your name: '), age, 4.001))
