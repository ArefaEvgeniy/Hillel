template = "Мене звати %s. Мені %s років. %s це класне ім'я"
template_2 = "Мене звати %(name)s. Мені %(age)s років. %(name)s це класне ім'я"

name = input('Enter your name: ')
age = input('Enter your age: ')

new_string = template % (name, age, name)
print(new_string)

print(template_2 % {'name': name, 'age': age})
