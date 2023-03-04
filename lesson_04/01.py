template = 'Привет, %s. Я рад, что %s к нам подключился. %s %d лет'
template_2 = 'Привет, %(name)s. Я рад, что %(name)s к нам подключился. %(name)s %(age)d лет'

my_name = input('Enter your name: ')

print(template % (my_name, my_name, my_name, 15))
print(template_2 % {'name': 'Женя', 'age': 15})
