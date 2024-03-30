template = 'Мене звати %s. Мені %s років. %s дуже класне ім\'я'
template_2 = 'Мене звати %(name)s. Мені %(age)s років. %(name)s дуже класне ім\'я'

name = 'Bob'
age = 22

print(template % (name, age, name))
print(template_2 % {'name': name, 'age': age})
