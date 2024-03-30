template = 'Мене звати {}. Мені {} років. {} дуже класне ім\'я'
template_1 = 'Мене звати {0}. Мені {1} років. {0} дуже класне ім\'я'
template_2 = 'Мене звати {name:^10}. Мені {age} років. {name:^10} дуже класне ім\'я'

name = 'Bob'
age = 22

print(template.format(name, age, name))
print(template_1.format(name, age))
print(template_2.format(age=age, name=name))
print(template_2.format(age=age, name='Vsevolod'))

points = 19.5
total = 22
print('Correct answer: {:.2%}. Total range'.format(points/total))

coord = [[3, 5], [8, 9]]
print('X: {0[0][0]}; Y: {0[1][1]}'.format(coord))
