text = 'Мене звати {}. Мені {} роки. Ім\'я {} класне.'
text2 = 'Мене звати {0}. Мені {1} роки. Ім\'я {0} класне.'
text3 = 'Мене звати {name}. Мені {age} роки. Ім\'я {name} класне.'

print(text.format('Євген', 44, 'Євген'))
print(text2.format('Євген', 44))
print(text3.format(age=44, name='Євген'))

name = 'Євген'
age = 44

print(text3.format(age=age, name=name))

coord = (3, 5)
print('X:{0[0]}, Y:{0[1]}'.format(coord))

print('{:>30} ttr'.format('Євген'))
print('{:<30} ttr'.format('Євген'))
print('{:^30} ttr'.format('Євген'))

print('{:.2}'.format(0.2354355230234))

point = 15.5
total = 22
print('{:.2%}'.format(point/total))
