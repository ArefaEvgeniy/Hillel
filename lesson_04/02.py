template = "Мене звати {}. Мені {} років. {} це класне ім'я"
template_2 = "Мене звати {0}. Мені {1} років. {0} це класне ім'я"
template_3 = "Мене звати {name}. Мені {age} років. {name} це класне ім'я"

name = input('Enter your name: ')
age = input('Enter your age: ')

new_string = template.format(name, age, name)
print(new_string)
print(template_2.format(name, age))
print(template_3.format(name=name, age=age))

print('-' * 50)
print(template_2.format(age, name))
print(template_3.format(age=age, name=name))

print('-' * 50)
coord = (3, 5)
print('X: {0[0]}; Y: {0[1]}'.format(coord))

print('-' * 50)
print('{:<30}'.format('Євген'))
print('{:>30}'.format('Євген'))
print('{:-^30}'.format('Євген'))
