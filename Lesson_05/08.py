template = 'My name is {}, I am {} years old and I am from {}. {} is the best name!'
template_2 = 'My name is {0}, I am {1} years old and I am from {2}. {0} is the best name!'
template_3 = 'My name is {name}, I am {age} years old and I am from {country}. {name} is the best name!'

...

name = 'Alice'
age = 55
country = 'England'

print(template.format(name, age, country, name))
print(template_2.format(name, age, country))
print(template_3.format(name=name, age=age, country=country))
