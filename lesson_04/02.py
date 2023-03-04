template = 'Привет, {}. Я рад, что {} к нам подключился. {} {} лет'
template_2 = 'Привет, {0}. Я рад, что {0} к нам подключился. {0} {1} лет'
template_3 = 'Привет, {name}. Я рад, что {name} к нам подключился. {name} {age} лет'

my_name = input('Enter your name: ')

print(template.format(my_name, my_name, my_name, 25, 66, 88))
print(template_2.format(my_name, 25))
print(template_3.format(age=20, name=my_name))

my_list = (1, 2, 3)
print('X: {0[0]}, Y: {0[1]}, distant: {0[2]}cm'.format(my_list))

names = ['Екатерина', 'Александр', 'Юлия']

print('{0[0]:-<20}\n{0[1]:*^20}\n{0[2]:_>20}'.format(names))

import math
print('PI is: {:.52}'.format(math.pi))

points = 19.5
total = 22
print('{:.2%}'.format(points/total))
